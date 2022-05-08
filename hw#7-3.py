'''2019038062 염중화'''

from tkinter import*
from tkinter.ttk import*


## 메인코드 부분 ##
window=Tk()

notebook=Notebook(window,width=500,height=500)
notebook.pack()

tab1=Frame(window)
notebook.add(tab1,text="고양이")

tab2=Frame(window)
notebook.add(tab2,text="강아지")

photo1=PhotoImage(file="animal/cat.gif")
photo2=PhotoImage(file="animal/dog.gif")

label1=Label(tab1,image=photo1)
label1.pack()

label2=Label(tab2,image=photo2)
label2.pack()

window.mainloop()
