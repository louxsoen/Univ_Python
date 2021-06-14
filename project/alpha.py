import requests
import re as cut
import os
import time
import math
from bs4 import BeautifulSoup as bus

'''
웹 크롤링을 위해 BeautifulSoup를 사용했습니다.
BeautifulSoup를 사용한 이유
.text 확장자를 이용해서 텍스트 형태의 html 요소에 접근해야함.
html요소에 접근이 쉬운 BeautifulSoup 채택

BeautifulSoup 미적용 오류가 난다면
터미널에 pip install beautifulsoup4 입력

만약 pip가 없다면?
# 윈도우 버전 pip 설치법
1. Open CMD
2. curl https://bootstrap.pypa.io/get-pip.py-o get-pip.y
3. python get-pip.py

# 리눅스 버전 pip 설치법
sudo apt-get install python-pip (파이썬 2.x 버전)
sudo apt-get install python3-pip (파이썬 3.x 버전)

# 맥 버전 pip 설치법
sudo easy_install pip

참고해주세요.

코딩 환경
macOS Big Sur 11.4
Macbook Pro (16-Inch, 2019)
2.3 Ghz 8 Core Intel Core i9
16GB 2667 MHz DDR4
'''


#---------------------------------------------------------------# 날씨 정보 가져오기 (크롤링)

html = requests.get('https://search.naver.com/search.naver?query=날씨') # 네이버 날씨 HTML주소

box_weather = bus(html.text, 'html.parser') # 날씨 박스
css_weather = box_weather.find('div', {'class': 'weather_box'}) # css 코드 날씨 박스

location = css_weather.find('span', {'class':'btn_select'}).text # 위치!!!
temp = css_weather.find('span', {'class':'todaytemp'}).text # 온도

arr = css_weather.findAll('dd') # CSS 문법중 <div> alert </div> 이후 dd 구문 검색
dust = arr[0].find('span', {'class':'num'}).text # 미세먼지
minidust = arr[1].find('span', {'class':'num'}).text 
ozone = arr[2].find('span', {'class':'num'}).text


#---------------------------------------------------------------# 날씨 정보 단위 제거 및 자료형 스카우트

dust_list = cut.findall("\d+", dust) # 단위까지 붙은 미세먼지 변수에서 숫자만 출력
minidust_list = cut.findall("\d+", minidust) # 초미세먼지 단위 제거

# 네이버 날씨에 정보가 없을 경우 프로그램 오류가 나는 것을 확인 재발 방지
try: 
    temp_num = int(temp) # temp가 문자 변수여서 int형으로 스카우트
except:
    print('온도 수치를 가져올 수 없습니다.')
    temp_num = "--"

try:
    dust_num = int(dust_list[0]) # 자료형 스카우트
except:
    print('미세먼지 수치를 가져올 수 없습니다.')
    dust_num = "정보 없음"

try:
    minidust_num = int(minidust_list[0]) # 자료형 스카우트
except:
    print('초미세먼지 수치를 가져올 수 없습니다.')
    minidust = "정보 없음"


#---------------------------------------------------------------# 시간 정보 가져오기 (크롤링)
def googletime():
    local_year = time.strftime('%Y')
    local_month = time.strftime('%m')
    local_day = time.strftime('%d')
    local_hour = time.strftime('%H')
    local_min = time.strftime('%M')
    local_sec = time.strftime('%S')

    print('컴퓨터 시간 | {}년 {}월 {}일 {}시 {}분 {}초'.format(local_year, local_month, local_day, local_hour, local_min, local_sec))

#---------------------------------------------------------------# weather str 설정

if dust_num <= 30: # 미세먼지 수치별 상태를 dust_str에 저장
    dust_str = "좋습니다."
elif dust_num <= 80:
    dust_str = "보통입니다."
elif dust_num <= 150:
    dust_str = "나쁩니다."
elif dust_num > 150:
    dust_str = "최악입니다."

if minidust_num <= 15: # 초미세먼지 수치별 상태를 minidust_str에 저장
    minidust_str = "좋습니다."
elif minidust_num <= 35:
    minidust_str = "보통입니다."
elif minidust_num <= 100:
    minidust_str = "나쁩니다."
elif minidust_num > 100:
    minidust_str = "최악입니다."

if temp_num < 0: # 온도에 따른 서준이의 개인적은 소견
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

temp_type = "섭씨" # 섭씨 화씨 구분 추가 예시
user_name = "이서준" # 프로그래머 이름
ex_name = user_name # ex_name 해시

#---------------------------------------------------------------# 날씨 정보 출력 (1)

def info():
    print("##### 오늘의 날씨 정보입니다. #####")
    print('{}님이 계시는 위치는 {}입니다.'.format(user_name, location))
    print('온도는 {} {}도이며 {}'.format(temp_type, temp_num, temp_str))
    print('미세먼지 농도는 {}이며 {}'.format(dust, dust_str))
    print('초미세먼지 농도는 {}이며 {}'.format(minidust, minidust_str))
    print('오존 수치는 {}입니다.'.format(ozone))

