#!/usr/bin/env python

import os

def isNum(s):
    if s.isdigit():
        return 1
    else:
        return 0

for i in os.listdir('/proc'):
    if isNum(i):
        print i
