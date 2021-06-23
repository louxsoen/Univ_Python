last_usage = int(input('전 달 전력량 : '))  # 전 달 전력랑을 입력 받습니다.
usage = int(input('이번 달 전력량 : '))  # 이번 달 전력량을 입력 받습니다.

total_usage = last_usage - usage  # 이번 달 전력 사용량 = 전 달 - 이번 달 전력량
print('이번 달 전력 사용량 =', total_usage)  # 이번 달 전력 사용량 출력

if total_usage <= 200:  # 전력 사용량이 200 이하일 경우
    cost = 93.3 * total_usage + 910  # 기본 요금 910원에 1kWh당 93.3원
elif 201 <= total_usage <= 400:  # 전력 사용량이 201~400 사이일 경우
    cost = 187.9 * total_usage + 1600  # 기본 요금 1600원에 1kWh당 187.9원
else:  # 위의 조건을 충족시키지 못 할 때 ( 400kWh 초과 )
    cost = 280.6 * total_usage + 7300  # 기본 요금 7300원에 1kWh당 280.6원

print('전기요금 =', cost)  # cost를 출력
