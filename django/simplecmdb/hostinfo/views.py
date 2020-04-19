# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from hostinfo.models import Host,HostGroup
import pickle
import json

# Create your views here.

def collect(request):
    if request.POST:
        print request.body
        #反序列化request.body的信息 request.body表示参数的数据
        #data=pickle.loads(request.body)
        data=json.loads(request.body)
        print data
        hostname=data['hostname']
        ip=data['ip']
        vendor=data['vendor']
        product=data['product']
        osver=data['osver']
        sn=data['sn']
        memory=data['memory']
        cpu_num=data['cpu_num']
        cpu_model=data['cpu_model']
        
        #判断hostname的记录是否存在数据库中,有会更新字段,没会创建新记录
        try:
            h=Host.objects.get(hostname=hostname)
        except:
            h=Host()
        h.hostname=hostname
        h.ip=ip
        h.vendor=vendor
        h.product=product
        h.osver=osver
        h.sn=sn
        h.memory=memory
        h.cpu_num=cpu_num
        h.cpu_model=cpu_model
        h.save()
        return HttpResponse('OK')
    else:
        return HttpResponse('not data')


def getjson(request):
    #获得每个分组
    obj_list=[]
    for hg in HostGroup.objects.all():
        dic_g={'groupname':hg.groupname,'members':[]}
        for h in hg.members.all():
            dic_h={'hostname':h.hostname,'ip':h.ip}
            #把成员的信息插入到members的空列表中
            dic_g['members'].append(dic_h)
        obj_list.append(dic_g)
    print obj_list
    return HttpResponse(json.dumps(obj_list))


def getshell(request):
    obj_str=''
    for hg in HostGroup.objects.all():
        groupname=hg.groupname
        for h in hg.members.all():
            hostname=h.hostname
            ip=h.ip
            obj_str+=groupname+' '+hostname+' '+ip+'\n'
    return HttpResponse(obj_str)
