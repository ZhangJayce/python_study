# -*- coding: utf-8 -*-


# map 和 reduce 的含义

# map (fn, lsd) 参数一是函数，参数而为是序列

# 功能 将传入的函数依次作用做序列里的每一个元素，并且把结果作为新的 Iterator 返回

list1 = ["1", "2", "3", "4"]

res = map(int,list1)

print(list(res))



#reduce(func, lsd)

#一个函数作用在序列上，reduce 把结果继续和序列上的下一个元素做累计运算,函数必须接受两个参数

#reduce(f,[1,2,3,4]) -> reduce(f(f(f(1,2),3),4))


print(list("12345  "))