#!/usr/bin/env python
#coding:utf8

from subprocess import Popen,PIPE

def getIfconfig():
    p=Popen(['ifconfig'],stdout=PIPE,stderr=PIPE) 
    stdout,stderr=p.communicate()
    data=stdout.split('\n')
    data=[i for i in data if i]
    return data

def listIfconfig(data):
    lines=''
    new_list=[]
    for line in data:
        #字符串开头是定格的
        if line[0].strip():
            #第一次lines为空 ['','br0','lo']
            new_list.append(lines)
            lines=line+'\n'
        #字符串开头是\t 把该行字符串加进之前的lines中
        else:
            lines+=line+'\n'

    #因为遍历完找不到line[0].strip() 最后一次要重新加入列表中
    new_list.append(lines)
    new_list=[i for i in new_list if i and not i.startswith('lo')]
    return new_list

def parseIfconfig(new_list):
    dic={}
    for lines in new_list:
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
    new_list=listIfconfig(data)
    print parseIfconfig(new_list)
