'''
三大属性：
    类名    首字母大写 其他遵循驼峰规则 
    属性
    行为

'''
'''
class 类名(父类，可以有多个)：
    定义属性
    定义方法
'''
#创建一个类
#object 基类，超类，所有类的父类，可以省略
class ZhangJian(object):
    name = ""
    age = 0

    def study(self, time):
        print(self.name,"study",time,"hours")

ZhangJian.name = "zhang jian"

#实例化对象
#格式 对象名 = 类名(参数列表)

zhang1 = ZhangJian()
zhang2 = ZhangJian()
print(id(zhang1.name))
print(id(zhang2.name))

zhang1.name = "zhangjian"
zhang1.study(1)


#目前看来所有的对象属性都一样

#构造函数

class cat():
    def __init__(self,a,b,c):#创建对象的时候自动调用 
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        print("this is __repr__")
    def __str__(self):
        return "this is str"
    def eat(self):
        print("eat fish")
    def __del__(self):
        print("this is del")

hanLai = cat(1,2,3)

print(hanLai.a,hanLai.b,hanLai.c)

#self代表类的实例(对象)而非类

#self 不是关键字，一半常用self

print(hanLai)
print(hanLai.__class__)#表示类名

hanLai1 = hanLai.__class__(7,8,9)#可以使用这样创建对象

print(hanLai1.a,hanLai1.b,hanLai1.c)


#析构器 释放时候自动调用
del hanLai1
del hanLai

#重写__repr__与__str__ 将函数重新定义

#__str__ 一般显示出所有的参数
#__repr__ 终端使用时候输出，没有str 时候调用此方法 
hanLai2 = cat(11,12,13)
print(hanLai2)

