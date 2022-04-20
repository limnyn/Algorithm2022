# 터틀 그래픽을 이용하여 사각형 3개를 그려보자. 단 조건은 사각형은 20도씩 기울어
# 져 있다.
import turtle

t = turtle.Pen()

for i in range(10):
    t.left(20)   # 왼쪽으로 20도 회전
    # 아래는 사각형을 만드는 코드이다.
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

turtle.exitonclick()

