'''
    #装饰器
    
    概念 ： 是一个闭包，把一个函数当作参数就返回一个替代版的函数
'''

#作用如下 >>>
def zhangjian():
    print("zhang jian is a good man")

def zhangjian_out(func):
    print("hello world")
    func()

zhangjian_out(zhangjian)
#          <<<

#最简单的装饰器如下

def outer(func):
    def inner():
        print("hello world")
        func()
    return inner

func = outer(zhangjian)

func()

#稍微复杂
def say(age):
    print("zhangjian age is %d" %age)

say(100)

def outer1(func):
    def inner(age):
        if(age < 0):
            age = 0
        func(age)
    return inner

f1 = outer1(say)#需要调用  flow 下面

f1(-1)

######################################################

def outer2(func):
    def inner(age):
        if(age < 0):
            age = 0
        func(age)
    return inner

#使用@ 将 装饰器应用到函数
@outer2 
def say1(age):
    print("zhangjian age is %d" %age)

say1(-1)
#以上装饰器不通用

def outer3(func):
    def inner(*args,**kwargs):
        #添加修改的功能
        func(*args,**kwargs)
    return inner
