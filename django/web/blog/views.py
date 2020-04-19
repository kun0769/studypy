# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from blog.models import Host

# Create your views here.

def index(request):
    t=loader.get_template('index.html')
    c={}
    return HttpResponse(t.render(c))

def db(request):
    print request
    if request.GET:
        hostname=request.GET.get('hostname')
        ip=request.GET.get('ip')
        h=Host()
        h.hostname=hostname
        h.ip=ip
        print h.hostname
        print h.ip
        h.save()
        return HttpResponse('OK')
    elif request.POST:
        hostname=request.POST.get('hostname')
        ip=request.POST.get('ip')
        h=Host()
        h.hostname=hostname
        h.ip=ip
        h.save()
        return HttpResponse('OK')
    else:
         return HttpResponse('no data')
