#!/usr/bin/env python
#coding:utf8
#
#program:
#    起主线程生产10个数字，并让3个线程打印出来
#    生产速度小于消费速度
#
#history:
#2019/12/05    kun    V1.0

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
            data = self.queue.get()
            if data == None:
                break
            print data,time.ctime()

if __name__=='__main__':
    #先生产线程后生产数据,消费速度大于生产速度,进程会阻塞
    #并行开启三个进程打印数据,等于同时开启三个进程
    queue=Queue.Queue(10)
    for i in xrange(3):
        t=MyThread(queue)
        t.start()
    #实例化队列对象并循环10次插入1-10的随机数
    for i in xrange(10):
        queue.put(random.randint(1,10))
        time.sleep(1)

    #生产完数据后向队列添加none,三个进程添加3次
    queue.put(None)
    queue.put(None)
    queue.put(None)
