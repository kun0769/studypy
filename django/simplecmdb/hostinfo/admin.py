# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from hostinfo.models import Host,HostGroup

# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display=['hostname','ip','cpu_num','cpu_model','memory','vendor','product','osver','sn']

class HostGroupAdmin(admin.ModelAdmin):
    list_display=['groupname']

admin.site.register(Host,HostAdmin)
admin.site.register(HostGroup,HostGroupAdmin)
