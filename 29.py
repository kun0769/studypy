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

def file(f):
    #获得目标路径的生成器
    target=os.walk(f)
    
    for i,j,k in target:
        for file in k:
            #获得文件路径
            filedir=os.path.join(i,file)
            #获得其文件的MD5值
            md5=md5sum(filedir)
            yield '%s %s' %(md5,filedir)

if __name__=='__main__':
    try:
        line=''
        gen=file(sys.argv[1])
        for i in gen:
            #把多个文件和其md5值组合在一起
            line+=i+'\n'
        print line
        #打印出集合体/目录的md5值
        print hashlib.md5(line).hexdigest()
    except IndexError:
        print '%s need to follow file' %__file__
