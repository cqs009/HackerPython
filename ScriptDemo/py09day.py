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

# os.chdir() 更改文件目录
os.chdir('testpage')
print(os.getcwd())
os.chdir('h:\HackerPython\ScriptDemo')
print(os.getcwd())

# os.chmod(path,mode) 更改权限
# mode部分的参数
# 参数值                权限掩码                说明
# stat.S_IXOTH          0o001           其他用户的执行权限
# stat.S_IWOTH          0o002           其他用户的写权限
# stat.S_IROTH          0o004           其他用户的读权限
# stat.S_IRWXO          0o007           其他用户的所有权限       
# stat.S_IXGRP          0o010           用户组的执行权限
# stat.S_IWGRP          0o020           用户组的写权限
# stat.S_IRGRP          0o040           用户组的读权限
# stat.S_IRWXG          0o070           用户组的全部权限
# stat.S_IXUSR          0o100           拥有者的执行权限
# stat.S_IWUSR          0o200           拥有着的写权限
# stat.S_IRUSR          0o400           拥有者的读权限
#stat.S_ISVTX           0o1000          目录里文件目录只有拥有者才可删除更改
#stat.S_ISGID           0o2000          执行此文件其进程有效组为文件所在组
#stat.S_ISUID           0o4000          执行此文件其进程有效用户为文件所有者
#stat.S_IREAD                           windows下设为只读
#stat.S_IWRITE                          windows下取消只读

os.chmod('testpage',0o002)
print('修改成功')

# 更改文件所有者 os.chown(path,uid,gid) 参数：文件路径，所属用户ID，所属用户组ID



