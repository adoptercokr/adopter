import os, shutil

base = 'Customer'
fallback_img_dir = os.path.join(base, '260930-moheomdam', 'img')

for d in os.listdir(base):
    if not d.startswith('260930-'): continue
    target_img = os.path.join(base, d, 'img')
    
    # If the folder doesn't exist, create it
    if not os.path.exists(target_img):
        os.makedirs(target_img, exist_ok=True)
    
    # Check how many files are inside
    files = os.listdir(target_img)
    
    # If there are no jpg files, copy from fallback
    if len(files) < 3:
        print(f"Copying fallback images to {d}...")
        for f in os.listdir(fallback_img_dir):
            if f.endswith('.jpg'):
                shutil.copy(os.path.join(fallback_img_dir, f), os.path.join(target_img, f))
