#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用多个线程处理同一个变量，使其值+1
#
#histoty:
#2019/12/02    kun    V1.0

import threading
import time

count=0

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        time.sleep(0.5)
        lock.acquire()
        count +=1
        print 'I am %s ,set nount: %s' %(self.name,count)
        lock.release()

if __name__=='__main__':
    #定义锁对象,让其线程执行是按照顺序来
    lock=threading.Lock()
    for i in xrange(200):
        t=MyThread()
        t.start()
