#!/usr/bin/python

# ===============================================
#           optparser 学习
# ===============================================

import sys
import os
from optparse import OptionParser

def main():
    usage='这是个参数命令解析器的练习'
    parse = OptionParser(usage)
    parse.add_option('-t',dest='target',help='目标',action='store_true')
    parse.add_option('-u',dest='user',help='用户名',action='store_true')
    parse.add_option('-p',dest='password',help='密码',action='store_true')


    options, args= parse.parse_args()
    print('args--->'+str(args))
    if len(args) != 0:
        parse.print_help()


if __name__=='__main__':
    main()