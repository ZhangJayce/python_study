#set 是一组key的集合，不存储value

#本质为无序无重复元素的集合

#创建一个set 需要一个list / tuple /dict 作为输入集合 

dict1 = {"zhangjian":100,"hello world":1111}

set1 = set(dict1)

set1.add(1)

#set1.add([1,2]) 不能插入列表

#打碎插入
set1.update([1,2,3,4,5,6])

print(set1)

# 交集 并集

#set主要用于类型转换