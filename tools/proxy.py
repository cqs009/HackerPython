#!/usr/bin/python

# ==============================================================================
# ==========================        Porxy       ================================
# ==============================================================================

# 载入系统模块
import sys

# 载入socket模块
import socket

# 载入线程模块
import threading


def server_loop(local_host, local_port,target_host, target_port, receive_first):


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host,local_port))
    except:
        print("[!] Failed to listen on %s:%d" %(local_host,local_port))
        print("[!] Check for other listening socket or correct permissions.")
        sys.exit(0)
    
    print("[*] Listening on %s:%d" %(local_host,local_port))

    server.listen(10)


    while True:
        client_socket,addr = server.accept()
        # 打印本地连接信息
        print("[==>] Received incoming connection from %s:%d" %(addr[0],addr[1]))

        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket, target_host, target_port, receive_first))

        proxy_thread.start()



def main():

    # 获取命令
    if len(sys.argv[1:]) != 5:
        print("Usage: ./proxy.py|proxy.py [localhost] [localport] [targethost] [targetport] [receive_first]")
        print("Example: ./proxy.py|proxy.py 127.0.0.1 9999 10.11.13.1 9999 True")
        sys.exit()

    # 设置本地监听参数
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    # 设置远程目标
    target_host = sys.argv[3]
    target_port = int(sys.argv[4])

    # 让代理在发送给远程主机之前连接和接受数据
    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    # 设置监听 socket
    server_loop(local_host,local_port,target_host,target_port,receive_first)



def proxy_handler(client_socket, target_host, target_port,receive_first):

    # 连接远程主机
    target_socket =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    target_socket.connect((target_host,target_port))

    # 是否从远程主机接收数据
    if receive_first:
        target_buffer = receive_from(target_socket)
        hexdump(target_buffer)
        # 发送给我们得响应处理
        target_buffer = response_handler(target_buffer)
        
        if len(target_buffer):
            print("[<==] Sending %d bytes to localhost." %(len(target_buffer)))
            client_socket.send(target_buffer.encode('utf-8'))
    
    # 循环读取本地得数据并发送给远程主机和本地主机
    while True:

        # 读取本地数据
        local_buffer = receive_from(client_socket)

        if len(local_buffer):
            print("[==>] Received %d bytes from localhost." %(len(local_buffer)))
            hexdump(local_buffer)

            # 发送数据到本地
            local_buffer = request_handler(local_buffer)

            # 发送数据到远程主机
            target_socket.send(local_buffer.encode('utf-8'))
            print("[==>] Sent to target")
        # 接收响应数据
        target_buffer = receive_from(target_socket)
       
        if len(target_buffer):
            print("[<==] Received %d bytes from target." %(len(target_buffer)))
            hexdump(target_buffer)

            # 发送数据到响应处理函数
            target_buffer  = response_handler(target_buffer)

            # 发送响应到本地 socket
            client_socket.send(target_buffer.encode('utf-8'))
            print("[<==] Sent to localhost.")

        if not len(local_buffer) or not len(target_buffer):
            client_socket.close()
            target_socket.close()
            print("[*] No more data. Closing connections.")
            break


def hexdump(src,length=16):
    result = []
    digits = 2 if isinstance(src, str) else 4
    for i in range(0, len(src), length):
        s = src[i:i+length]
        hexa = ' '.join(['%0*X' % (digits, ord(x)) for x in s])
        text = ''.join([x if 0x20 <= ord(x) < 0x7F else '.' for x in s])
        result.append('%04X  %-*s   %s' % (i, length*(digits + 1), hexa, text))

    print('\n'.join(result))


def receive_from(connection):

    buffer = ""

    # 设置超时时间
    connection.settimeout(30)

    try:
        while True:
            data = connection.recv(102400)

            
            if not data:
                break
            buffer += data.decode('utf-8')
    except:
        pass
    return buffer

# 对目标是远程主机得请求进行修改
def request_handler(buffer):
    # 执行包修改 
    return buffer

# 对目标是本地主机得响应进行修改
def response_handler(buffer):
    return buffer

main()