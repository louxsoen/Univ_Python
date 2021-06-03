n = int(input("학생 수를 입력하시오 : "))

dB = []
i = 0
while(i < n):
    name = str(input("이름 | "))
    num = str(input("학번 | "))
    dept = str(input("학과 | "))
    phone = str(input("전번 | "))
    addr = {'이름' : name, '학번' : num, '학과' : dept, '전화번호' : phone}
    dB.append(addr)
    i += 1

print(dB)
