#!/usr/bin/env python

import hashlib
import sys

def md5(f):
    m=hashlib.md5()
    with open(f) as fd:
        while True:
            data=fd.read(4096)
            if data:
                m.update(data)
            else:
                break
    return m.hexdigest()

if __name__=='__main__':
    try:
        print md5(sys.argv[1]),sys.argv[1]
    except IndexError:
        print "%s need to follow file"  %__file__   

