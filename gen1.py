#!/usr/bin/env python
#coding:utf8
#
#progarm:
#    通过访问url获得json格式的主机信息并根据主机信息生成nagois配置文件
#
#history:
#2019/11/10    kun    V1.0

import os
import urllib,urllib2
import json

cur_dir=os.path.dirname(__file__)   #当前目录
conf_dir=os.path.join(os.path.abspath(cur_dir),'host')  #配置文件目录

#创建目录
if not os.path.exists(conf_dir):
    os.mkdir(conf_dir)

#定义配置文件
host_tmp="""define host {
    use                     linux-server
    host_name               %(hostname)s
    alias                   %(hostname)s
    address                 %(ip)s
}
"""

#获得url的主机信息
url='http://192.168.161.100:8000/hostinfo/getjson/'
reqest=urllib2.urlopen(url)    #获得json格式信息
data=json.loads(reqest.read()) #获得列表

#获得配置文件的内存再写入文件中
conf=''
for hg in data:
    for dic in hg['members']:
        conf+=host_tmp %dic   #把members的字典的value替换调host_tmp中的key

host_conf=os.path.join(conf_dir,'host.conf')
with open(host_conf,'w') as fd:
    fd.write(conf)   #把conf信息写入文件host/host.conf中


