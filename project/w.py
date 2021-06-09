import requests
import re as cut
from bs4 import BeautifulSoup as bs

html = requests.get('https://search.naver.com/search.naver?query=날씨')

box = bs(html.text, 'html.parser')

css = box.find('div', {'class': 'weather_box'})

location = css.find('span', {'class':'btn_select'}).text
temp = css.find('span', {'class':'todaytemp'}).text

arr = css.findAll('dd') 
dust = arr[0].find('span', {'class':'num'}).text
minidust = arr[1].find('span', {'class':'num'}).text
ozone = arr[2].find('span', {'class':'num'}).text

dust_list = cut.findall("\d+", dust)
dust_num = int(dust_list[0])

minidust_list = cut.findall("\d+", minidust)
minidust_num = int(minidust_list[0])

ozon_list = cut.findall("\d+", ozone)
ozon_num = float(ozon_list[0])

if dust_num <= 30:
    dust_str = "좋습니다."
elif dust_num <= 80:
    dust_str = "보통입니다."
elif dust_num <= 150:
    dust_str = "나쁩니다."
elif dust_num > 150:
    dust_str = "최악입니다."

if minidust_num <= 15:
    minidust_str = "좋습니다."
elif minidust_num <= 35:
    minidust_str = "보통입니다."
elif minidust_num <= 100:
    minidust_str = "나쁩니다."
elif minidust_num > 100:
    minidust_str = "최악입니다."

temp_num = int(temp)

if temp_num < 0:
    temp_str = "매우 춥습니다."
elif temp_num <= 10:
    temp_str = "춥습니다."
elif temp_num <= 20:
    temp_str = "조금 쌀쌀합니다."
elif temp_num <= 28:
    temp_str = "따뜻합니다."
elif temp_num <= 32:
    temp_str = "덥습니다."
elif temp_num > 32:
    temp_str = "매우 덥습니다."

temp_type = "섭씨"
def info():
    print('현재 위치는 {}입니다.'.format(location))
    print('온도는 {} {}도이며 {}'.format(temp_type, temp_num, temp_str))
    print('미세먼지 농도는 {}이며 {}'.format(dust, dust_str))
    print('초미세먼지 농도는 {}이며 {}'.format(minidust, minidust_str))
    print('오존 수치는 {}'.format(ozone))


while True:
    try:
        value = int(input('원하시는 서비스 항목을 선택해주세요.'))
        break
    except ValueError:
        print("숫자만 입력해주세요.")



'''
num으로 처리된 항목들
1. 최저기온
2. 최고기온
3. 시간당 강수량
4. 미세먼지
5. 초미세먼지
6. 오존지수
html 파일에서 <dd> 로 처리된 변수의 첫 번째를 출력해보니
arr[0] : 미세먼지
arr[1] : 초미세먼지
arr[2] : 오존지수
이렇게 출력됨을 확인하였다.
'''



