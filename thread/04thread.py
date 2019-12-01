#!/usr/bin/env python
#coding:utf8

import threading
import time

def func(name,i):
    for n in xrange(i):
        print name,n
        time.sleep(1)

t1=threading.Thread(target=func,args=('声音',3))
t2=threading.Thread(target=func,args=('画面',3))

#设置线程和主线程一同结束
t1.setDaemon(True)
t1.start()
t2.setDaemon(True)
t2.start()
