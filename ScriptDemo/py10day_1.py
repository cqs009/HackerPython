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
            print("%s 调用了一个 %s 的函数" %(time.ctime(time.time()),threadName))
            counter -= 1


rk = MyThread(1,'瑞克',3)
mt = MyThread(1,'莫蒂',3)
#rk.start()
#mt.start()

# ================= 简单的线程同步 ====================
threadingLock = threading.Lock()
threads = []
class SynThread(threading.Thread):
    ''' 
        自定意同步的线程类 
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
        threadingLock.acquire()# 获取线程锁，用于线程同步
        print_time(self.name,3,self.counter)
        
        threadingLock.release()# 释放锁，开启下一个线程
        print("线程调用的函数执行完成")
print('========== 简单的线程同步 ==========')



xn = SynThread(1,'瑞克', 3)
xn2 = SynThread(1,'莫蒂',3)
xn.start()
xn2.start()
threads.append(xn)
threads.append(xn2)

for th in threads:
    th.join()
    print('退出线程')



# ================ 线程优先级队列 =================================

# 引用 Queue 模块
import queue
print('===== 线程优先级队列 =====')


class QueueThread(threading.Thread):
    '''
        自定义的使用了线程优先级队列的线程类
    '''
    def __init__(self, threadID, threadName, que):
        # 初始化 threading 
        threading.Thread.__init__(self)
        self.treadID = threadID
        self.name = threadName
        self.q = que
    def run(self):
        print('开启线程：' + self.name)
        print_quedate(self.name, self.q)
        print('退出线程：' + self.name)

def print_quedate(threadName, q):

    while not q.empty():
        
        threadLock.acquire()
        if not q.empty():
            quedata = q.get()
            threadLock.release()
            print('%s 从队列盒子中取出了：%s' %(threadName, quedata))
        else:
            print('该队列已空！')
        time.sleep(1)

# 初始化数据
threadNameList = ['电佬', 'XX','飞佬']
quedataList = ['旺仔牛奶糖','鸡腿','可乐','鸡翅']
# 定义线程锁
threadLock = threading.Lock()
# 实例化线程优先级队列
strQueue = queue.Queue(13)


def test(threadNameList, quedataList):

    #初始化线程ID
    threadID = 1

    # 线程集合
    threadList = []
    # 使用线程锁同步填充队列
    threadLock.acquire()
    for strdata in quedataList:
        strQueue.put(strdata)
    threadLock.release()

    # 创建线程
    for threadName in threadNameList:
        thread = QueueThread(threadID, threadName, strQueue)
        thread.start()
        threadList.append(thread)
        threadID += 1
    


    # 等待全部线程完成后退出
    for th in threadList:
        th.join()
        print('退出主线程')
    

test(threadNameList, quedataList)










