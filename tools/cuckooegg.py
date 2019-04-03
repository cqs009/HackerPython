#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import crypt

def usage():
    print(" Open Pass Tools\n")
    print("Usage: cuckooegg.py  dictionary file \n")
    print("Examples:")
    print("cuckooegg.py  dictionary.txt ")
    try:
        sys.exit(0)
    except:
        print()

def main():

    global dictionary_file

    if not len(sys.argv[1:]):
        usage()
    
    dictionary_file = sys.argv[1]

    passwd_file = open("/etc/shadow")

    for lien  in passwd_file.readlines():
        
        if  ":" in lien:
            user_name = lien.split(":")[0]
            crypt_pass = lien.split(":")[1].split("    ")
            print("[*] Cracking Password For: %s" %(user_name))
            crackPass(dictionary_file,crypt_pass)


#定义一个提取盐值+生成密文+核对 的函数
def crackPass(dictionary_file,crypt_pass):
    crypt_pass = crypt_pass[0]
    salt = crypt_pass[0:12]  #这里是提取盐值
    dict_file = open(dictionary_file)
    for word in dict_file.readlines():
        word = word.split("\n")
        word = word[0]
        crypt_word = crypt.crypt(word,salt)
        if crypt_pass == crypt_word:
            print("[*] Found Password: %s \n" %(word))
            return
    print("[-] Password Not Found. \n")
    return

if  __name__ == "__main__":
    main()