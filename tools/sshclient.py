#!/usr/bin/python

# ============================================================
# ===============       简单的SSH 客户端      =================
# ============================================================

import sys
import threading
import paramiko
import subprocess


def ssh_command():
    # 获取命令
    if len(sys.argv[1:]) != 4:
        print("Usage: ./sshclient.py|sshclient.py [ip] [username] [password] [cmd]")
        print("Example: ./sshclient.py|sshclient.py 10.11.13.43 root root pwd")
        sys.exit()
    
    # 设置参数
    ip = sys.argv[1]
    uname = sys.argv[2]
    upass = sys.argv[3]
    cmd = sys.argv[4]

    client = paramiko.SSHClient()

    # 密钥认证
    #client.load_host_keys()
    # 用户名、密码认证
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=uname, password=upass)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(cmd)
        data = ssh_session.recv(1024)
        print(data.decode('utf-8'))
    return
ssh_command()