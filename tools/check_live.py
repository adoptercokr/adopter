import urllib.request

req = urllib.request.Request('https://moheomdam.adopter.co.kr/', headers={'User-Agent': 'Mozilla/5.0'})
c = urllib.request.urlopen(req).read().decode('utf-8')
gal_pos = c.find('id="gallery"')
cal_pos = c.find('id="calendar-section"')

print('--- Live moheomdam.adopter.co.kr Status ---')
print('1. Gallery pos:', gal_pos, ', Calendar pos:', cal_pos)
print('   -> Gallery before Calendar?:', gal_pos < cal_pos)
print('2. Has favicon.svg?:', 'favicon.svg' in c)
print('   -> Empty icon data:,?:', 'href="data:,"' in c)
print('3. Has room1_1 to room1_10?:', all(f'room1_{i}.jpg' in c for i in range(1, 11)))
print('   Has room2_1 to room2_10?:', all(f'room2_{i}.jpg' in c for i in range(1, 11)))
print('   Has room3_1 to room3_10?:', all(f'room3_{i}.jpg' in c for i in range(1, 11)))
print('4. Has roomAmenitiesGrid?:', 'id="roomAmenitiesGrid"' in c)
print('   Has roomConfigCards?:', 'id="roomConfigCards"' in c)
print('   Has roomPhotoIndex/Total?:', 'id="roomPhotoIndex"' in c and 'id="roomPhotoTotal"' in c)
print('-------------------------------------------')
