#!/usr/bin/python
# -*- coding: utf-8 -*-

import optparse #选项解释器

from socket import *
import socket

def connScan(target_host,target_port):
    try:
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((target_host,target_port)) 
        print("[+] %s/tcp 开放" %(target_port))
        client.close()
    except :
        print("[-] %s/tcp 关闭" %(target_port))

def portScan(target_host,target_ports):
    try:
        ip = gethostbyname(target_host)
    except:
        print("[-] 无法解析 '%s': 位置地址" %(target_host))
        return
    try:
        target_name = gethostbyaddr(ip)
        print("[+] 扫描的结果: %s" %(target_name))
    except:
        print("[+] 扫描的结果: %s" %(ip))
    print("扫描端口 %s" %(target_ports))
    connScan(target_host,int(target_ports))

def main():
    parse = optparse.OptionParser()
    parse.add_option("-H", "--tgthost",dest="tgthost",type='str',help="要扫描的目标地址")
    parse.add_option("-p", "--tgtport",dest="tgtport",type='str',help="要扫描的目标端口")

    (options, args) = parse.parse_args()
    target_host = options.tgthost
    target_ports = options.tgtport
    print(target_ports)
    if (target_host == None) | (target_ports== None):
        print(parse.usage)
        exit()

    portScan(target_host,target_ports)


if  __name__ == "__main__":
    main()




