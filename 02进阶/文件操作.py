#文件操作


'''

1. open(path,flag[,encoding],[,errors])

flag :
    r rb r+ ....

'''
file_path = r"C:\Users\ZhangJian\Desktop\jayce\python_study\02进阶\偏函数.py"
fd = open(file_path,"r",encoding='UTF-8')

str1 = fd.read()#全部读出
print(str1)

fd.seek(0)# 文件指针指向指定位置
print("****************")
str1 = fd.read(10)#读十个字节
print(str1)

fd.readline()#读取一行 包括换行


fd.readline(6)#读取指定字节数
fd.seek(0)
list = fd.readlines()#读取所有行并且返回一个列表

print(list)

list = fd.readlines()#给定的数字大于0  返回实际size 字节的行


#读文件需要一个完整的过程 打开 ， 读写 ，关闭

try:
    fd = open(file_path,"r",encoding='UTF-8')
finally:
    if fd:
        fd.close()

#常用，使用完自动关闭

with open(file_path,"r",encoding = "UTF-8") as fd:
    print(fd.read())

# write


with open(r"C:\Users\ZhangJian\Desktop\test.txt","w+",encoding = "UTF-8") as fd:
    fd.write("zhang jian is a good man ")#写进缓冲区 未刷新时候不会写入文件
    #fd.flush()
    # while True:
    #     pass


'''
    刷新缓存区的方法 ：
        缓存区满
        文件描述符关闭
        程序退出
        手动刷新
'''
with open(r"C:\Users\ZhangJian\Desktop\test.txt","wb") as fd:
    str = "zhang jian is a good man张健"
    fd.write(str.encode("utf-8"))
with open(r"C:\Users\ZhangJian\Desktop\test.txt","rb") as fd:
    str = fd.read()
    new_str = str.decode("gbk ")
    print(new_str)

#编码 解码 应该一致


#list tuple set dict  类型的文件读写
import pickle#数据持久性模块


my_list = [1,2,3,4,5,"zhang jian is a good man"]

with open(r".\test","wb") as fd:
    pickle.dump(my_list,fd)


with open(r".\test","rb") as fd:
    read_list = pickle.load(fd)
    print(read_list)
