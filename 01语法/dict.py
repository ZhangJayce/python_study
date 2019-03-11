'''
    使用键值(key-vakue)对存储，具有几块的存储速度
    key 的特性
        1. 字典中的key唯一
        2. key必须是不可变对象，一半可用整数，字符串
        3. 列表可变，不可以做key
'''

#字典的创建

stu1 = {"zhangjian":100,"lilei":100}

#字典的访问
print(stu1["zhangjian"])
#print(stu1["aaa"])#没有值会报错
print(stu1.get("zhang"))

#添加
stu1["jayce"] = 100
print(stu1)

#遍历

for key in stu1:
    print(key)
    print(stu1[key])

for value in stu1.values():
    print(value)

for k,v in stu1.items():
    print(k,v)

for k,v in enumerate(stu1):
    print(k,v)

str2 = "hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world "
l = str2.split(" ")
print(l)

dict3 = {"zhangjian":100,"lilei":100}

print(dict3.get("a"))

z = dict3.get("a")

    