#!/usr/bin/env python
#coding:utf8

import subprocess

try:
    subprocess.check_call('exit 1',shell=True)
#Exception表示所有异常 这里可以写subprocess.CalledProcessError
except subprocess.CalledProcessError,e:
    print '%s' %e
