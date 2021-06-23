'''
now = input("날짜를 입력하시오. ex : \'2021-06-09\' ")
this_year = int(now[0:4])
past_year = this_year - 1
print("1년전 날짜 : ", str(past_year) + now[4:])
'''

num = input("전화번호를 입력하세요. ex : \'010-1234-4321\' ")
mid = num[4:8]
lst = int(num[9:])

print("당신의 전화번호 중간 자리는 %s, 마지막 자리는 %s" %(mid, lst))
print("전화번호 이웃은 010-%s-%s, 010-%s-%s 입니다." %(mid, lst-1, mid, lst+1))