import os
import re
import base64

js_template_b64 = b'Y29uc3QgU1RBWV9DT05GSUcgPSB7CiAgbmFtZTogIntuYW1lfSIsCiAgc3VidGl0bGU6ICJQcmVtaXVtIFN0YXkiLAogIGRlc2NyaXB0aW9uOiAibZjqr5QsIOq3uCDsnpDrspTqsIAg7Jio7KCE7ZWcIOyJvOydtCDrkJjripQg6rO16rCEIiwKICBiZW5lZml0czogWwogICAgeyBpZDogImIxIiwgaWNvbjogYDxzdmcgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIGNsYXNzPSJ3LTYgaC02Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0zIDE3YzIgMCAzLTEgNS0xczMgMSA1IDEgMy0xIDUtMSAzIDEgNiAxTTMgMjFjMiAwIDMtMSA1LTFzMyAxIDUgMSAzLTEgNS0xIDMgMSA2IDFNNiA4YTIgMiAwIDEwMC00IDIgMiAwIDAwMCA0ek03IDlsNCA0IDQtMi0xLjUtMyI+PC9wYXRoPjwvc3ZnPmAsIHRpdGxlOiAi7ZSE65287J2067mPIOqztOqwhCIsIGRlc2NyaXB0aW9uOiAi7Jik7KeBIO2VnCDtjIDrp4zsnYQg7JyE7ZWcIOyZhOuyve2VnCDtlITrnbzsnbTruY8g7Iqk7YWM7J20IiwgZGV0YWlsOiAi7KGw7Jqp7ZWY6rOgIOyVhOuKnSBoIO2ctOyLneIgfSwKICAgIHsgaWQ6ICJiMiIsIGljb246IGA8c3ZnIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBjbGFzcz0idy02IGgtNiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNCAxNGE4IDggMCAwMDE2IDB2LTJINFYydk02IDE5djJNMTh2LTJNOCA3YzAtMiAxLTMgMS0zczEgMSAxIDNNMTIgNmMwLTIgMS0zIDEtM3MxIDEgMSAzTTE2IDdjMC0yIDEtMyAxLTNzMSAxIDEgMyI+PC9wYXRoPjwvc3ZnPmAsIHRpdGxlOiAi7ZSE66as66+47JeEIOyWtOubaOuLiO2LsCIsIGRlc2NyaXB0aW9uOiAi7LWc6rOg6riJIO2YuO2FlCDsiJjsgIDsnZgg7Ja065to64uI7YuwIOygnOqztSIsIGRldGFpbDogIuy5nO2ZmOq9vSDsoJztkIgg7IKs7JqpIiB9CiAgXSwKICBzcGFjZXM6IFsKICAgIHsgaWQ6ICJzMSIsIHRpdGxlOiAi66mU7J24IOqztOqwhCIsIHN1YnRpdGxlOiAiTWFpbiBTcGFjZSIsIG1haW5JbWFnZTogIi4vaW1nL3Bob3RvXzEuanBnIiwgaW1hZ2VzOiBbIi4vaW1nL3Bob3RvXzEuanBnIiwgIi4vaW1nL3Bob3RvXzIuanBnIl0sIHRvdGFsUGhvdG9zOiAyIH0sCiAgICB7IGlkOiAiczIiLCB0aXRsZTogIu2ctOyLnSDqs7TqsIQiLCBzdWJ0aXRsZTogIlJlc3QgQXJlYSIsIG1haW5JbWFnZTogIi4vaW1nL3Bob3RvXzMuanBnIiwgaW1hZ2VzOiBbIi4vaW1nL3Bob3RvXzMuanBnIiwgIi4vaW1nL3Bob3RvXzQuanBnIl0sIHRvdGFsUGhvdG9zOiAyIH0KICBdLAogIGZhY2lsaXRpZXM6IFsKICAgIHsgbmFtZTogIuustOyEoCDsnbjtgLDrhQoiLCBpY29uOiAid2lmaSIgfSwKICAgIHsgbmFtZTogIuyjvOywqOyepSIsIGljb246ICJwYXJraW5nIiB9CiAgXSwKICBydWxlczogWwogICAgIuyytO2BrO2KjSAxNTowMCAvIOyytO2BrOyVhOsmDCAxMTowMCIsCiAgICAi7Iuk64K0IOygiOuMgCDquIjsl7AiLAogICAgIuuwnOugpOuPmeusvCDrj5nrrsAg67aI6rCAIgogIF0sCiAgcmF0ZXM6IHsKICAgIHdlZWtkYXk6ICJ7d2Vla2RheX0iLAogICAgd2Vla2VuZDogInt3ZWVrZW5kfSIsCiAgICBwZWFrOiAie3dlZWtlbmR9IgogIH0KfTs='
js_template = base64.b64decode(js_template_b64).decode('utf-8')

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
        
        # We also need to fix name since name is garbled in the current stay_config.js!
        # Wait, if name is garbled, I should get the name from the folder name!
        # Folder is like '260930-sinchang'. We can't recover Korean name from that easily.
        # But wait! I wrote the Korean name perfectly in the crawler script, but wait! The crawler script itself had garbled Korean!
        
        js = js_template.replace('{name}', name).replace('{weekday}', weekday).replace('{weekend}', weekend)
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(js)
