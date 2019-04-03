# -*- coding: utf-8 -*-


import tkinter

win = tkinter.Tk()

win.title("zhang jian is a good man")

#  设置大小和位置 前面大小 后面坐标
win.geometry("800x800+200+200")

str1 = tkinter.StringVar()

listbox = tkinter.Listbox(win, selectmode=tkinter.BROWSE, )
listbox.pack()

listbox.insert(tkinter.END, "111")
listbox.insert(tkinter.END, "222")
listbox.insert(tkinter.END, "333")
listbox.insert(tkinter.END, "444")
listbox.insert(tkinter.END, "555")
listbox.insert(tkinter.ACTIVE, "000")
#选中 
listbox.select_set(2, 5)
listbox.select_clear(3)

print("==============", listbox.size()) # 列表中的元素个数
# 获取内容
listbox.get(1)

listbox.delete(1)

# 当前选项选中的索引
print(listbox.curselection())
# 判断一个选项是否被选中
print(listbox.select_includes(2))
win.mainloop()