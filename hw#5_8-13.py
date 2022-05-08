import turtle
import random
import math
from tkinter.simpledialog import *

'''2019038062 염중화'''

## 변수 선언 부분 ##

turtle.setup(width = 500, height = 500)

inStr = ""
tX, tY, txtSize, i= 0,0,20,1
dist=200

## 메인 코드 부분 ##

turtle.title("나선형 글자 출력")
turtle.shape("turtle")

inStr = askstring("문자열 입력", "거북이 쓸 문자열을 입력")
turtle.penup()
degr=720/(len(inStr))

for ch in inStr:
    
    radi=(3.14)*(degr/180)*i
    tX = math.cos(radi)*dist
    tY = math.sin(radi)*dist
    r = random.random(); g = random.random(); b = random.random()

    turtle.goto(tX,tY)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font=("맑은고딕", txtSize, "bold"))

    dist-=(200/len(inStr))
    i+=1
    
turtle.done()
