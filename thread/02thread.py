#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用锁令一个线程输出Hello，另一个输出World 并输出5行
#    主线程输出Hello 其他线程(函数)输出World
#
#history:
#2019/12/01    kun    V1.0

import thread
import time

def world():
    for i in xrange(5):
        if w_lock.acquire():
            print 'World',time.ctime()
            h_lock.release()

h_lock=thread.allocate_lock()
w_lock=thread.allocate_lock()
thread.start_new_thread(world,())
w_lock.acquire()
for i in xrange(5):
    if h_lock.acquire():
        print 'Hello',
        w_lock.release()

while h_lock.locked():
    pass
