#!/usr/bin/env python
#coding:utf8

with open('/etc/hosts') as fd:
    while True:
        line=fd.readline().strip()
        if not line:
            break
        print line
