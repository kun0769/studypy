#!/usr/bin/env python
#coding:utf8

from subprocess import Popen,PIPE

p=Popen(['dmidecode'],stdout=PIPE)
data=p.stdout
lines=[]
a=True
dic_new={}

while a:
    line=data.readline()
    if line.startswith('System Information'):
        while True:
            #读取System Information下一行,非空行把数据写入列表中
            line=data.readline()
            if line =='\n':
                a=False
                break
            else:
                lines.append(line)
#把列表变成字典
dic=dict([i.strip().split(': ') for i in lines])
dic_new['Manufacturer']=dic['Manufacturer']
dic_new['Product']=dic['Product Name']
dic_new['Serial']=dic['Serial Number']

for k,v in dic_new.items():
    print k,v
