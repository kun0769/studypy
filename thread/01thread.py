#!/usr/bin/env python
#coding:utf8

import thread
import time

def func(name,i,l):
    for n in xrange(i):
        print name,n
        time.sleep(1)
    try: 
        l.release()
    except:
        pass
    

#生产锁对象并获得锁
lock=thread.allocate_lock()
lock.acquire()
thread.start_new_thread(func,('声音',3,lock))
thread.start_new_thread(func,('画面',3,lock))

#根据锁作态判断线程是否结束
while lock.locked():
    pass
