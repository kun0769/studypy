#!/usr/bin/python

with open("/home/kun/python/aa") as fd:
    while 1:
        line=fd.readline()
        if not line:
            break
        print line,
