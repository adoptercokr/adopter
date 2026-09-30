import os
import re

dirs = os.listdir('Customer')
for d in dirs:
    p = os.path.join('Customer', d, 'stay_config.js')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        name_match = re.search(r'name:\s*\"(.*?)\"', content)
        name = name_match.group(1) if name_match else d
        prices = re.search(r'weekday:\s*\"(.*?)\"', content)
        weekday = prices.group(1) if prices else '200,000'
        prices2 = re.search(r'weekend:\s*\"(.*?)\"', content)
        weekend = prices2.group(1) if prices2 else '250,000'
        
        bt = chr(96)
        
        # Unicode escaped strings to prevent CP949 garbling
        desc = '\uBA38\uBBA4, \uADF8 \uC790\uCCB4\uAC00 \uC628\uC804\uD55C \uC27C\uC774 \uB418\uB294 \uACF5\uAC04'
        title_b1 = '\uD504\uB77C\uC774\uBE57 \uACF5\uAC04'
        desc_b1 = '\uC624\uC9C1 \uD55C \uD300\uB9CC\uC744 \uC704\uD55C \uC644\uBCBD\uD55C \uD504\uB77C\uC774\uBE57 \uC2A4\uD14C\uC774'
        detail_b1 = '\uC870\uC6A9\uD558\uACE0 \uC544\uB291\uD55C \uD734\uC2DD'
        title_b2 = '\uD504\uB9AC\uBBF8\uC5C4 \uC5B4\uBA54\uB2C8\uD2F0'
        desc_b2 = '\uCD5C\uACE0\uAE09 \uD638\uD154 \uC218\uC900\uC758 \uC5B4\uBA54\uB2C8\uD2F0 \uC81C\uACF5'
        detail_b2 = '\uCE5C\uD658\uACBD \uC81C\uD488 \uC0AC\uC6A9'
        title_s1 = '\uBA54\uC778 \uACF5\uAC04'
        title_s2 = '\uD734\uC2DD \uACF5\uAC04'
        fac_1 = '\uBB34\uC120 \uC778\uD130\uB137'
        fac_2 = '\uC8FC\uCC28\uC7A5'
        rule_1 = '\uCCB4\uD06C\uC778 15:00 / \uCCB4\uD06C\uC544\uC6C3 11:00'
        rule_2 = '\uC2E4\uB0B4 \uC808\uB300 \uAE08\uC5F0'
        rule_3 = '\uBC18\uB824\uB3D9\uBB3C \uB3D9\uBC18 \uBD88\uAC00'

        js = f'''const STAY_CONFIG = {{
  name: "{name}",
  subtitle: "Premium Stay",
  description: "{desc}",
  benefits: [
    {{ id: "b1", icon: {bt}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M3 17c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M3 21c2 0 3-1 5-1s3 1 5 1 3-1 5-1 3 1 6 1M16 8a2 2 0 100-4 2 2 0 000 4zM7 9l4 4 4-2-1.5-3"></path></svg>{bt}, title: "{title_b1}", description: "{desc_b1}", detail: "{detail_b1}" }},
    {{ id: "b2", icon: {bt}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M4 14a8 8 0 0016 0v-2H4v2zM6 19v2M18 19v2M8 7c0-2 1-3 1-3s1 1 1 3M12 6c0-2 1-3 1-3s1 1 1 3M16 7c0-2 1-3 1-3s1 1 1 3"></path></svg>{bt}, title: "{title_b2}", description: "{desc_b2}", detail: "{detail_b2}" }}
  ],
  spaces: [
    {{ id: "s1", title: "{title_s1}", subtitle: "Main Space", mainImage: "./img/photo_1.jpg", images: ["./img/photo_1.jpg", "./img/photo_2.jpg"], totalPhotos: 2 }},
    {{ id: "s2", title: "{title_s2}", subtitle: "Rest Area", mainImage: "./img/photo_3.jpg", images: ["./img/photo_3.jpg", "./img/photo_4.jpg"], totalPhotos: 2 }}
  ],
  facilities: [
    {{ name: "{fac_1}", icon: "wifi" }},
    {{ name: "{fac_2}", icon: "parking" }}
  ],
  rules: [
    "{rule_1}",
    "{rule_2}",
    "{rule_3}"
  ],
  rates: {{
    weekday: "{weekday}",
    weekend: "{weekend}",
    peak: "{weekend}"
  }}
}};
'''
        with open(p, 'w', encoding='utf-8') as f:
            f.write(js)
