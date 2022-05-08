import turtle

'''20190308062 염중화'''

## 변수 선언 부분 ##

i,k,tX,tY = [0]*4
swidth,sheight = 700,320
gugudan=""
gu=turtle

## 메인 코드 부분 ##

gu.title('거북이 구구단')
gu.shape('turtle')
gu.setup(width = swidth +50, height= sheight + 50)
gu.screensize(swidth,sheight)
gu.penup()
tX, tY = -475,200
gu.goto(tX,tY)

for i in range(2,10):
    for k in range(1,10):
        gu.goto(tX+80*i,tY - 40*k)
        gugudan=str(i)+'x'+str(k)+'='+str(k*i)
        gu.write(gugudan,font = ('Arial',12,'bold'))
gu.goto(320,-150)
gu.done()
