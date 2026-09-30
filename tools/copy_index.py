import os
import shutil

template_html = r"templates\01-stay\index.html"
customer_dir = "Customer"

for d in os.listdir(customer_dir):
    p = os.path.join(customer_dir, d)
    if os.path.isdir(p) and d.startswith("260930-"):
        dest = os.path.join(p, "index.html")
        shutil.copy2(template_html, dest)
        print(f"Copied to {dest}")
