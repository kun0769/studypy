# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-01 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=50)),
                ('members', models.ManyToManyField(to='hostinfo.Host')),
            ],
        ),
    ]
