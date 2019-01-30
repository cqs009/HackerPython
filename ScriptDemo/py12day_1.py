#!/usr/bin/python
import socket


target_host = "192.168.0.102"
target_port = 80

address = (target_host,target_port)

# 创建一个无连接客户端
# 基于IPv4标准的网络数据包套接字
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据包
datastr = "python"
datastr = datastr.encode()
client.sendto(datastr, address)

client.close()