#!/usr/bin/env python
#
#program:
#    使用multiprocessing.Pool方法运行多进程
#    设置5个进程来等待执行 池子中只能有2个进程
#
#history:
#2020/04/14    kun    V1.0

import multiprocessing
from subprocess import Popen,PIPE

def run(id):
    p=Popen('vim',stdout=PIPE,stderr=PIPE)
    p.communicate
    print "Task: %s" %id

#只能同时运行两个进程
pool=multiprocessing.Pool(processes=2)
#设置5个进程
for i in xrange(5)
    pool.apply_async(func=run,args=(i,))
print "Wait..."

pool.close()
pool.join()
print "Down..."
