#!/usr/bin/env python
#coding:utf8

import hashlib
import sys
import os

def md5sum(f):
    m=hashlib.md5()
    with open(f) as fd:
        while True:
            data=fd.read(4096)
            if data:
                m.update(data)
            else:
                break
    return m.hexdigest()

#获得目标路径的生成器
target=os.walk(sys.argv[1])

for i,j,k in target:
    for file in k:
        #获得文件路径
        filedir=os.path.join(i,file)
        #获得其文件的MD5值
        md5=md5sum(filedir)
        print md5,filedir
