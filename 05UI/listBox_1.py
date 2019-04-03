# -*- coding: utf-8 -*-


import tkinter

win = tkinter.Tk()

win.title("zhang jian is a good man")

#  设置大小和位置 前面大小 后面坐标
win.geometry("800x800+200+200")

str1 = tkinter.StringVar()

listbox = tkinter.Listbox(win, selectmode=tkinter.SINGLE, 
                            listvariable=str1)  # 不支持鼠标按下后选中
listbox.pack()

listbox.insert(tkinter.END, "111")
listbox.insert(tkinter.END, "222")
listbox.insert(tkinter.END, "333")
listbox.insert(tkinter.END, "444")
listbox.insert(tkinter.END, "555")
listbox.insert(tkinter.ACTIVE, "000")

# 获取列表中的所有值
print("******************************", str1.get())

str1.set(("1", "2", "3"))

def click(event):
    print(listbox.get(listbox.curselection()))

listbox.bind("<Double-Button-1>", click)

win.mainloop()