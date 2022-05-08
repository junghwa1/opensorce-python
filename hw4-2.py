import turtle

'''2019038062 염중화'''

## 변수 선언 부분 ##
tX,tY = 300,0
num=0
bnum=0

## 함수 선언 부분 ##

def stampturtle(n,b, tX, tY):

    for i in range(len(b) - 2) :
        turtle.goto(tX, tY)
        if n & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        
        turtle.stamp()
        tX -= 35
        n >>= 1

## 메인 코드 부분 ##

num=int(input("숫자를 입력하세요: "))
bnum=bin(num)

turtle.shape('turtle')
turtle.left(90)
turtle.penup()

stampturtle(num,bnum, tX, tY)

turtle.done()
