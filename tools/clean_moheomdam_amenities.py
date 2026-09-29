import re

paths = [
    "Customer/260930-moheomdam-모험담/index.html",
    "moheomdam/index.html",
    "moheomdam.html"
]

for p in paths:
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()

    # Simplify amenities in DEFAULT_ROOMS
    c = c.replace(
        """        amenities: [
          { icon: "🏊", name: "풀빌라" },
          { icon: "📺", name: "OTT" },
          { icon: "🧴", name: "욕실용품" },
          { icon: "📶", name: "와이파이" },
          { icon: "🍳", name: "취사가능" },
          { icon: "<svg class="w-4 h-4 inline-block text-stone-600 mr-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><line x1="2" y1="8" x2="22" y2="8"/><line x1="2" y1="16" x2="22" y2="16"/><line x1="7" y1="4" x2="7" y2="8"/><line x1="17" y1="4" x2="17" y2="8"/></svg>", name: "VOD" },
          { icon: "🌿", name: "테라스" }
        ],""",
        """        amenities: [
          { name: "풀빌라" },
          { name: "OTT" },
          { name: "욕실용품" },
          { name: "와이파이" },
          { name: "취사가능" },
          { name: "VOD" },
          { name: "테라스" }
        ],"""
    )

    # Room 2
    c = re.sub(
        r'amenities:\s*\[\s*\{\s*icon:\s*"[^"]*",\s*name:\s*"원형벽난로"\s*\}.*?\{\s*icon:\s*"[^"]*",\s*name:\s*"테라스"\s*\}\s*\]',
        '''amenities: [
          { name: "원형벽난로" },
          { name: "OTT" },
          { name: "욕실용품" },
          { name: "와이파이" },
          { name: "취사가능" },
          { name: "커피머신" },
          { name: "테라스" }
        ]''',
        c,
        flags=re.DOTALL
    )

    # Room 3
    c = re.sub(
        r'amenities:\s*\[\s*\{\s*(?:icon:.*?name:\s*"풀빌라"|name:\s*"풀빌라").*?\{\s*(?:icon:.*?name:\s*"바베큐"|name:\s*"바베큐")\s*\}\s*\]',
        '''amenities: [
          { name: "프라이빗풀" },
          { name: "노천자쿠지" },
          { name: "야외불멍" },
          { name: "OTT" },
          { name: "욕실용품" },
          { name: "와이파이" },
          { name: "바베큐" }
        ]''',
        c,
        flags=re.DOTALL
    )

    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Cleaned DEFAULT_ROOMS amenities in {p}")
