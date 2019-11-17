#!/usr/bin/env python
#coding:utf8

import sys

with open('/tmp/test1.txt','w') as fd:
    print >> fd,"this is test\n",111111111111


print >> sys.stderr,'this is stderr\n'

