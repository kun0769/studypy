#!/usr/bin/env python
#coding:utf8

from subprocess import Popen,PIPE
import shlex
import os

def getPid():
    #获得pid对象
    pid=Popen(shlex.split('pidof httpd'),stdout=PIPE)
    #获得httpd服务的pid的列表
    pids=pid.stdout.read().split()
    return pids

def getMen(pids):
    sum=0
    for pid in pids:
        #/proc/pid/status
        filename=os.path.join('/proc',pid,'status')
        with open(filename) as fd:
            for line in fd:
                if line.startswith('VmRSS:'):
                    #获得单个httpd进程的物理内存
                    men=int(line.split()[1])
                    #计算总的httppd物理内存
                    sum+=men
                    break
    return sum

def getTotal(f):
    with open(f) as fd:
        for line in fd:
            if line.startswith('MemTotal:'):
                #获得总物理内存
                total=line.split()[1]
                return total

if __name__=='__main__':
    mem= getMen(getPid())
    total= getTotal('/proc/meminfo')
    #print "httpd memory is %sK" %mem
    #print "Percent: %.2f%%" %(mem/float(total)*100)
    print 'httpd memory is {}K'.format(mem)
    print 'Percent: {:.2f}%'.format(mem/float(total)*100)
