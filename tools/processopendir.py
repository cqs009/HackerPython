#!/usr/bin/python

import sys
import os
from multiprocessing import Process, Pool,Lock
import queue
import stat
import time

dirs = []
pool = Pool(10)
lock = Lock()
strQueue = queue.Queue(100)
def main():
    if len(sys.argv[1:]) < 1:
        print("Usage: ./processopendir.py  [absolute path1] [absolute path2]...")
        print("Example: ./processopendir.py  /usr/bin  /opt ...")
        sys.exit()

    for i in range(len(sys.argv[1:])):
        dirs.append(sys.argv[i+1])
    #dirs.append("/opt")
    #dirs.append("/mnt")


    for item in dirs:
        retractnum=0
        p = Process(target=traverseMultistageDir,args=(item,retractnum))
        p.start()
        p.join()
 


def traverseMultistageDir(path,retractnum=0):
         paths = os.listdir(path)
         strs = '       '*retractnum
         retractnum += 1
         for pathtime in paths:
                newpath = os.path.join(path, pathtime)
                fileType = os.stat(newpath).st_mode

                if stat.S_ISDIR(fileType):
                        print(strs+"%s" %(pathtime))
                        
                        traverseMultistageDir(newpath,retractnum)
                else:
                        print(strs+"%s" %(pathtime))





if  __name__ == '__main__':
    main()