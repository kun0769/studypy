#!/usr/bin/env python

from subprocess import Popen,PIPE

p=Popen('ls /tmp',shell=True)
p.wait()
print 'main process'
