# -*- coding: utf-8 -*-


import tkinter

win = tkinter.Tk()

win.title("zhang jian is a good man")
#  设置大小和位置 前面大小 后面坐标
win.geometry("800x800+200+200")

int1 = tkinter.IntVar()
str1 = tkinter.StringVar()
radio1 = tkinter.Radiobutton(win, text="one", value=0, variable=int1, command=lambda:print(int1.get()))
radio2 = tkinter.Radiobutton(win, text="two", value=1, variable=int1, command=lambda:print(int1.get()))
radio3 = tkinter.Radiobutton(win, text="one", value="1", variable=str1, command=lambda:print(str1.get()))
radio4 = tkinter.Radiobutton(win, text="two", value="2", variable=str1, command=lambda:print(str1.get()))
radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()
win.mainloop()