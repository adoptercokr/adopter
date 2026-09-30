import os
import shutil
import re

src_img = 'Customer/260930-moheomdam/img'
dst_img = 'Customer/tpl-01-heestay/img'

if os.path.exists(dst_img):
    shutil.rmtree(dst_img)
shutil.copytree(src_img, dst_img)

config_path = 'Customer/tpl-01-heestay/stay_config.js'
with open(config_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace all Korean image paths with photo_1.jpg, photo_2.jpg...
count = 1
def replacer(match):
    global count
    res = f"'./img/photo_{(count % 10) + 1}.jpg'"
    count += 1
    return res

js = re.sub(r"'\./img/.*?\.jpg'", replacer, js)

with open(config_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Fixed tpl-01-heestay images")
