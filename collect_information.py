#/usr/bin/env python
#coding:utf8

from subprocess import Popen,PIPE
import urllib,urllib2
import pickle
import json

#获得ifconfig命令信息
def getIfconfig():
    p=Popen(['ifconfig'],stdout=PIPE)
    data=p.stdout.read()
    return data

#获得dmidecode命令信息
def getDmi():
    p=Popen(['dmidecode'],stdout=PIPE)
    data=p.stdout.read()
    return data

#处理ifconfig和dmidecode信息转为列表，每段信息为每个元素
def parseData(data):
    data=[i for i in data.split('\n') if i]
    lines=''
    new_list=[]
    for line in data:
        if line[0].strip():
            new_list.append(lines)
            lines=line+'\n'
        else:
            lines+=line+'\n'
    new_list.append(lines)
    new_list=[i for i in new_list if i]
    return new_list

#获得ip信息的字典
def parseIfconfig(new_list):
    new_list=[i for i in new_list if not i.startswith('lo')]
    dic={}
    for line in new_list:
        line=line.split('\n')
        devname=line[0].split(': ')[0]
        ipaddr=line[1].split()[1]
        break
    dic['ip']=ipaddr
    return dic

#获得vendor product sn信息的字典
def parseDmi(new_list):
    dic={}
    new_list=[i for i in new_list if i.startswith('System Information')]
    new_list=[i for i in new_list[0].split('\n')[1:] if i]
    new_dic =dict([i.strip().split(':') for i in new_list])
    dic['vendor']=new_dic['Manufacturer'][1:]
    dic['product']=new_dic['Product Name'][1:]
    dic['sn']=new_dic['Serial Number'][1:10]
    return dic

#获得hostname信息的字典
def getHostname(f):
    with open(f) as fd:
        for i in fd:
            data=i.strip('\n')
            break
    return {'hostname':data}

#获得osver信息的字典
def getOsver(f):
    with open(f) as fd:
        for i in fd:
            data=i.strip()
            break
    return {'osver':data}

#获得cpu_model cpu_num信息的字典
def getCup(f):
    num=0
    with open(f) as fd:
        for i in fd:
            if i.startswith('processor'):
                num+=1
            if i.startswith('model name'):
                model=i.split(': ')[1].strip()
                model=model.split()[0]+' '+model.split()[-1]
    return {'cpu_num':num,'cpu_model':model}

def getMem(f):
    with open(f) as fd:
        for i in fd:
            if i.startswith('MemTotal:'):
               mem=int(i.split()[1].strip())
               break
    mem='%.2fM' %(mem/1024.0)
    return {'memory':mem}

if __name__=='__main__':
    ifconfig_data= getIfconfig()
    dmi_data=getDmi()
    ifconfig_list=parseData(ifconfig_data)
    dmi_list=parseData(dmi_data)

    dic_ip=parseIfconfig(ifconfig_list)
    dic_dmi=parseDmi(dmi_list)

    dic_hostname=getHostname('/etc/hostname')
    dic_osver=getOsver('/etc/redhat-release')
    dic_cpu=getCup('/proc/cpuinfo')
    dic_mem=getMem('/proc/meminfo')
    
    dic={}
    dic.update(dic_hostname)
    dic.update(dic_ip)
    dic.update(dic_osver)
    dic.update(dic_dmi)
    dic.update(dic_cpu)
    dic.update(dic_mem)

    print dic
    #data=urllib.urlencode(dic)
    #把字典序列化为字符串传输到Django的视图函数中
    #data=pickle.dumps(dic)
    data=json.dumps(dic)
    req=urllib2.urlopen('http://192.168.161.100:8000/hostinfo/collect/',data)
    print req.read()
