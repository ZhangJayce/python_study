# -*- coding: utf-8 -*-


class test(object):
    def __init__(self, age, name):
        self.age = age
        self.__name = name  # 此为限制访问

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


# 避免将属性直接暴露出来
zhangJian = test(1, "zhangjian")
print(zhangJian.name)  # 相当于调用了getName()
zhangJian.name = "hanlai"  # 相当于调用了 setName() 好处是为复制给过滤 替代了set 和 get
print(zhangJian.name)
