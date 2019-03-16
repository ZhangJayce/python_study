'''
    os : 包含了普通的os 的功能


'''
import os
import time
print(os.name)

print(os.environ)

print(os.curdir)

print(os.getcwd())#当前路径

print(os.listdir())#指定目录下所有的文件

#print(os.mkdir("zhangjian"))

#print(os.rmdir("zhangjian"))

#print(os.stat("zhangjian")) #查看文件状态

#print(os.rename("zhangjian","jayce"))

print(os.system("ipconfig"))#运行shell or dos命令

print(os.path.abspath("."))#相对路径 转 绝对路径

#拼接路径

r'''
C:\Users\ZhangJian\Desktop\jayce\python_study
    +
    jayce
'''

p1 = r"C:\Users\ZhangJian\Desktop\jayce\python_study\jayce.txt"
p2 = "jayce"
p3 = r"C:\Users\ZhangJian\Desktop\jayce\python_study\jayce"

print(os.path.join(p1,p2))

#拆分路径 
print(os.path.split(p1))#生成元祖，拆最后一个
print(os.path.splitext(p1))#生成元祖，拆最后一个扩展名

print(os.path.isdir(p1))
print(os.path.isdir(p3))
print(os.path.isfile(p3))
#判断路径(文件 / 文件夹)是否已存在
print(os.path.exists(r"C:\Users\ZhangJian\Desktop\jayce\python_study\02进阶\os_module.py"))

#获取文件大小
print(os.path.getsize(r"C:\Users\ZhangJian\Desktop\jayce\python_study\02进阶\os_module.py"))
