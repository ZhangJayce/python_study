'''
    如何自定义一个模块

'''
print(__name__)#当模块使用的时候为 模块名

def my_print(str):
    print(str)


if __name__ == "__main__":#自身运行的时候为__main__
    print("test")

