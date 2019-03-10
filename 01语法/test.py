'''
    这中间是注释
'''

import time
import random
import turtle
#print(1+2)

#tip1 if 相关的用法

a = 100
b = 100
if (a == 10):
    print("hello world")
elif(b == 10):
    print ("zhang jian is not a good man")
else:
    print("zhang jian is a good man")


#tip2 while 循环
'''
while 条件：
    语句
'''

i = 10
while i > 0:
    print("zhang jian is a good man",i)
    i -= 1

#tip3 for 的用法
'''
    for iterating_var in sequence:
        statements(s)
'''

#tip4 strcmp

print ("a" < "b")

#tip5 数据类型
    #5.1 bool
bool_type = True
print(bool_type)

bool_type = None
print(bool_type)
    #5.2 list &&m for
num = [11,12,13,14]

print(num[0])
for i in range(len(num)):
    print(num[i])
num[3]=1000
print(num[-1])


    #list 操作
list1 = [1,2,3,4]
list2 = [6,7,8]
print(list1 + list2)
    #判断成员是否存在 in
print(2 in list1)
    #列表截取
print(list1[1:3])
    #多维列表 仅作了解
    #列表成员也是列表

#列表追加
list1.append(5)#列表的末尾追加一个元素
print(list1)

list1.append(list2)#列表的末尾追加一个元素
print(list1)

list1.extend(list2)#列表的末尾追加另一个列表中的多个元素
print(list1)

list1.insert(2,100)#在指定index出插入一个元素
print(list1)
list1.pop()#移除列表中的一个元素，返回值为删除的元素
print(list1)

list1.remove(6)#移除列表中的第一这匹配的元素
print(list1)

list1.remove([6,7,8])#移除列表中的第一这匹配的元素
print(list1)

list1.clear()#清除列表中所有元素
print(list1)

print(list2)

print(list2.index(6))#找出列表中的的第一次出现元素的下标，可以多个参数
list3 = [4,6,7,8,5]
print(max(list2))#列表中的最大值
print(min(list2,list3))#列表中的最小值,列表的大小比较类似于字符串

list3.count(4)#元素出现的次数

#值得深思 为什么没有自增运算符 引用他人解释
#link https://blog.csdn.net/somehow1002/article/details/73744626
'''
为什么没有自增。。。的运算符
变量是以内容为基准而不是像 c 中以变量名为基准，所以只要你的数字内容是5，不管你起什么名字，这个变量的 ID 是相同的，同时也就说明了 python 中一个变量可以以多个名称访问
这样的设计逻辑决定了 python 中数字类型的值是不可变的，因为如果如上例，a 和 b 都是 5，当你改变了 a 时，b 也会跟着变，这当然不是我们希望的

因此，正确的自增操作应该 a = a + 1 或者 a += 1，当此 a 自增后，通过 id() 观察可知，id 值变化了，即 a 已经是新值的名称
'''
#自我理解：++名为自增，数字本身为一个数字类型对象，数字类型对象是不可以变得
print(list1)
list1.reverse()#倒序
list1.sort()#升序不传参数

#浅拷贝 又叫做引用拷贝 两个变量指向了同一块空间
list1 = list2
print(list1,list2)

#深拷贝     memcpy
list3 = list2.copy()

#找出第二大的数
list4 = [1,2,3,4,5,6,7,8,9,0,9,9]
list5 = list(set(list4))
print(list5[-2])

if i > 1 and i < 4 :
    print()

# while True:
#     print("hello world")
#     time.sleep(0.5)
    
'''

for 循环

for 变量 in 集合
    语句

按顺序取集合中的每个元素赋值给变量，直到集合中的变量取完为止

'''
print(range(0,20,2))
print(range(0,20,2))
for i in range(0,21,2):#range(start,end,step)
    print(i)

for index,data in enumerate((1,2,3,4,5)):
    print(index, data)
    if index == 3:
        break


#while 语句  如果被 break 中断的else 不会执行
print(random.randint(0,10))


turtle.done()