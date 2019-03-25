import tkinter

win = tkinter.Tk()

win.title("zhang jian is a good man")

#  设置大小和位置 前面大小 后面坐标
win.geometry("800x800+200+200")

# lable
#                           文本                            背景颜色     字体颜色
lable = tkinter.Label(win, text="zhang jian is a good man", bg="pink", 
                                fg="blue",
                                font =("宋体",20),
                                width = 10,
                                height = 10,
                                wraplength = 40, # 多宽后换行
                                justify = "left", #左对齐
                                anchor = "center"
                                )
lable.pack()


def click():
    print("hello world")


button = tkinter.Button(win, text="按钮", command=click)
button.pack()
#匿名函数
button2 = tkinter.Button(win, text="按钮2", command=lambda:print("zhang jian is a good man"))
button2.pack()
button1 = tkinter.Button(win, text="quit", command=win.quit)
button1.pack()

'''
输入控件：
'''
# 绑定变量
e = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=e)
e.set("zhang jian ")
entry.pack()
#获取输入窗的内容
e.get()
entry.get()

button3 = tkinter.Button(win, text="按钮3", command=lambda : print(e.get()))
button3.pack()

# 暗文输入
entry = tkinter.Entry(win, show="*")
entry.pack()

# 文本控件
# height 表示显示四行

# 滚动条

scroll = tkinter.Scrollbar()
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)  # 防止在右侧，将Y轴填满
text = tkinter.Text(win, width=30, height=4)
str = """1 : <CFString 0x7fff98cce6a8 [0x7fff98c3e8e0]>{contents = "AppleSelectedInputSources"} = <CFArray 0x7fd5aff442f0 [0x7fff98c3e8e0]>{type = immutable, count = 1, values = (
        0 : <CFBasicHash 0x7fd5aff46a70 [0x7fff98c3e8e0]>{type = immutable dict, count = 3,
entries =>
        0 : <CFString 0x7fff98cacf68 [0x7fff98c3e8e0]>{contents = "InputSourceKind"} = <CFString 0x7fff98cf24a8 [0x7fff98c3e8e0]>{contents = "Keyboard Layout"}
        1 : <CFString 0x7fff98ca7c68 [0x7fff98c3e8e0]>{contents = "KeyboardLayout Name"} = <CFString 0x7fd5aff3a860 [0x7fff98c3e8e0]>{contents = "ABC"}
        2 : <CFString 0x7fff98cde5e8 [0x7fff98c3e8e0]>{contents = "KeyboardLayout ID"} = <CFNumber 0xfc37 [0x7fff98c3e8e0]>{value = +252, type = kCFNumberSInt64Type}
    """
text.insert(tkinter.INSERT, str)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

scroll.config(command=text.yview)  # 滚动条控制文本动
text.config(yscrollcommand=scroll.set) # 文本控制滚动条动
win.mainloop()