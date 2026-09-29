import urllib.request
import urllib.parse
import re
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
}

def search_naver_places(keyword, max_pages=3):
    """네이버 모바일 통합 검색에서 플레이스 목록 추출"""
    place_ids = []
    print(f"🔍 키워드 검색: {keyword}")
    for page in range(1, max_pages + 1):
        url = f"https://m.search.naver.com/search.naver?query={urllib.parse.quote(keyword)}&page={page}"
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                ids = re.findall(r'place\.naver\.com/accommodation/(\d+)', html)
                ids += re.findall(r'place\.naver\.com/place/(\d+)', html)
                for pid in ids:
                    if pid not in place_ids:
                        place_ids.append(pid)
        except Exception as e:
            print(f"  검색 에러 ({keyword}): {e}")
        time.sleep(0.5)
    return place_ids

def inspect_place(pid):
    """플레이스 상세 정보 및 외부 홈페이지 여부 엄격 판별"""
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return None

    # 1. 앵커 태그 분석
    anchors = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
    
    instagram_url = ""
    blog_url = ""
    has_homepage = False
    homepage_url = ""
    
    # 제외 대상 도메인 (네이버 자체 서비스)
    NAVER_DOMAINS = [
        'naver.com', 'nmap.place.naver.com', 'map.naver.com', 'help.naver.com',
        'policy.naver.com', 'nid.naver.com', 'm.place.naver.com'
    ]
    
    for href, text in anchors:
        text_clean = re.sub(r'<[^>]+>', '', text).strip()
        href_lower = href.lower()
        
        # 앵커 텍스트에 '홈페이지'가 있으면 100% 홈페이지 보유
        if '홈페이지' in text_clean:
            has_homepage = True
            homepage_url = href
            break
            
        if 'instagram.com' in href_lower:
            instagram_url = href
            continue
            
        if 'blog.naver.com' in href_lower:
            blog_url = href
            continue
            
        # http/https 외부 링크 체크
        if href_lower.startswith('http://') or href_lower.startswith('https://'):
            is_naver = any(nd in href_lower for nd in NAVER_DOMAINS)
            if not is_naver:
                # 외부 도메인이 걸려 있으면 홈페이지로 판정
                # 예: imweb.me, modoo.at, stayfolio, 자체도메인 등
                has_homepage = True
                homepage_url = href
                break

    # 이미 홈페이지가 있으면 즉시 탈락!
    if has_homepage:
        return {
            'pid': pid,
            'has_homepage': True,
            'homepage_url': homepage_url
        }

    # 홈페이지가 없는 경우, 기본 정보 추출
    # 업체명 추출
    name_match = re.search(r'<span class="GHAhO">([^<]+)</span>', html)
    if not name_match:
        name_match = re.search(r'<title>([^<]+?)(?:\s*:\s*네이버)?</title>', html)
    name = name_match.group(1).strip() if name_match else f"숙소-{pid}"

    # 전화번호
    phone_match = re.search(r'<span class="xlx7Q">([0-9-]+)</span>', html)
    phone = phone_match.group(1).strip() if phone_match else "0507-0000-0000"

    # 주소
    addr_match = re.search(r'<span class="LDgIH">([^<]+)</span>', html)
    addr = addr_match.group(1).strip() if addr_match else "제주특별자치도"

    # 사진 개수 체크 (이미지 태그 검사)
    images = re.findall(r'https://ldb-phinf\.pstatic\.net/[^"\']+', html)
    img_count = len(set(images))

    return {
        'pid': pid,
        'has_homepage': False,
        'name': name,
        'phone': phone,
        'address': addr,
        'instagram': instagram_url,
        'blog': blog_url,
        'img_count': img_count,
        'url': f"https://m.place.naver.com/accommodation/{pid}/home"
    }

def main():
    keywords = [
        "제주 감성 숙소", "제주 애월 펜션", "제주 구좌 숙소",
        "제주 서귀포 감성펜션", "제주 협재 펜션", "제주 조천 민박"
    ]
    
    all_pids = []
    for kw in keywords:
        pids = search_naver_places(kw, max_pages=2)
        for pid in pids:
            if pid not in all_pids:
                all_pids.append(pid)
        if len(all_pids) >= 30:
            break
            
    print(f"\n총 {len(all_pids)}개의 후보 플레이스 발견. 정밀 검사 시작...\n")
    
    verified_targets = []
    
    for pid in all_pids:
        res = inspect_place(pid)
        if not res:
            continue
            
        if res['has_homepage']:
            print(f"❌ [제외 - 홈페이지 보유] ID {pid}: {res['homepage_url']}")
        else:
            print(f"✅ [선정 - 홈페이지 없음!] {res['name']} | 전화: {res['phone']} | 인스타: {res['instagram']} (사진 {res['img_count']}장)")
            verified_targets.append(res)
            if len(verified_targets) >= 10:
                print("\n🎉 목표 10곳 엄선 완료!")
                break
        time.sleep(0.3)
        
    print(f"\n최종 엄선된 타겟 수: {len(verified_targets)}")
    with open("tools/verified_strictly_no_homepage.json", "w", encoding="utf-8") as f:
        json.dump(verified_targets, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
