#!/usr/bin/env python
#coding:utf8
#
#progarm:
#    通过访问url获得json格式的主机信息并根据主机和主机组信息生成nagois配置文件
#    增加对同一个主机在不同主机组的判断 和 访问不了Django的url时从临时文件读取json信息
#
#history:
#2019/11/10    kun    V2.1

import os
import urllib,urllib2
import json

cur_dir=os.path.dirname(__file__)   #当前目录
conf_dir=os.path.join(os.path.abspath(cur_dir),'host')  #配置文件目录
cache_file='/tmp/json.tmp'


#定义主机配置文件
host_tmp="""define host {
    use                     linux-server
    host_name               %(hostname)s
    alias                   %(hostname)s
    address                 %(ip)s
}
"""

#定义主机组配置文件
hostgroup_tmp="""define hostgroup {
    hostgroup_name          %(groupname)s
    alias                   %(groupname)s
    members                 %(members)s
}
"""

#创建目录
def initDir():
    if not os.path.exists(conf_dir):
        os.mkdir(conf_dir)

def getData():
    #获得url的主机信息
    url='http://192.168.161.100:8000/hostinfo/getjson/'
    #能访问到url获得json信息会写一份到json.tmp,访问不到时读取json.tmp的json数据
    try:
        reqest=urllib2.urlopen(url)    #获得json格式信息
        reqest_data=reqest.read()
        with open(cache_file,'wb') as fd:
            fd.write(reqest_data)
        data=json.loads(reqest_data) #获得列表
        return data
    except:
        with open(cache_file) as fd:
            data=json.load(fd)
        return data

def writeConf(f,s):
    with open(f,'w') as fd:
        fd.write(s)   #把conf信息写入文件host/host.conf中

#计算主机名出现的次数 {hostname:次数}
def count(key,dic):
    if key in dic:
        dic[key]+=1
    else:
        dic[key]=1

def parseData(data):
    #获得配置文件的内存再写入文件中
    hostnameconf=''
    groupnameconf=''
    dic_new={}
    for hg in data:
        groupname=hg['groupname']
        members=[]
        for dic in hg['members']:
	    hostname=dic['hostname']
            members.append(hostname)
            count(hostname,dic_new)  #执行count函数 获得主机名出现次数的dic
            #主机名出现一次的才会去替换配置文件
            if dic_new[hostname] <2:
                hostnameconf+=host_tmp %dic   #把members的字典的value替换调host_tmp中的key
        groupnameconf+=hostgroup_tmp %{'groupname':groupname,'members':','.join(members)} #把自定义的字典的value替换调hostgroup_tmp中的key  ','.join(members)把[]变成str
    
    host_conf=os.path.join(conf_dir,'host.conf')
    group_conf=os.path.join(conf_dir,'group.conf')

    writeConf(host_conf,hostnameconf)  #主机信息写入配置文件
    writeConf(group_conf,groupnameconf) #主机组信息写入配置文件

if __name__=='__main__':
    initDir()
    data=getData()
    parseData(data)
