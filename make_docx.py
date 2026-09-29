import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

doc = docx.Document()

# 제목
title = doc.add_heading('📘 어댑터(adopter.co.kr) 웹사이트 전체 구조 및 운영 매뉴얼', 0)
title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

doc.add_paragraph('본 문서는 프로그래밍 초보자도 어댑터 웹사이트가 어떻게 만들어지고 돌아가는지, 어떻게 스스로 수정할 수 있는지 완벽하게 이해할 수 있도록 작성된 가이드입니다.\n')

# 1. 시스템 구조 
doc.add_heading('1. 웹사이트 제작 및 운영 3단계 핵심 구조', level=1)
doc.add_paragraph('현재 어댑터 웹사이트는 최신 AI 기술과 무료 클라우드 서버를 결합하여 "유지비 0원"으로 24시간 안전하게 돌아가도록 설계되었습니다.')

p = doc.add_paragraph()
p.add_run('① AI 에이전트 (Claude / Gemini 등) - "개발자 역할"\n').bold = True
p.add_run('사용자가 직접 복잡한 코드를 짜지 않아도 됩니다. AI에게 "포트폴리오 사이트에 새로운 작업물을 추가해줘"라고 명령하면 AI가 HTML 코드를 작성하고 수정해 줍니다.')

p = doc.add_paragraph()
p.add_run('② 깃허브 (GitHub) - "온라인 코드 창고"\n').bold = True
p.add_run('AI나 사용자가 수정한 모든 소스코드와 사진 파일이 영구적으로 백업되는 저장소입니다. 윈도우의 폴더와 똑같지만, 인터넷에 공개/비공개로 저장되는 창고입니다.\n')
p.add_run('👉 어댑터 저장소 링크: https://github.com/adoptercokr/adopter')

p = doc.add_paragraph()
p.add_run('③ 클라우드플레어 (Cloudflare Pages) - "무료 웹 서버"\n').bold = True
p.add_run('깃허브(창고)에 있는 코드를 전 세계 사람들이 볼 수 있도록 24시간 띄워주는 "웹 서버" 역할을 합니다. 사용자가 사이트에 접속할 때 굉장히 빠른 속도로 화면을 보여주며 트래픽 무제한 무료 호스팅을 제공합니다.\n')
p.add_run('👉 클라우드플레어 링크: https://dash.cloudflare.com')

# 2. 폴더 구조
doc.add_heading('2. 현재 폴더(파일)의 상세 구조', level=1)
doc.add_paragraph('내 컴퓨터의 [01-Nova-Web-Studio/adopter] 폴더를 열면 여러 파일이 있습니다.')

doc.add_paragraph('• portfolio.html : 웹사이트의 [포트폴리오] 메뉴를 담당하는 핵심 파일입니다. 이 안에 텍스트를 수정하면 화면 글자가 바뀝니다.')
doc.add_paragraph('• index.html : 웹사이트의 첫 메인 화면입니다.')
doc.add_paragraph('• img/ 폴더 : 웹사이트에 보이는 모든 사진(캡처화면, 로고 등)이 들어있는 곳입니다. 새로운 포트폴리오 사진을 넣으려면 무조건 이 폴더 안에 사진을 복사해 넣어야 합니다.')
doc.add_paragraph('• CNAME 파일 : "이 폴더의 코드를 adopter.co.kr 주소로 띄워라" 라고 지시하는 도메인 방향키 파일입니다. 절대 삭제하면 안 됩니다.')

# 3. 업데이트 방법
doc.add_heading('3. 실전 웹사이트 업데이트(배포) 가이드', level=1)
doc.add_paragraph('웹사이트의 글자나 사진을 수정한 후, 실제 인터넷에 반영(업데이트)하는 방법에는 2가지가 있습니다.')

doc.add_heading('방법 A: GitHub 자동 배포 (가장 권장하는 표준 방식)', level=2)
doc.add_paragraph('VS Code 터미널 창을 열고, 아래 3줄의 명령어를 한 줄씩 치고 엔터를 누릅니다.')
p = doc.add_paragraph('1) git add .\n2) git commit -m "어떤 내용을 수정했는지 메모 작성"\n3) git push origin main')
p.style = 'Intense Quote'
doc.add_paragraph('위 명령어를 치면 내 컴퓨터에서 수정한 내용이 깃허브(창고)로 즉시 전송됩니다. 깃허브에 코드가 올라가면 Cloudflare 서버가 이를 자동으로 감지하여 1~2분 뒤 실제 웹사이트를 새 버전으로 갱신해 줍니다.')

doc.add_heading('방법 B: 클라우드플레어 수동 드래그 업로드 (GitHub 연동이 끊겼을 때)', level=2)
doc.add_paragraph('명령어 치는 것이 너무 어렵거나 GitHub 자동 연동이 안 되어 있을 경우 사용하는 비상용(또는 초보자용) 방법입니다.')
doc.add_paragraph('1) 바탕화면에 현재 작업 중인 전체 폴더(adopter)를 하나의 zip 압축파일(예: adopter_배포.zip)로 만듭니다.')
doc.add_paragraph('2) 클라우드플레어 관리자 화면(https://dash.cloudflare.com)에 로그인합니다.')
doc.add_paragraph('3) [Pages] 탭에서 adopter 프로젝트를 누르고, 방금 만든 압축파일(zip)을 마우스로 화면에 끌어다 놓습니다 (Drag & Drop).')
doc.add_paragraph('4) 10초 만에 파일이 통째로 덮어씌워지며 바로 사이트가 업데이트됩니다.')

# 4. 유지보수 팁
doc.add_heading('4. 초보자를 위한 유지보수 꿀팁', level=1)
doc.add_paragraph('• 사진이 안 뜰 때: HTML 코드에 적힌 사진 이름(예: img/사진.jpg)과 실제 img 폴더 안의 파일 이름이 대소문자까지 100% 똑같은지 확인하세요.')
doc.add_paragraph('• 사이트가 망가졌을 때: 깃허브에는 언제든 과거 시점으로 100% 되돌릴 수 있는 타임머신 복구 기능이 있습니다. 망가지면 AI에게 "과거 커밋으로 복구해 줘"라고 명령하시면 즉시 고쳐줍니다.')
doc.add_paragraph('• 캐시 문제: 수정을 완료했는데 사이트에 안 뜰 경우, 컴퓨터 브라우저가 옛날 화면을 기억(캐시)하고 있어서 그럴 수 있습니다. [Ctrl + Shift + R] 을 눌러 강력 새로고침을 하거나, 휴대폰으로 접속해 보세요.')

doc.save('초보자용_사이트_운영가이드_상세본.docx')
print("Detailed DOCX created successfully.")
