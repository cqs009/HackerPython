#!/usr/bin/python

'''
    进程模块

'''

# 导入相应的模块
import time
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_process(name):
  print('运行子进程 %s' %(name))


# 创建一个简单的进程

if __name__ == '__name__':
  run_process(name='test')
else:
  print('========')