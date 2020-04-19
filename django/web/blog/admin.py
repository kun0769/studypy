# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Host

# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display=['hostname','ip']

admin.site.register(Host, HostAdmin)

