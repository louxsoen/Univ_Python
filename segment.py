import turtle as t

s7seg_base = "7s10.gif"  # reset이미지
s7seg_led = ["7s-a.gif", "7s-b.gif", "7s-c.gif", "7s-d.gif", "7s-e.gif", "7s-f.gif", "7s-g.gif"]
s7seg_num = [[1, 1, 1, 1, 1, 1, 0],  # 0
             [0, 1, 1, 0, 0, 0, 0],  # 1
             [1, 1, 0, 1, 1, 0, 1],  # 2
             [1, 1, 1, 1, 0, 0, 1],  # 3
             [0, 1, 1, 0, 0, 1, 1],  # 4
             [1, 0, 1, 1, 0, 1, 1],  # 5
             [1, 0, 1, 1, 1, 1, 1],  # 6
             [1, 1, 1, 0, 0, 0, 0],  # 7
             [1, 1, 1, 1, 1, 1, 1],  # 8
             [1, 1, 1, 1, 0, 1, 1]]  # 9

def disp_num(k):
    if k == 10:  # k가 10이면 reset이미지로
        t.stamp()
        t.shape(s7seg_base) # s7segbase로 모양 설정
    else:
        t.clearstamps()  # 스탬프 클리어해주기
        for i in range(7): # 7번 반복
            if s7seg_num[k][i] == 1:  # 1인 경우 해당 위치에 led 온
                t.shape(s7seg_led[i])
                t.stamp()

def key_0():  # 0일 때
    disp_num(0)

def key_1():  # 1일 떄
    disp_num(1)

def key_2(): # 2일 때
    disp_num(2)

def key_3(): # 3일 때
    disp_num(3)

def key_4():
    disp_num(4)

def key_5():
    disp_num(5)

def key_6():
    disp_num(6)

def key_7():
    disp_num(7)

def key_8():
    disp_num(8)

def key_9():
    disp_num(9)

def key_10():
    t.clearstamps()
    disp_num(10)

t.setup(400, 400)  # 화면 크기 400 x 400으로 설정
s = t.Screen()  # 스크린을 생성
t.hideturtle()  # turtle 숨기기
t.speed(0)  # 속도 빠르게
for i in range(7):  # 7번 반복
    s.addshape(s7seg_led[i]) # 이미지 추가

s.addshape(s7seg_base)  # reset 이미지가 추가되면 초기화면으로
t.shape(s7seg_base)
t.stamp() # 스탬프 클리어

s.onkey(key_0, "0")  # 입력 받는 키
s.onkey(key_1, "1")
s.onkey(key_2, "2")
s.onkey(key_3, "3")
s.onkey(key_4, "4")
s.onkey(key_5, "5")
s.onkey(key_6, "6")
s.onkey(key_7, "7")
s.onkey(key_8, "8")
s.onkey(key_9, "9")
s.onkey(key_10, "r")
s.listen()  # 키 입력받게 하는 함수

t.exitonclick()