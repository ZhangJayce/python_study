
#print(3/0)

'''
    try：
        语句
    except 错误码 as e:
        pass
    except 错误码 as e:
        pass
    except 错误码 as e:
    
    else:

'''

try:
    print(3/0)
except ZeroDivisionError as e:
    print("error : ZeroDivisionError")

try:
    print(3/0)
except:
    print("error : ZeroDivisionError")

try:
    print(3/0)
except ZeroDivisionError as e:
    print("error : ZeroDivisionError")

#断言

def func(num,div):
    #断言  意思为不满足条件时候 终止程序打印对应的信息
    assert(div != 0),"div 不能等于0" 
    return(num / div)


func(3,0)