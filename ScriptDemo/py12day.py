#!/usr/bin/python3

import socket
import sys
# ==============================================
# ==============      TCP 客户端      ===========
# ===============================================

#目标域名或IP
target_host = "127.0.0.1"
#目标端口
target_port = 9999


# 创建一个客户端  socket.socket(family,type,)
#family参数指的是host的种类：
#    AF_UNIX：也叫AF_LOCAL,基于本地文件的
#   AF_NETLINK：这是linux系统支持的一种套接字
#    AF_INET：这个套接字是基于网络的，对于IPV4协议的TCP和UDP（常用）
#    AF_INET6：这个套接字是基于网络的，对于IPV6协议的TCP和UDP
#type参数指的是套接字类型：
#    SOCK_STREAM：流套接字，使用TCP socket（常用）
#    SOCK_DGRAM：数据报套接字，使用UDP socket（常用）
#    SOCK_RAW：raw套接字
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接客户端
client.connect((target_host,target_port))

#======== py3不能发送str字符，需要转成 bytes =========================
# 发送数据
datastr = "are you ok?"

client.send(datastr.encode())

# 接收返回数据
response = client.recv(4096)

print(response.decode())

client.close()








