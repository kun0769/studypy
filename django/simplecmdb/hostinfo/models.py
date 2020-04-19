# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Host(models.Model):
    hostname=models.CharField(max_length=50)
    vendor=models.CharField(max_length=50)
    product=models.CharField(max_length=50)
    osver=models.CharField(max_length=50)
    sn=models.CharField(max_length=50)
    memory=models.CharField(max_length=50)
    cpu_num=models.IntegerField()
    cpu_model=models.CharField(max_length=50)
    ip=models.GenericIPAddressField()

    def __str__(self):
        return self.hostname

class HostGroup(models.Model):
    groupname=models.CharField(max_length=50)
    members=models.ManyToManyField(Host)
