#!/usr/bin/env python
#coding:utf8

import sys
import os

if len(sys.argv)==1:
    file=sys.stdin.read()
else:
    try:
        fn=sys.argv[1]
    except IndexError:
        print "请在脚本%s后加上参数" %__file__
        sys.exit()
    if not os.path.exists(fn):
        print "%s 不存在" %fn
        sys.exit()

    with open(sys.argv[1]) as fd:
        file=fd.read()

chars=len(file)
words=len(file.split())
lines=file.count('\n')

print '%(lines)s %(words)s %(chars)s' %locals()
