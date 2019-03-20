class cat():
    def __init__(self,a,b,c):#创建对象的时候自动调用 
        self.a = a
        self.b = b
        self.__c = c

    def __repr__(self):
        print("this is __repr__")
    def __str__(self):
        return "this is str"
    def eat(self):
        print("eat fish : ",self.__c)
    def __del__(self):
        print("this is del")

hanLai = cat(1,2,3)

#如何做私有变量
#变量前加  __   python 中，属性前加两个下划线，属性变成 私有（private）
hanLai.eat()

#hanLai.c = 100
#print(hanLai.c)
