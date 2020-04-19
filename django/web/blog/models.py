# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Host(models.Model):
    hostname=models.CharField(max_length=50)
    ip=models.GenericIPAddressField()
