'''
    每一个.py文件就是一个模块

    模块：
        内置模块
        三方模块
        自定义模块
'''

import sys
import os
print(sys.argv)

#print(sys.path)
import zhangjian
zhangjian.my_print("zhangjian")#使用模块.函数名

#另外一种导入模式  从 zhangjian 导入 my_print  引入一部分

from zhangjian import my_print
my_print("hello world")

#将当前文件（zhangjian） 所有的内容全部导入
from zhangjian import *


print("1",__name__)


#如果有重名的模块 用包
#目录中包含一个 “__init__.py”的文件才能叫做一个包

import a.zhangjian
import b.zhangjian


a.zhangjian.my_print()
b.zhangjian.my_print()