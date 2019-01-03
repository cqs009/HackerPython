#!/usr/bin/puthon

# =========== I/O =======================

#  ===== 输出 ===========================

hello = 'hi man!'

# 使用print() 函数 输出值
print(hello)


# 使用str() 返回一个用户易懂的字符串表达形式
hello = 1/3
try:
    print(hello + '1212')
except Exception:
    print("数据类型不匹配！")

print(str(hello)+ '1212' )

# 使用 str.format() 函数输出指定格式的值
for i in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(i,i*i,i**i))

# 使用 repr() 返回一个解释器易读的表达形式
hello = 'yes\no'
print(hello)
print('=== 分割线 ===')
print(repr(hello))

# 使用input() 读取键盘输入
inputstr = input("请输入内容：")
print(inputstr)

# ======= 读写文件 =====================
# 使用 open() 打开文件
f = open('H:/HackerPython/ScriptDemo/testfile.txt',"w")

# 使用 write() 将内容写入
f.write("py是世界上最好的语言。\n是的，超级非常好用\n")
# 关闭打开的文件
f.close()


# 使用 read() 读取文件全部内容
f = open('H:/HackerPython/ScriptDemo/testfile.txt',"r")
filevalue = f.read()
print(filevalue)
f.close()

# 使用readline()读取单行内容
f = open('H:/HackerPython/ScriptDemo/testfile.txt',"r")
linestr = f.readline()
print(linestr)
f.close()

# 使用 readlines() 来获取多行内容的集合
f = open('H:/HackerPython/ScriptDemo/testfile.txt',"r")
lines = f.readlines()
print(lines)
f.close()

# 使用 tell() 返回文件对象当前的位置（从文件头开始算起的字节数）
f = open('H:/HackerPython/ScriptDemo/testfile.txt',"rb+")
print(f.tell())
f.close()

# 使用 seek(offset, from_what) 函数改变文件的当前位置
# rom_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
f = open('H:/HackerPython/ScriptDemo/testfile.txt',"rb+")
print(f.seek(3,1))
f.close()

# ======================= pickle 模块 ==================================

# 该模块实现了基本的序列化和反序列化

import pickle
import pprint

# 使用该模块将数据对象保存到文件中

data1 = {'a': [1,3,5,7,9]}
output = open('textfile.txt', 'wb')
pickle.dump(data1,output)
output.close

# 使用该模块将数据对象从文件中读出来
#pkfile = open('H:/HackerPython/ScriptDemo/textfile.txt', 'rb')
#data2 = pickle.load(pkfile)
#pprint.pprint(data1)
#pkfile.close()

# =====================python中的文件打开模式 ======================================
#   模式                描述

#   r                   以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。

#   rb                  以二进制格式打开一个文件用于只读，文件指针放在文件头

#   r+                  打开一个文件用于读写，文件指针放在文件头

#   rb+                 以二进制格式打开一个文件用于读写，文件指针放在文件头

#   w                   打开一个文件只用于写入，如果文件存在则打开原有文件，并将原有内容覆盖，如果不存在则新建写入

#   wb                  以二进制格式打开一个文件只用于写入，如果文件存在则打开原有文件，并将原有内容覆盖，如果不存在则新建写入

#   w+                  打开一个文件用于读写，如果文件存在则打开原有文件，并将原有内容覆盖，如果不存在则新建写入

#   wb+                 以二进制格式打开一个文件用于读写，如果文件存在则打开原有文件，并将原有内容覆盖，如果不存在则新建写入

#   a                   打开一个文件用于追加，如果文件存在则文件指针放在文件结尾，再原有内容后面追加内容，不存在则从头追加内容

#   ab                  以二进制的格式打开一个文件用于追加，如果文件存在则文件指针放在文件结尾，再原有内容后面追加内容，不存在则从头追加内容

#   a+                  打开一个文件用于读写，如果文件存在则文件指针放在文件结尾，再原有内容后面追加内容，不存在则从头追加内容

#   ab+                  以二进制格式打开一个文件用于读写，如果文件存在则文件指针放在文件结尾，再原有内容后面追加内容，不存在则从头追加内容







