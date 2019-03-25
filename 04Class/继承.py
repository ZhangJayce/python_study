# -*- coding: UTF-8 –*-

class Person():
    def __init__(self,name):
        self.name = name
        self.__money = 1000
    def getMoney(self):
        return self.__money
    def setMoney(self,money):
        self.__money = money

class Student(Person):
    def __init__(self,name):
        super(Student,self).__init__(name)
        #使用super来初始化父类中的属性
        Person.__init__(self,name)
zhangjian = Student("zhangjian")
hanlai = Student("hanlai")
zhangjian.setMoney(1234)

print(zhangjian.name)
print(zhangjian.getMoney())
print(hanlai.getMoney())

#多继承 多个父类中包含同样的方法，哪个父类排在前面调用对应父类的方法


