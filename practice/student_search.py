name = str('a')
phone = str('b')
info = {'이름' : name, '전화번호' : phone}
dB = []

i = 0
while(i != 3):
    i = int(input("1) 친구 등록, 2) 검색, 3) 종료 | 입력 : "))
    if(i == 1):
        print("| 친구 등록하기 |")
        name = str(input("이름 : "))
        phone = str(input("전화번호 : "))
        info = {'이름' : name, '전화번호' : phone}
        dB.append(info)
    if(i == 2):
        print("| 친구 검색하기 |")
        search_name = str(input("이름 : "))
        info.get('전화번호')
    if(i == 3):
        print("| 시스템을 종료합니다. |")
    print(dB)
    print(info)

