#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用multiprocessing.Pool方法创建多进程
#
#history:
#2020/04/14    kun    V1.0

import multiprocessing
import os
import time

def run(id):
    print "id:%s pid:%s ppid:%s" %(id, os.getpid(), os.getppid())
    start=time.time()
    time.sleep(3)
    end=time.time()
    print "Task %s run %0.2f" %(id, (end-start))
    

if __name__=='__main__':
    pool=multiprocessing.Pool(processes=2)
    for i in xrange(5):
        pool.apply_async(func=run,args=(i,))

    pool.close()
    pool.join()
    print "Down..."
