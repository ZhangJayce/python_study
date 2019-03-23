class Animal():
    def __init__(self,name):
       self.name = name
    def eat(self):
        print(self.name," eaat food")

class Cat(Animal):
    def __init__(self,name):
        super(Cat,self).__init__(name)
        Animal.__init__(self,name)

hanLai = Cat("hanLai")

hanLai.eat()
