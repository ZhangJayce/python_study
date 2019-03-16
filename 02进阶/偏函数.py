import functools
#传入base = value  可以做进制转换
print(int('12345',base = 16))

#可以使用偏函数

def int16(x,base = 16):
    return int(x,base)

print(int16("10"))

#可以使用functool.partial 创建 
#把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

int2 = functools.partial(int, base=2)


