import requests
import re as cut
import os
import math
from bs4 import BeautifulSoup as bs


#---------------------------------------------------------------# 날씨 정보 가져오기 (크롤링)

html = requests.get('https://search.naver.com/search.naver?query=날씨') # 정보를 가져올 HTML주소

box_weather = bs(html.text, 'html.parser') 
css_weather = box_weather.find('div', {'class': 'weather_box'})

location = css_weather.find('span', {'class':'btn_select'}).text
temp = css_weather.find('span', {'class':'todaytemp'}).text

arr = css_weather.findAll('dd') 
dust = arr[0].find('span', {'class':'num'}).text
minidust = arr[1].find('span', {'class':'num'}).text
ozone = arr[2].find('span', {'class':'num'}).text

dust_list = cut.findall("\d+", dust)
dust_num = int(dust_list[0])

minidust_list = cut.findall("\d+", minidust)
minidust_num = int(minidust_list[0])

ozon_list = cut.findall("\d+", ozone)
ozon_num = float(ozon_list[0])

#---------------------------------------------------------------# 시간 정보 가져오기 (크롤링)
'''
html = requests.get('https://www.google.com/search?q=현재+시간')

box_time = bs(html.text, 'html.parser')
css_time = box_time.find('div', {'class': 'weather_box'})

location = css_time.find('span', {'class':'btn_select'}).text

arr = css_time.findAll('dd') 
dust = arr[0].find('span', {'class':'num'}).text
minidust = arr[1].find('span', {'class':'num'}).text
ozone = arr[2].find('span', {'class':'num'}).text

dust_list = cut.findall("\d+", dust)
dust_num = int(dust_list[0])

minidust_list = cut.findall("\d+", minidust)
minidust_num = int(minidust_list[0])

ozon_list = cut.findall("\d+", ozone)
ozon_num = float(ozon_list[0])
'''

#---------------------------------------------------------------# weather str 설정

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

#---------------------------------------------------------------# 기초 세팅

temp_type = "섭씨" # 섭씨 화씨 구분 추가 예
user_name = "이서준"
ex_name = user_name

#---------------------------------------------------------------# 날씨 정보 (1)
def info():
    print("오늘의 날씨 정보입니다.")
    print('{}님이 계시는 위치는 {}입니다.'.format(user_name, location))
    print('온도는 {} {}도이며 {}'.format(temp_type, temp_num, temp_str))
    print('미세먼지 농도는 {}이며 {}'.format(dust, dust_str))
    print('초미세먼지 농도는 {}이며 {}'.format(minidust, minidust_str))
    print('오존 수치는 {}'.format(ozone))

#---------------------------------------------------------------# 사칙 연산 계산기 (3)


#---------------------------------------------------------------# GCD계산기 (4)
def divisor(a, b):
    print('GCD계산기 | GCD(Grestest Common Divisor은 두 수의 최대공약수를 지칭합니다.')

    a, b = b, a # swtich

    c = math.gcd(a, b)
    div_a = []
    div_b = []
    
    print('Gcd({}, {}) = {}'.format(a, b, c))

    for i in range(1, a):
        if a % i == 0:
            div_a.append(i)
    
    for i in range(1, b):
        if b % i == 0:
            div_b.append(i)

    print('{}의 약수 {}'.format(a, div_a))
    print('{}의 약수 {}'.format(b, div_b))

#---------------------------------------------------------------# 메인함수 (-1)
def cls():
    console_clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    console_clear()

while True:
    while True:
        try:
            value = int(input('\n메인화면 | 원하시는 서비스 항목을 선택해주세요.\n1 ) 날씨 정보 확인하기 \n2 ) 현재 시간 확인하기\n3 ) 사칙연산 계산기\n4 ) GCD 계산기\n5 ) 사용자 이름 변경 \n0 ) 종료\n'))
            break
        except ValueError:
            cls()
            print("입력 오류 | 숫자만 입력해주세요.")

    if value == 0:
        cls()
        print('S- OS를 종료합니다. 감사합니다.')
        break
    elif value == 1:
        cls()
        info()
    elif value == 3:
        cls()
        cal_input = input('사칙 연산 계산기 | 식을 작성해주세요. \'ex : 51 + 34\'')
        
    elif value == 4:
        cls()
        a = int(input('정수 a를 입력하시오. : '))
        b = int(input('정수 b를 입력하시오. : '))
        divisor(a, b)
    elif value == 5:
        cls()
        user_name = input("새로운 사용자의 이름을 입력하시오. (현재 사용자 : {})\n".format(user_name))
        print('사용자 이름이 {}님에서 {}님으로 변경되었습니다.'.format(ex_name, user_name))
        
    

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
