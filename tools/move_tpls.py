import os, shutil

os.makedirs('Customer', exist_ok=True)
tpls = os.listdir('templates')
for t in tpls:
    src = os.path.join('templates', t)
    dst = os.path.join('Customer', 'tpl-' + t)
    if os.path.isdir(src):
        if os.path.exists(dst): shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"Moved {t} to Customer/tpl-{t}")
