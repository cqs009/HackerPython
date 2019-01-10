#!/usr/bin/python

'''
        文件和目录的处理
'''

# 引入 os 和 sys模块

import os,sys,stat


# ==========   目录操作 =============

# 目录枚举
path = "H:\HackerPython"

# os.chdir() 更改文件目录
os.chdir(path)


# 获取指定路径下的子目录和文件信息详细信息
def listdirDetail(path):
        files = os.listdir(path)
        for name in files:
                pathinfo = os.path.join(path, name) # path 拼接
                print("%s 详细信息如下：" %(name)) 
                print("所有者用户ID：%d" %(os.stat(pathinfo).st_uid)) 
                print("inode 保护模式：%s" %(os.stat(pathinfo).st_mode))
                print("inode 节点号：%d" %( os.stat(pathinfo).st_ino))
                print("大小为：%d 字节" %( os.stat(pathinfo).st_size))
                print("最后访问时间 %s" %(os.stat(pathinfo).st_atime))
                print("最后修改时间 %s" %(os.stat(pathinfo).st_mtime))
                print("\n")
                
#listdirDetail(path)

# 判断当前 path 是文件还是目录
def checkPath(path):
        files = os.listdir(path)
        for fileName in files:
                pathinfo = os.path.join(path, fileName)
                fileType = os.stat(pathinfo).st_mode

                if stat.S_ISDIR(fileType):
                        print("%s 是一个目录" %(fileName))
                elif stat.S_ISREG(fileType):
                        print("%s 是一个文件" %(fileName))
                else:
                        print("%s 是一个未知目录类型" %(fileName))

#checkPath(path)


# 遍历多级目录
retractnum = 0
def traverseMultistageDir(path,retractnum):
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
         
              
path = 'H:\HackerPython'
print("%s" %(path))
traverseMultistageDir(path, retractnum)
print("========== 分割线 ==========")




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

os.chdir("H:\HackerPython\ScriptDemo")

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



