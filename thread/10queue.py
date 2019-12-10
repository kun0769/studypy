#!/usr/bin/env python
#coding:utf8
#
#program:
#    实现一个线程不断生成一个随机数到一个队列中，实现一个线程从上面的队列里面不断的取出奇数，实现另外一个线程从上面的队列里面不断取出偶数
#
#history:
#2019/12/10    kun    V1.0

import Queue
import threading
import random
import time

#生产10个数的线程
def prodecter(name,queue):
    for i in xrange(10):
        num=random.randint(1,10)
        #获取线程名字
        th_name=name+'-'+threading.currentThread().getName()
        queue.put(num)
        time.sleep(1)
        print "%s:%s -----> %s" %(time.ctime(),th_name,num)

#取基数的线程
def jishu(name,queue):
    th_name=name+'-'+threading.currentThread().getName()
    while True:
        try:
            value=queue.get(1,5)
            if value %2 != 0:
                print "%s:%s -----> %s" %(time.ctime(),th_name,value)
                time.sleep(1)
            else:
                queue.put(value)
        except:
            print "%s:%s finished." %(time.ctime(),th_name)
            break

#取偶数的线程
def oushu(name,queue):
    th_name=name+'-'+threading.currentThread().getName()
    while True:
        try:
            value=queue.get(1,5)
            if value %2 == 0:
                print "%s:%s -----> %s" %(time.ctime(),th_name,value)
                time.sleep(1)             
            else:                         
                queue.put(value)          
        except:                           
            print "%s:%s finished." %(time.ctime(),th_name)
            break

def main():
    q=Queue.Queue(10)
    t_pro=threading.Thread(target=prodecter,args=('pro',q))
    t_jishu=threading.Thread(target=jishu,args=('jishu',q))
    t_oushu=threading.Thread(target=oushu,args=('oushu',q))
    t_pro.start()
    t_jishu.start()
    t_oushu.start()

if __name__=='__main__':
    main()
