#!/usr/bin/env python
#coding:utf8

import sys

def lineCount(fd):
    n=0
    for i in fd:
        n+=1
    return n

d=sys.stdin
print lineCount(d)
