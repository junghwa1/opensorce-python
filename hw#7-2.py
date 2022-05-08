from tkinter import*
from tkinter.colorchooser import*
from tkinter.simpledialog import*

'''2019038062 염중화'''

## 함수 선언 부분 ##

def click(event):
    global x1 
    x1=event.x
    global y1
    y1=event.y
    
def release(event):
    x2,y2=(event.x),(event.y)
    canvas.create_line(x1,y1,x2,y2,width=penWidth, fill= penColor)

def selrect_color():
    global penColor
    color=askcolor()
    penColor=color[1]

def selrect_penWidth():
    global penWidth
    penWidth=askinteger("선 두께","선 두께(1~10)를 입력하세요",
                        minvalue=1,maxvalue=10)
    
## 변수 선언 부분 ##

penColor="black"
penWidth=5
window=Tk()

## 메인 코드 부분 ##

canvas=Canvas(window)
canvas.pack()
mainMenu=Menu(window)
window.title("그림판 프로그램")
window.config(menu=mainMenu)

drawMenu=Menu(mainMenu)
mainMenu.add_cascade(label="설정",menu=drawMenu)
drawMenu.add_command(label="선 색상 선택",command=selrect_color)
drawMenu.add_separator()
drawMenu.add_command(label="선 두께 설정",command=selrect_penWidth)

canvas.bind("<Button-1>",click)
canvas.bind("<ButtonRelease-1>",release)

window.mainloop()
