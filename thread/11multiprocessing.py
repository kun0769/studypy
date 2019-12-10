#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用multiprocessing模块生产10个进程
#
#history:
#2019/12/10    kun    V1.0

import multiprocessing
import os
import time

def fun(i):
    print i,os.getpid(),os.getppid()
    time.sleep(1)

for i in xrange(10):
    p=multiprocessing.Process(target=fun,args=(i,))
    p.start()
