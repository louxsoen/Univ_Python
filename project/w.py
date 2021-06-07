import requests
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


print('현재 위치는 {}입니다'.format(location))
print('온도는 {}도 라서 ~합니다.'.format(temp))
print(dust)
print(minidust)
print(ozone)