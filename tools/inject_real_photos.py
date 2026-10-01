import json, os, re

ADOPTER = r'c:\nas\mj\비즈니스\유튜브-SNS-캐릭터-애니\ai사이트\AI-mj공작실\01-Nova-Web-Studio\adopter'

with open('tools/naver_photos.json','r',encoding='utf-8') as f:
    photo_db = json.load(f)

# 4곳은 인스타 없어서 Unsplash 사용 (분위기에 맞게)
fallback_sets = {
    '260930-haily': [
        'https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1515263487990-61b07816b324?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1540518614846-7eded433c457?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1618140052121-39fc6db33972?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&q=80&w=1920'
    ],
    '260930-huahin': [
        'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1549294413-26f195200c16?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1542314831-c6a4d14faaf2?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1501183638710-841dd1904471?auto=format&fit=crop&q=80&w=1920'
    ],
    '260930-geumneung': [
        'https://images.unsplash.com/photo-1510798831971-661eb04b3739?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1574362848149-11496d93a7c7?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1505873242700-f289a29e1e0f?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1598928506311-c55dd1b212f7?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1600585154526-990dced4ea0d?auto=format&fit=crop&q=80&w=1920'
    ],
    '260930-mongdol': [
        'https://images.unsplash.com/photo-1590490359683-658d3d23f972?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1616486029423-aaa4789e8c9a?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1484154218962-a197022b5858?auto=format&fit=crop&q=80&w=1920',
        'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&q=80&w=1920'
    ]
}

all_folders = list(photo_db.keys()) + list(fallback_sets.keys())

for folder in all_folders:
    imgs = photo_db.get(folder, fallback_sets.get(folder, []))
    if not imgs:
        continue

    folder_path = os.path.join(ADOPTER, 'Customer', folder)
    if not os.path.exists(folder_path):
        print(f'SKIP (not found): {folder}')
        continue

    for filename in ['index.html', 'stay_config.js']:
        filepath = os.path.join(folder_path, filename)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find ALL image references and replace with real ones
        pattern = r'(?:\./img/[a-zA-Z0-9_\-]+\.(?:jpg|png|webp)|\.\./img/[a-zA-Z0-9_\-]+\.(?:jpg|png|webp)|https://images\.unsplash\.com/[^\"\'>\s]+|https://search\.pstatic\.net/[^\"\'>\s]+)'
        found = re.findall(pattern, content)
        seen = set()
        unique = [x for x in found if not (x in seen or seen.add(x))]

        for i, old in enumerate(unique):
            new = imgs[i % len(imgs)]
            content = content.replace(old, new)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f'Injected REAL photos into {folder}')
