#!/usr/bin/env python
#coding:utf8

import sys

file=sys.stdin.read()

chars=len(file)
words=len(file.split())
lines=file.count('\n')

print "%(lines)s %(words)s %(chars)s" %locals()

