#!/usr/bin/env python
#coding:utf8

import sys
import time

for i in range(10):
    sys.stdout.write('str:%d' %i)
    sys.stdout.flush()
    time.sleep(1)
