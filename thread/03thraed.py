#!/usr/bin/env python
#coding:utf8

import threading
import time

def func():
    print 'Hello World',time.ctime()
    time.sleep(1)

if __name__=='__main__':
    for i in xrange(10):
        #实例threading对象
        t=threading.Thread(target=func,args=())
        #开启线程
        t.start()
        t.join()
