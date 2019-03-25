# -*- coding: utf-8 -*-


class test(object):
    def __init__(self, age, name):
        self.age = age
        self.__name = name  # 此为限制访问

    def __add__(self, other):
        # 相当于重新生成了一个对象
        return test(self.age + other.age, self.__name + other.__name)

    def __str__(self):
        return "age = " + str(self.age)

#  不同的加法会有不同的解释
print(1 + 2)
print("1" + "2")

test1 = test(1, "zhangjian")
test2 = test(2, "hanLai")

print(test1 + test2)