#---------------------------------------------------------------# 사칙 연산 계산기 (3)

def all():
    def count(str, a, b): # operater 마다 계산하는 라이브러리를 짜놓음 ###### 주의
        if str == '+':
            return a + b
        if str == '-':
            return a - b
        if str == '*':
            return a * b
        if str == '/':
            return a / b
        if str == '^':
            return a ** b

    def num_lib(val): # 값 선언 (리스트로 대치 예정) ############ 주의
        return val == '0' or val == '1' or val == '2' or val == '3' or val == '4' or val == '5' or val == '6' or val == '7' or val == '8' or val == '9'

    def num_test(val_str): # 값이 오지 않는 경우 패스하는 함수 CONST취급 할 것
        n = 0
        var = ''
        try: 
            while num_lib(val_str[n]):
                var  += val_str[n]
                n += 1
        except: pass # 여러번 수행 구간 건들지 말 것

        return (int(var), n)


    status = False
    cal_input = input('사칙 연산 계산기 | 식을 작성해주세요. \'ex : 51+34*5\' (띄어쓰면 안됩니다.)\n')

    while True:
        try: 
            if cal_input[0] == '-': # 음수 처리 함수 1
                status = True # string format 열어주기
                cal_input = cal_input[1:]

            a = num_test(cal_input)[0]

            if status == True: # 음수 처리 함수 2
                a = -a # 음수 출력 부분
                status = False
            a_end = num_test(cal_input)[1]
            cal_input = cal_input[a_end:]

            if cal_input == '': 
                break

            op = cal_input[0] # operation (부호) 확인하는 부분
            cal_input = cal_input[1:]

            b = num_test(cal_input)[0]
            b_end = num_test(cal_input)[1]

            result = count(op, a, b) # 결과값 출력 부분
            a = result 
            cal_input = str(a) + cal_input[b_end:]

            print(cal_input)

        except:                 # 잘못된 값 차단
            print('잘못된 값을 적어 메인화면으로 돌아갑니다.')
            break

#---------------------------------------------------------------# GCD계산기 (4)
def divisor(): # GCD 계산 및 DIVISOR 확인

    print('GCD계산기 | GCD(Grestest Common Divisor)는 두 수의 최대공약수를 지칭합니다.')

    while True:
        try:
            a = int(input('정수 a를 입력하시오. : '))
            if(a == 0):
                print('0을 입력하셨으므로 프로그램을 종료합니다.')
                break
           
            b = int(input('정수 b를 입력하시오. : '))  
            if(b == 0):
                print('0을 입력하셨으므로 프로그램을 종료합니다.')
                break
            
        except ValueError:
            print('잘못된 값을 입력하셨습니다.')
            break
        
        if (a == 0) | (b == 0):
            print('GCD 프로그램을 종료합니다.')
            break

        a, b = b, a # 두 수 스위치

        c = math.gcd(a, b) # c는 GCD 결과값
        div_a = []
        div_b = []
        
        print('Gcd({}, {}) = {}'.format(a, b, c))

        for i in range(1, a+1): # a 약수 추가
            if a % i == 0:
                div_a.append(i)
        
        for i in range(1, b+1): # b 약수 추가
            if b % i == 0:
                div_b.append(i)

        print('{}의 약수 {}'.format(a, div_a))
        print('{}의 약수 {}'.format(b, div_b))
        print('종료하려면 0을 입력하십시오.')

#---------------------------------------------------------------# 콘솔 클린하게 해주는 함수

def cls(): # 화면 클리너 해주는 함수
    console_clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') # 윈도우에선 cls, 맥에서는 clear
    console_clear()

#---------------------------------------------------------------# 메인함수 (-1)

while True:
    while True:
        try:
            value = int(input('\n메인화면 | 원하시는 서비스 항목을 선택해주세요.\n1 ) 날씨 정보 확인하기 \n2 ) 현재 시간 확인하기\n3 ) 사칙연산 계산기\n4 ) GCD 계산기\n5 ) 사용자 이름 변경 \n0 ) 종료\n'))
            break
        except ValueError:
            cls()
            print("입력 오류 | 숫자만 입력해주세요.")

    if value == 0: # 종료 
        cls()
        print('S- OS를 종료합니다. 감사합니다.')
        break
    elif value == 1: # 날씨 정보
        cls()
        info()
    elif value == 2: #시간 정보
        cls()
        googletime()

    elif value == 3: # 사칙 연산 계산기
        cls()
        all()
        
    elif value == 4: # gcd 계산기 연산
        cls()
        divisor()
    elif value == 5: # 사용자 이름 변경
        cls()
        user_name = input("새로운 사용자의 이름을 입력하시오. (현재 사용자 : {})\n".format(user_name))
        print('사용자 이름이 {}님에서 {}님으로 변경되었습니다.'.format(ex_name, user_name))
        ex_name = user_name
        
    

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
