import time

'''
utc时间

DST:夏令时，夏季调快一个小时

'''

'''
表现形式
    时间戳
    元祖
        一个python 的 数据结构 表示，元祖有九个元素
    格式化字符串
'''

print(time.gmtime())

print(time.localtime())

print(time.time())#时间戳

print(time.mktime(time.localtime()))#元祖转时间戳

print(time.asctime(time.localtime()))#元祖转转字符串

print(time.ctime(time.time()))#时间戳转字符串

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))#将元祖转字符串类型

print(time.strptime("2019-03-17 20:53:29","%Y-%m-%d %H:%M:%S"))#将元祖转字符串类型

#返回当前程序的cpu执行时间
#Unix 始终返回全部的运行时间
#windows 从第二次开始，距离上一个clock 所运行的时间 
#该方法 将在3.8 删除 time.perf_counter or time.process_time instead
print(time.clock())

print(time.clock())

for i in range(1):
    pass

print(time.clock())

'''
datetime
    模块中的类：
        datetime 同时拥有时间和日期
        timedelta 计算时间的跨度
        tzinfo  时区信息
        time    只关注时间
        date    只关注日期
'''
import datetime

#获取当前时间
d = datetime.datetime.now()
print(d)

print(type(d))

d1 = d.strftime("%Y-%m-%d %H:%M:%S")
print(d1)
print(datetime.datetime.strptime(d1,"%Y-%m-%d %H:%M:%S"))

d3 = datetime.datetime.now()

time.sleep(0.1)

d4 = datetime.datetime.now()

print(d4 - d3)#计算时间的相差

import calendar#日历模块

print(calendar.month(2019,3))

print(calendar.calendar(2017))

print(len(calendar.month(2019,3)))