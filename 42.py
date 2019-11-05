#!/usr/bin/env python
#coding:utf8

from subprocess import Popen,PIPE
import re

def getIfconfig():
    p=Popen(['ifconfig'],stdout=PIPE)
    data=p.stdout.read().split('\n\n')
    #去掉lo开头的和空的字符串
    data=[i for i in data if i and not i.startswith('lo')]
    return data

def parseIfconfig(data):
    re_devname=re.compile(r'(ens|lo|virbr)\d+',re.M)
    re_ip=re.compile(r'inet\s([\d\.]{7,15})',re.M)
    re_mac=re.compile(r'ether\s([0-9a-f:]+)',re.M|re.I)
    if re_devname.search(i):
        devname=re_devname.search(i).group(0)
    else:
        devname=''
    if re_ip.search(i):
        ip=re_ip.search(i).group(1)
    else:
        ip=''
    if re_mac.search(i):
        mac=re_mac.search(i).group(1)
    else:
        mac=''
    return {devname:[ip,mac]}
        
if __name__=='__main__':
    data=getIfconfig()
    for i in data:
        print parseIfconfig(i)
