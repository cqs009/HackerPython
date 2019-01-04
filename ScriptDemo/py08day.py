#!/usr/bin/python

'''
    文件操作相关知识点
'''

# open() 的完整格式
# open(file,mode='r',buffering=0,encoding=utf8,errors=None,newline=None,closefd=True,opener=None)
# file: 文件的相对或绝对路径
# mode: 文件打开模式
# buffering: 设置缓冲
# errors: 设置报错级别
# newline: 区分换行符
# encodeing: 编码格式
# closefd: 传入的file参数类型
# ==================================================================================
# 文件打开模式（续上节）
#   模式        描述
#   t           文本模式（默认）
#   +           打开一个文件进行更新，可读可写
#   x           新建写入


# ==================================================================================

# flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件中

f = open('testfile.txt','a+')
f.write('糟老头子坏滴很\n')
f.flush()
f.close()

f = open('testfile.txt','r+')
print(f.read())
f.close()
# 使用 fileno() 返回一个整型的文件描述符，可用于一些底层操作上
f = open('testfile.txt','rb')
print(f.fileno())
f.close()

# 使用 isatty() 判断文件是否连接到一个设备上
f = open('testfile.txt','r')
print(f.isatty())
f.close()

# 使用 next() 返回文件下一行
f = open('testfile.txt','r')
print(next(f))
f.close()

# 使用runcate([size])








