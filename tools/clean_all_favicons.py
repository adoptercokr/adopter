import os
import glob
import re

# 1. Delete all favicon.svg in Customer/
for f in glob.glob('Customer/*/favicon.svg'):
    try:
        os.remove(f)
        print('Deleted:', f)
    except Exception as e:
        print('Error deleting:', f, e)

# 2. Replace favicon tags in Customer/*/index.html
for f in glob.glob('Customer/*/index.html'):
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
        c = re.sub(r'<link rel=["\']icon["\'][^>]*>', '<link rel="icon" href="data:,">', c)
        c = re.sub(r'<link rel=["\']apple-touch-icon["\'][^>]*>', '', c)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print('Cleaned favicon in:', f)
    except Exception as e:
        print('Error cleaning html:', f, e)

print('All favicons completely cleaned across Customer/!')
