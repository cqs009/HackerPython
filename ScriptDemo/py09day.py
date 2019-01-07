#!/usr/bin/python

'''
        文件和目录的处理
'''

# 引入 os 和 sys模块

import os,sys

# access(path,mode) 校验目录权限
# mode有一下几个
# os.F_OK: 测试path是否存在
# os.R_OK: 测试path是否可读
# os.W_OK: 测试path是否可写
# os.X_OK: 测试path是否可执行

ret = os.access('aaa',os.F_OK)
print(ret)

ret = os.access('testfile.txt',os.R_OK)
print(ret)


ret = os.access('textfile.txt',os.W_OK)
print(ret)

ret = os.access('py01day.py',os.X_OK)
print(ret)

# os.getcwd() 查看当前的path
print(os.getcwd())










