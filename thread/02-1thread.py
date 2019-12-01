#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用锁令一个线程输出Hello，另一个输出World 并输出5行
#    一个线程输出Hello 一个线程输出World 主线程也使用锁来判断是否两个线程执行完来结束主线程
#
#history:
#2019/12/01    kun    V1.0

import thread
import time

def hello():
    for i in xrange(5):
        h_lock.acquire()
        print 'Hello',
        w_lock.release()

def world():
    for i in xrange(5):
        w_lock.acquire()
        print 'World',time.ctime()
        h_lock.release()
    lock.release()

#lock对象用于判断主线程的结束
lock=thread.allocate_lock()
lock.acquire()
h_lock=thread.allocate_lock()
w_lock=thread.allocate_lock()
w_lock.acquire()
thread.start_new_thread(hello,())
thread.start_new_thread(world,())

while lock.locked():
    pass
