import random

op = ["+","-","*","//"] # 더하기, 빼기, 곱셈, 나누기 연산자를 저장하는 op 리스트형
check = int(0) # 얼마나 반복했는지 세어주는 변수 (0부터 시작)
point = int(0) # 점수를 세어주는 변수 (0부터 시작)

while check < 10: # check 변수가 10보다 커질 때까지 아래 구문을 반복
    num_1 = random.randint(1, 99) # num_1은 1~100 사이 랜덤 숫자를 지정할 변수
    num_2 = random.randint(1, 99) # num_2은 1~100 사이 랜덤 숫자를 지정할 변수
    op_num = random.randint(0,3) # op_num은 0~3 사이 랜덤 숫자를 배정받고

    print(str(num_1), str(op[op_num]), str(num_2)) # string 값으로 num_1 (수식) num_2 값 (랜덤 문제 출력)
    answer = int(input()) # answer은 위 식을 보고 입력하는 수를 받는 변수

    # 문제를 맞추는 경우
    if answer == num_1 + num_2 or answer == num_1 - num_2 or answer == num_1 // num_2 or answer == num_1 * num_2:
        point += 10 # 10점을 준다.
        check += 1 # check에 1을 더한다
        print('정답입니다! 10점을 부여할게요!\n현재 점수 :', point, '점', '| 진행률 :', check*10, '%')
        continue # 구문의 처음으로 돌아간다.
    else: # 문제를 맞추지 못 하는 경우
        check += 1 # check에 1을 더한다.
        print('땡.. 아쉽지만 오답입니다.\n현재 점수 :', point, '점', '| 진행률 :', check*10, '%')
        continue # 구문의 처음으로 돌아간ㄷ.

if point >= 70: # 만약 점수가 70점 이상일 경우
    print('축하합니다! 합격입니다.') # 합격 메시지
else: # 그러지 못 할 경우
    print('아쉽지만 불합격입니다.') # 불합격 메시지
