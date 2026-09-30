from playwright.sync_api import sync_playwright

def test_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        page.goto("https://m.place.naver.com/accommodation/2036409548/home")
        page.wait_for_selector("body", timeout=5000)
        import time
        time.sleep(2)
        html = page.content()
        with open("naver_test.html", "w", encoding="utf-8") as f:
            f.write(html)
        browser.close()

test_playwright()
