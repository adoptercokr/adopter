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

def search_pids(keyword):
    """키워드로 플레이스 ID 수집"""
    url = f"https://m.search.naver.com/search.naver?query={urllib.parse.quote(keyword)}"
    req = urllib.request.Request(url, headers=HEADERS)
    pids = []
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            found = re.findall(r'place\.naver\.com/accommodation/(\d+)', html)
            found += re.findall(r'place\.naver\.com/place/(\d+)', html)
            for pid in found:
                if pid not in pids:
                    pids.append(pid)
    except Exception as e:
        print(f"검색 실패 ({keyword}): {e}")
    return pids

def inspect_place_apollo(pid):
    """Apollo State 및 HTML 앵커를 정밀 분석하여 홈페이지 보유 여부 완벽 검증"""
    url = f"https://m.place.naver.com/accommodation/{pid}/home"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return None

    # 1. 앵커 태그 검사
    anchors = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL)
    for href, text in anchors:
        text_clean = re.sub(r'<[^>]+>', '', text).strip()
        if '홈페이지' in text_clean:
            return {'has_homepage': True, 'reason': f"Anchor text: {text_clean} -> {href}"}
        # 외부 도메인 검사
        href_lower = href.lower()
        if href_lower.startswith('http') and not any(nd in href_lower for nd in ['naver.com', 'instagram.com', 'facebook.com', 'youtube.com']):
            return {'has_homepage': True, 'reason': f"Anchor external href: {href}"}

    # 2. Apollo State 정밀 검사
    m = re.search(r'window\.__APOLLO_STATE__\s*=\s*(\{.+?\});', html)
    if not m:
        return None
    
    try:
        data = json.loads(m.group(1))
    except Exception:
        return None

    # homepages 검사
    for k, v in data.items():
        if isinstance(v, dict) and 'homepages' in v and v['homepages']:
            hp = v['homepages']
            # etc 목록이 있으면 100% 홈페이지 있음 (예: 보아비양)
            if hp.get('etc') and len(hp['etc']) > 0:
                etc_urls = [item.get('url', '') for item in hp['etc']]
                return {'has_homepage': True, 'reason': f"Apollo homepages.etc: {etc_urls}"}
            # repr 검사
            if hp.get('repr'):
                repr_url = hp['repr'].get('url', '').lower()
                repr_type = hp['repr'].get('type', '')
                if repr_type == '홈페이지' or (repr_url and not any(nd in repr_url for nd in ['naver.com', 'instagram.com', 'facebook.com', 'youtube.com'])):
                    return {'has_homepage': True, 'reason': f"Apollo homepages.repr: {repr_url} ({repr_type})"}

    # PlaceDetailBase 정보 추출
    base = data.get(f'PlaceDetailBase:{pid}', {})
    if not base:
        # 혹시 다른 키로 존재하는지 탐색
        for k, v in data.items():
            if k.startswith('PlaceDetailBase:') and v.get('id') == pid:
                base = v
                break

    name = base.get('name', '')
    if not name:
        return None

    # 전화번호
    phone = base.get('virtualPhone') or base.get('phone') or "0507-0000-0000"
    # 도로명 주소
    road_addr = base.get('roadAddress') or base.get('address') or "제주특별자치도"
    # 대표 설명
    desc = base.get('microReviews', [''])[0] if base.get('microReviews') else "제주 감성 숙소"

    # 인스타그램 링크 추출
    insta_url = ""
    for k, v in data.items():
        if isinstance(v, dict) and 'homepages' in v and v['homepages']:
            hp = v['homepages']
            if hp.get('repr') and 'instagram' in hp['repr'].get('url', '').lower():
                insta_url = hp['repr'].get('url', '')
                break

    # 사진 개수 및 리스트 파악
    images = []
    for k, v in data.items():
        if isinstance(v, dict) and 'origin' in v and str(v.get('origin')).startswith('http'):
            images.append(v['origin'])
        elif isinstance(v, dict) and 'url' in v and 'ldb-phinf' in str(v.get('url')):
            images.append(v['url'])
            
    images = list(dict.fromkeys(images)) # 중복 제거

    return {
        'has_homepage': False,
        'pid': pid,
        'name': name,
        'phone': phone,
        'address': road_addr,
        'desc': desc,
        'instagram': insta_url,
        'image_count': len(images),
        'images': images[:10],
        'url': f"https://m.place.naver.com/accommodation/{pid}/home"
    }

def main():
    queries = [
        "제주 감성 민박", "제주 조천 감성숙소", "제주 한경면 감성숙소", 
        "제주 성산 감성펜션", "제주 남원 감성숙소", "제주 대정 감성숙소",
        "제주 애월 독채펜션", "제주 구좌 감성숙소"
    ]
    
    candidate_pids = []
    for q in queries:
        pids = search_pids(q)
        for p in pids:
            if p not in candidate_pids:
                candidate_pids.append(p)
        if len(candidate_pids) >= 40:
            break
            
    print(f"총 {len(candidate_pids)}개 후보 플레이스 검증 시작...")
    
    pure_targets = []
    
    for pid in candidate_pids:
        info = inspect_place_apollo(pid)
        if not info:
            continue
            
        if info['has_homepage']:
            print(f"❌ [탈락 - 홈페이지 있음] {info['reason']}")
        else:
            print(f"✨ [선정! 진짜 홈페이지 없음] {info['name']} | 전화: {info['phone']} | 주소: {info['address']} | 인스타: {info['instagram']} (사진 {info['image_count']}장)")
            pure_targets.append(info)
            if len(pure_targets) >= 10:
                print("\n🎉 완벽한 10곳 엄선 달성!")
                break
        time.sleep(0.3)
        
    print(f"\n최종 수집 완료: {len(pure_targets)}곳")
    with open("tools/strictly_pure_10_stays.json", "w", encoding="utf-8") as f:
        json.dump(pure_targets, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
