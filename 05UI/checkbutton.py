# -*- coding: utf-8 -*-


import tkinter

win = tkinter.Tk()

win.title("zhang jian is a good man")

#  设置大小和位置 前面大小 后面坐标
win.geometry("800x800+200+200")

hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()

checkbutton1 = tkinter.Checkbutton(win, text="zhang", variable=hobby1, command=lambda:print("zhang"))
checkbutton2 = tkinter.Checkbutton(win, text="jian", variable=hobby2, command=lambda:print("jian"))

checkbutton1.pack()
checkbutton2.pack()


win.mainloop()