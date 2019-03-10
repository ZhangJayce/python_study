'''
    这中间是注释
'''

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




