import os, urllib.request

img_dir = 'Customer/260930-staypanpo/img'
os.makedirs(img_dir, exist_ok=True)

urls = [
    "https://ldb-phinf.pstatic.net/20230524_221/16849040974868o2m1_JPEG/2.jpg",
    "https://ldb-phinf.pstatic.net/20230524_267/1684904097893oM1zK_JPEG/1.jpg",
    "https://ldb-phinf.pstatic.net/20230524_288/1684904098251zDk53_JPEG/3.jpg",
    "https://ldb-phinf.pstatic.net/20230524_156/1684904098614jD1s4_JPEG/4.jpg",
    "https://ldb-phinf.pstatic.net/20230524_281/1684904098939kF1jM_JPEG/5.jpg"
]

for i, u in enumerate(urls):
    req = urllib.request.Request(u, headers={'Referer': 'https://m.place.naver.com/'})
    with open(f'{img_dir}/photo_{i+1}.jpg', 'wb') as f:
        f.write(urllib.request.urlopen(req).read())

with open('Customer/260930-staypanpo/stay_config.js', 'r', encoding='utf-8') as f:
    js = f.read()

for i in range(5):
    js = js.replace(urls[i], f'./img/photo_{i+1}.jpg')

# Cache bust
js = js.replace('stay_config.js?v=', 'stay_config.js?v=99')

with open('Customer/260930-staypanpo/stay_config.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Downloaded images for Panpo")
