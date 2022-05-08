import turtle
import random

'''2019038062 염중화'''

## 함수 선언 부분 ##

def screenRightClick(x,y):
    global r, g, b
    r=random.random()
    g=random.random()
    b=random.random()
    mt.color((r ,g ,b))
    mt.pencolor((r, g, b))
    mt.pendown()
    mt.goto(x,y)
    mtSize=random.randrange(1,10)
    mt.shapesize(mtSize)
    C=random.randrange(0,360)
    mt.right(C)
    mt.stamp()

## 변수 선언 부분 ##

penSize,mtSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

mt=turtle

## 메인 코드 부분 ##

mt.title('거북이 도장')
mt.shape('turtle')
mt.pensize(penSize)

mt.onscreenclick(screenRightClick,3)

mt.done()
