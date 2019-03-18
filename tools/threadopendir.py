#!/usr/bin/python

import sys
# 文件管理模块
import os
import time
# 线程模块
import threading
# 子流程管理模块
import subprocess

import stat

import queue

dirs = []
# 定义线程锁
threadLock = threading.Lock()

strQueue = queue.Queue(100)

def main():
    if len(sys.argv[1:]) < 1:
        print("Usage: ./threadopendir.py  [absolute path1] [absolute path2]...")
        print("Example: ./threadopendir.py  /usr/bin  /opt ...")
        sys.exit()

    for i in range(len(sys.argv[1:])):
        dirs.append(sys.argv[i+1])#s
    

     # 线程集合
    threadList = []

   # 使用线程锁同步填充队列
    threadLock.acquire()
    for strdata in dirs:
        strQueue.put(strdata)
    threadLock.release()

    # 创建线程
    for i in range(len(dirs)):
        thread = dirThread(i,strQueue)
        thread.start()
        threadList.append(thread)
     # 等待全部线程完成后退出
    for th in threadList:
        th.join()
        print('退出主线程')



# 遍历多级目录
retractnum = 0
def traverseMultistageDir(path,retractnum=0):
         paths = os.listdir(path)
         strs = '       '*retractnum
         retractnum += 1
         for pathtime in paths:
                newpath = os.path.join(path, pathtime)
                fileType = os.stat(newpath).st_mode

                if stat.S_ISDIR(fileType):
                        print(strs+"%s" %(pathtime))
                        
                        traverseMultistageDir(newpath,retractnum)
                else:
                        print(strs+"%s" %(pathtime))


# 定义线程类
class dirThread(threading.Thread):

        def     __init__(self,threadId,que):
                threading.Thread.__init__(self)
                self.threadId = threadId
                self.q = que
        def run(self):
                 print_quedate(self.q)



def print_quedate(q):

    while not q.empty():
        
        threadLock.acquire()
        if not q.empty():
            quedata = q.get()
            threadLock.release()
            retractnum = 0
            print('从目录盒子中取出了：%s' %(quedata))
            traverseMultistageDir(quedata,retractnum)
        else:
            print('该队列已空！')
        time.sleep(1)


main()