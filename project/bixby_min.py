import random#random 모듈을 들고옵니다.
player=[]#player의 빙고판
computer=[]#computer의 빙고판
turn=1#차례
player_check=0#player의 빙고개수
computer_check=0#computer의 빙고개수

def show():#현재 빙고판의상태를 출력하는 함수
    print("\n\nplayer broad:")
    for i in range(25):
        if player[i]==0:#빙고 체크된판이 0일때 체크된걸로 표시
            print("%2s "%('X'),end="")
        else:# 체크된게 아닐때는 빙고판 숫자 표시
            print("%2d "%(player[i]),end="")
        if i%5==4:#5개 출력하고 줄바꿈
            print()
            
    print("\n\nseojun broad:")
    for i in range(25):#이밑은 위코드 기능과 동일
        if computer[i]==0:
            print("%2s "%('X'),end="")
        else:
            print("%2d "%(computer[i]),end="")
        if i%5==4:
            print()

def check(list):
    temp=0#해당줄의 체크개수
    bingo=0#빙고개수
    for i in range(25):
        if list[i]==0:#체크이면 체크수를 1증가
            temp+=1
        if temp==5:#1줄에 체크가 5개면 빙고개수 증가
            bingo+=1
        if i%5==4:#줄마다 체크개수 초기화
            temp=0
    for i in range(5):#세로줄마다 체크숫자 저장하기
        for p in range(5):
            if list[i+p*5]==0:#체크이면 체크수를 1증가
                temp+=1
        if temp==5:#1줄에 체크가 5개면 빙고개수 증가
            bingo+=1
        temp=0
    return bingo#빙고 개수 반환

def AI(list):
    temp=0#체크된것의 개수
    garo=[]#가로줄에서 체크된숫자를 저장
    sero=[]#세로줄마다 체크된 숫자를 저장
    priority=[]#우선순위
    result=0#최대 우선순위
    for i in range(25):#가로줄마다 체크숫자 저장하기
        if list[i]==0:#체크이면 체크수를 1증가
            temp+=1
        if i%5==4:#줄마다 체크개수 초기화
            garo.append(temp)
            temp=0
    temp=0
    for i in range(5):#세로줄마다 체크숫자 저장하기
        for p in range(5):
            if list[i+p*5]==0:#체크이면 체크수를 1증가
                temp+=1
        sero.append(temp)
        temp=0
    for i in range(25):#우선순위를 0으로 초기화
        priority.append(0)
        
    for i in range(5):#가로에 대한 우선순위
        for p in range(5):
            if computer[p+i*5] !=0:
                priority[p+i*5]+=garo[i]

    for i in range(5):#세로에 대한 우선순위
        for p in range(5):
            if computer[i+p*5]!=0:
                priority[i+p*5]+=sero[i]

    for i in range(25):
        if result<=priority[i]:
            result=i
    return result
    
    
    
for i in range(25):#player의 빙고판에 숫자를 채워넣는다.
    a=random.randint(1,25)#랜덤값으로 채워 넣는다.
    while a in player:#중복된값이 있으면 중복이 없을때까지 다시 뽑는다.
        a=random.randint(1,25)
    player.append(a)#빙고판 list에 추가
    
for i in range(25):#computer의 빙고판에 숫자를 채워넣는다.
    a=random.randint(1,25)#랜덤값으로 채워 넣는다.
    while a in computer:#중복된값이 있으면 중복이 없을때까지 다시 뽑는다.
        a=random.randint(1,25)
    computer.append(a)#빙고판 list에 추가

while 1:
    show()#현재 빙고판의 상태를 보여준다.
    if turn%2==1:#turn이 홀수일때는 player의 턴이다.
        print("\n플레이의 턴입니다.")
        while 1:
            while 1:
                try:#숫자만 입력하도록 하였다.
                    a=int(input("정수만 입력해주세요. :"))
                except ValueError :#만약 숫자를 입력한것이 아니라면 예외처리로 처리하도록하엿다
                    print("\n잘못된 입력입니다.")
                
                if  25>=a>=1 and a in player:#숫자라도 중복이나 잘못입력한숫자에 대해서 처리하도록 짰다.
                    break
                else:
                    print('\n중복된 숫자이거나 잘못입력하셨습니다.')
            if a in player:
                player[player.index(a)]=0
                computer[computer.index(a)]=0
                break
    else:
        print("\n빅스비의 턴입니다.")
        print("빅스비: %d"%( computer[AI(computer)]))
        player[player.index(computer[AI(computer)])]=0
        computer[AI(computer)]=0
    print("턴종료")
    if   check(player)>=5 and check(computer)>=5:
        print("무승부")
        break
    elif check(player)>=5:
        print("player win~~~~~~~~~~~~~~")
        break
    elif check(computer)>=5:
        print("computer win~~~~~~~~~~~~~~")
        break
    print('================================')
    turn+=1

from multiprocessing import Queue