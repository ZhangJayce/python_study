# -*- coding: UTF-8 –*-

from types import MethodType

def say():
    print("say")

class Cat():
    pass

hanLai = Cat()

hanLai.say = MethodType(say,hanLai)
hanLai.say()
