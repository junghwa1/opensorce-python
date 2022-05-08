import turtle
import random



def screenLeftClick(x,y):
    global r, g, b
    mt.pencolor((r, g, b))
    mt.pendown()
    mt.goto(x,y)

def screenRightClick(x,y):
    mt.penup()
    mt.goto(x,y)

def screenMidClick(x,y):
    global r, g, b
    mtSize=random.randrange(1,10)
    mt.shapesize(mtSize)
    r=random.random()
    g=random.random()
    b=random.random()



penSize,mtSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

mt=None
mt=turtle
mt.speed(0.000001)

mt.title('거북이로 그림 그리기')
mt.shape('turtle')
mt.pensize(penSize)

mt.onscreenclick(screenLeftClick,1)
mt.onscreenclick(screenMidClick,2)
mt.onscreenclick(screenRightClick,3)


mt.done()
