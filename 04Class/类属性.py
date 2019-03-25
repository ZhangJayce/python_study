# -*- coding: UTF-8 –*-

class Person():
    name = "zhang jian"#用于直接使用类去访问 如下
    def __init__(self):
            self.name = "han lai"

aaa = Person()

print(aaa.name)

print(Person.name)
#对象属性优先于类属性
#不要将对象属性和类属性重名

#限制添加属性
class test():
    __slots__ = ("zhang")#只能添加该元祖中成员为属性
    pass

a = test()
a.head = 1

