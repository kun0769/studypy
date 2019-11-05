#!/usr/bin/env python
#coding:utf8

from subprocess import Popen,PIPE

def getDmi():
    p=Popen(['dmidecode'],stdout=PIPE)
    data=p.stdout.read()
    return data

def parseDmi(data):
    lines=[]
    line=data.split('\n')
    dmi_list=[i for i in line if i]
    a=False
    for line in dmi_list:
        if line.startswith('System Information'):
            a=True
            continue
        if a:
            #判断每行开头是否是\t \t的strip()为False
            if not line[0].strip():
                lines.append(line)
            else:
                break
    return lines
    
def dmiDic():
    dmi_dic={}
    data=getDmi()
    lines=parseDmi(data)
    dic=dict([i.strip().split(':') for i in lines])
    dmi_dic['Manufacturer']=dic['Manufacturer']
    dmi_dic['Product Name']=dic['Product Name']
    dmi_dic['Serial Number']=dic['Serial Number']
    return dmi_dic
    
if __name__=='__main__':
    print dmiDic()
