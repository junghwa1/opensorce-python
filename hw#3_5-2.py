import random
import turtle
import math

'''2019038062 염중화'''

## 변수 선언 부분 ##

bt, gt, rt=[None]*3
btX, btY, gtX, gtY, rtX, rtY = [0] * 6
swidth, sheight = 300, 300

## 메인 코드 부분 ##

turtle.title('거북이 만나기')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)

bt=turtle.Turtle('turtle'); bt.color('blue'); bt.penup()
gt=turtle.Turtle('turtle'); gt.color('green'); gt.penup()
rt=turtle.Turtle('turtle'); rt.color('red'); rt.penup()

bt.goto(-100,-100); gt.goto(0,0);rt.goto(100,100)

while True:
    angle=random.randrange(0,360)
    dist=random.randrange(1,50)
    bt.left(angle); bt.forward(dist)
    angle=random.randrange(0,360)
    dist=random.randrange(1,50)
    gt.left(angle); gt.forward(dist)
    angle=random.randrange(0,360)
    dist=random.randrange(1,50)
    rt.left(angle); rt.forward(dist)

    btX=bt.xcor(); btY=bt.ycor()
    gtX=gt.xcor(); gtY=gt.ycor()
    rtX=rt.xcor(); rtY=rt.ycor()

    if ((-swidth/2<=btX and btX<= swidth/2) and (-sheight/2 <= btY and btY <= sheight/2)) :
        pass
    else :
        bt.goto(0,0)
    if ((-swidth/2<=gtX and gtX<= swidth/2) and (-sheight/2 <= gtY and gtY <= sheight/2)) :
        pass
    else :
        gt.goto(0,0)
    if ((-swidth/2<=rtX and rtX<= swidth/2) and (-sheight/2 <= rtY and rtY <= sheight/2)) :
        pass
    else :
        rt.goto(0,0)
    
    if math.sqrt(((btX-gtX)*(btX-gtX))+((btY-gtY)*(btY-gtY))) <= 20 or \
       math.sqrt(((btX-rtX)*(btX-rtX))+((btY-rtY)*(btY-rtY))) <= 20 or \
       math.sqrt(((rtX-gtX)*(rtX-gtX))+((rtY-gtY)*(rtY-gtY))) <= 20 :
       bt.turtlesize(3); gt.turtlesize(3); rt.turtlesize(3)
       break

turtle.done()
