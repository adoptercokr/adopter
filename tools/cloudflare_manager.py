import urllib.request
import json
import os
import subprocess
from pathlib import Path

# Load secrets from gitignored config or env
secrets_path = Path(__file__).resolve().parent.parent / "cloudflare_secrets.json"
if secrets_path.exists():
    with open(secrets_path, "r", encoding="utf-8") as f:
        config = json.load(f)
else:
    config = {}

CF_API_TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN", config.get("CF_API_TOKEN", ""))
CF_ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID", config.get("CF_ACCOUNT_ID", ""))
CF_PROJECT_NAME = config.get("CF_PROJECT_NAME", "adopter")

def register_custom_domain(subdomain: str) -> bool:
    """
    Cloudflare Pages 프로젝트에 서브도메인을 자동으로 등록합니다.
    예: subdomain='moheomdam' -> 'moheomdam.adopter.co.kr'
    """
    domain = f"{subdomain}.adopter.co.kr" if not subdomain.endswith(".adopter.co.kr") else subdomain
    url = f"https://api.cloudflare.com/client/v4/accounts/{CF_ACCOUNT_ID}/pages/projects/{CF_PROJECT_NAME}/domains"
    
    payload = json.dumps({"name": domain}).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {CF_API_TOKEN}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"[{domain}] Cloudflare Pages 도메인 자동 등록 성공: {data.get('success')}")
            return True
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode()
        if "already exists" in err_msg or "8000040" in err_msg:
            print(f"[{domain}] 이미 등록되어 있는 도메인입니다.")
            return True
        print(f"[{domain}] 도메인 등록 실패 (HTTP {e.code}): {err_msg}")
        return False
    except Exception as e:
        print(f"[{domain}] 에러 발생: {e}")
        return False

def deploy_pages(project_dir: str = ".") -> bool:
    """
    Wrangler를 사용하여 Cloudflare Pages에 원클릭 무인 배포합니다.
    """
    env = os.environ.copy()
    env["CLOUDFLARE_API_TOKEN"] = CF_API_TOKEN
    env["CLOUDFLARE_ACCOUNT_ID"] = CF_ACCOUNT_ID
    
    cmd = ["npx.cmd", "wrangler", "pages", "deploy", project_dir, f"--project-name={CF_PROJECT_NAME}", "--branch=main", "--commit-dirty=true"]
    try:
        res = subprocess.run(cmd, env=env, capture_output=True, text=True, cwd=project_dir)
        if res.returncode == 0:
            print("[배포 성공] Cloudflare Pages에 정상 배포되었습니다.")
            return True
        else:
            print(f"[배포 실패] {res.stderr or res.stdout}")
            return False
    except Exception as e:
        print(f"[배포 실행 에러] {e}")
        return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sub = sys.argv[1]
        register_custom_domain(sub)
    else:
        print("Usage: python cloudflare_manager.py <subdomain>")
