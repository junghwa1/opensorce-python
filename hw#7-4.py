from tkinter import*
from tkinter.filedialog import*

'''2019038062 염중화'''

## 함수 선언 부분 ##

def func_open():
    global filename
    filename=askopenfilename(parent=window,filetypes=(("GIF 파일", "*.gif"),
              ("모든 파일","*.*")))
    photo=PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image=photo

def func_exit():
    window.quit()
    window.destroy()

def zoomphoto(event):
    global zvalue
    global svalue
    if svalue == 0:
        zvalue+=2
    else:
        svalue=0
        zvalue=2
    photo=PhotoImage(file=filename)
    photo=photo.zoom(zvalue,zvalue)
    pLabel.configure(image=photo)
    pLabel.image=photo
    

    
def subphoto(event):
    global zvalue
    global svalue
    if zvalue == 0:
        svalue+=2
    else:
        zvalue=0
        svalue=2
    photo=PhotoImage(file=filename)
    photo=photo.subsample(svalue,svalue)
    pLabel.configure(image=photo)
    pLabel.image=photo

## 변수 선언 부분 ##

global zvalue
global svalue
zvalue=0
svalue=0

## 메인 코드 부분 ##

window=Tk()
window.geometry("400x400")
window.title("사진 확대 축소")

photo=PhotoImage()
pLabel=Label(window,image=photo)
pLabel.pack(expand=1,anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.bind("<Up>",zoomphoto)
window.bind("<Down>",subphoto)



window.mainloop()
