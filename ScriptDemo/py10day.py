#!/usr/bin/python

import _thread
import time


# ==================================================================
# ==                使用函数式来开启使用线程                        ==
# ==================================================================




# 创建一个被调用函数
def print_treadName(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s 调用了一个 %s 函数" %(time.ctime(time.time()),threadName))


try:
    _thread.start_new_thread(print_treadName,("瑞克",2, ))
    _thread.start_new_thread(print_treadName,("莫蒂",4, ))
except:
    print("ERROR:线程开启失败！！")


while 1:
    pass














