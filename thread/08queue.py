#!/usr/bin/env python
#coding:utf8
#
#program:
#    起主线程生产10个数字，并让3个线程打印出来
#
#history:
#2019/12/03    kun    V1.0

import threading
import Queue
import time
import random

class MyThread(threading.Thread):
    #queue对象作为参数传入
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue
    
    def run(self):
        #从队列中取出数据并打印，队列为空退出循环
        while True:
            if self.queue.empty():
                break
            data = self.queue.get()
            print data,time.ctime()
            time.sleep(1)

if __name__=='__main__':
    #实例化队列对象并循环10次插入1-10的随机数
    queue=Queue.Queue(10)
    for i in xrange(10):
        queue.put(random.randint(1,10))
    #并行开启三个进程打印数据
    for i in xrange(3):
        t=MyThread(queue)
        t.start()
