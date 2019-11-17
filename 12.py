#!/usr/bin/env python

import os

def isNum(s):
    for i in s:
        if i not in '0123456789':
            break
    else:
        print s

for i in os.listdir('/proc'):
    isNum(i)
