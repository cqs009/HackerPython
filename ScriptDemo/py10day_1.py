#!/usr/bin/python

import threading
import time


# ==================================================================
# ==                使用 threading模块 来开启使用线程                        ==
# ==================================================================

exitFlag = 0

class MyThread(threading.Thread):
    ''' 
        自定意线程类 
            该继承threading模块的Thread类 
    '''
    def __init__(self,threadID,threadName,counter):
        ''' 构造函数 '''
        # 初始化 threading 
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = threadName
        self.counter = counter
    
    def run(self):
        '''  用以表示线程活动的方法，可在该方法内调用需要执行的函数 '''
        print("开始执行线程调用的函数")
        print_time(self.name,3,self.counter)
        print("线程调用的函数执行完成")
    
def print_time(threadName, delay, counter):
        ''' 自定义函数，用于打印跟踪线程运行 '''
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print("%s 调用了一个 %s 函数" %(time.ctime(time.time()),threadName))
            counter -= 1


rk = MyThread(1,'瑞克',3)
mt = MyThread(1,'莫蒂',3)
rk.start()
mt.start()




















