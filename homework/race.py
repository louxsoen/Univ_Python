import turtle
import random

screen = turtle.Screen()
img1 = "/Users/louxsoen/Documents/rabbit.gif"
img2 = "/Users/louxsoen/Documents/turtle.gif"
screen.addshape(img1)
screen.addshape(img2)

t = turtle.Turtle() # 거북이
r = turtle.Turtle() # 토끼
line = turtle.Turtle() # 라인, 결승선, 출발선

# 결승선 그리는 함수
line.penup()
line.goto(400, -50) # 끝 가운데점
line.pendown()
line.pensize(20)
line.color("mediumpurple")
line.goto(400, -250)
line.goto(400, 100)

# 라인과 출발선 그리는 함수
line.penup()
line.color("gray")
line.pensize(5)
line.goto(388, -50)
line.pendown()
line.goto(-330, -50)
line.goto(-330, 100)
line.goto(-330, -250)
line.penup()


# 토끼와 거북이 출발선 배치
t.penup()
r.penup()

# 둘 라인 색 설정
t.color("magenta")
r.color("firebrick")

# 출발선 배치
t.goto(-400, -150)
r.goto(-400, 50)

t.pendown()
r.pendown()
t.shape(img1) # 이미지 불러오기
r.shape(img2) # 이미지 불러오기


# 경주 난수만큼 이동하기
for i in range(50):
    m1 = random.randint(1, 50)
    r.fd(m1)
    m2 = random.randint(1, 50)
    t.fd(m2)


# 파이참에서는 이 함수가 없으면 화면 유지가 안 돼요.
turtle.exitonclick()
