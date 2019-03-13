'''
def func_name(参数)
    pass

无特殊，函数名遵循标识符规则

'''
import time

def zhangjian():
    print("zhang jian is a good man ")
    time.sleep(0.5)
    #zhangjian()
    
#zhangjian()

#参数
def zhangjian1(hello):
    print(id(hello))
    hello = "world"
    print("zhang jian is a good man")
    time.sleep(0.5)
    #zhangjian()

hello = "hello"
print(id(hello))
zhangjian1(hello)
print(hello)


#值传递 引用传递


def zhangjian2(hello):
    print(id(hello))
    hello[1] = 3
    print("zhang jian is a good man")
    time.sleep(0.5)
    #zhangjian()

list_temp = [5,6,7,8]

zhangjian2(list_temp)
print(list_temp)

#变量引用常量的地址

#调用函数不传递参数使用默认值,一般将包含默认参数的参数放在最后
def zhangjian3(name = "zhangjian"):
    print(name)

zhangjian3("helloworld")

#不定长参数
def zhangjian4(nam, *args):
    for i in args:
        print(i)

zhangjian4(1,2,3,4,5,6,7,8)
#字典，传值用 key-value 形式  
def zhangjian5(**kwargs):
    print(type(kwargs))
    print(kwargs)

zhangjian5(zhangjian = 1)

#传任意长度，任意类型参数
def zhangjian6(*arg,**kwargs):
    pass

#匿名参数，不适用 def 关键字去定义 使用 lambdea
#主体是一个表达式，表达式中封装简单逻辑
#有自己的命名空间 且不能访问自由参数列表之外的或全局命名空间外的参数

#格式 lambda arg1,arg2,arg3:expression
sum = lambda num1,num2:num1+num2

print(sum(1,2))
