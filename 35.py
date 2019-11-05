#!/usr/bin/env python

import os
import string

def is_Num(s):
    for i in s:
        if i in string.digits:
            continue
        else:
            return False
    return True

for pid in os.listdir('/proc'):
    if is_Num(pid):
        print pid
