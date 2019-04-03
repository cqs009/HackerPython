#!/usr/bin/python3

# =================================================
# ==========      TCP 服务端    ====================
# =================================================

import socket
import threading

server_host = "0.0.0.0"
server_port = 9999

# 创建一个socket
server_address = (server_host, server_port)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 确定服务器得监听地址和端口
server.bind(server_address)

# 设置启动监听并设置最大连接数
server.listen(10)
print("[*] LISTENING ON %s:%d" %(server_host, server_port))

# 客户端消息应答处理线程
def handle_client(client_socket):
  # 获取客户端发送得内容
  request = client_socket.recv(4096)
  print("[*] Received: %s" %(request.decode()))
  # 返回一个数据包
  datastr = "OK"
  data = datastr.encode()
  client_socket.send(data)
  client_socket.close()

while True:
  client,address = server.accept()
  print("[*] Accept connection from %s:%d" %(address[0],address[1]))
  # 挂起客户端消息应答处理线程 处理客户端传入过来得数据
  handler_thread = threading.Thread(target=handle_client, args=(client,))
  handler_thread.start()