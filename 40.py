#!/usr/bin/env python
#coding:utf8

from subprocess import Popen,PIPE

def getIfconfig():
    p=Popen(['ifconfig'],stdout=PIPE)
    data=p.stdout.read().split('\n\n')
    #去掉lo开头的和空的字符串
    data=[i for i in data if i and not i.startswith('lo')]
    return data

def parseIfconfig(data):
    dic={}
    for lines in data:
        line=lines.split('\n')
        devname=line[0].split(': ')[0]
        #找出mac地址的行
        for i in line:
            if i.endswith('(Ethernet)'):
                eth=i
        macaddr=eth.split()[1]
        ipaddr=line[1].split()[1]
        dic[devname]=[ipaddr,macaddr]
    return dic

if __name__=='__main__':
    data=getIfconfig()
    print parseIfconfig(data)
