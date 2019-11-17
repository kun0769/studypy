#!/usr/bin/env python
#coding:utf8

import hashlib
import os
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

def file_dic(dir):
    #定义空字典组成新的数据结构
    dic={}
    a=os.walk(dir)
    for i,j,k in a:
        for file in k:
            filedir=os.path.join(i,file)
            md5file=md5(filedir)
            #判断md5的key是否在字典中 有就添加该文件到对应的文件列表中，没有则创建新文件列表
            if dic.has_key(md5file):
                dic[md5file].append(filedir)
            else:
                dic[md5file]=[filedir]
    return dic

if __name__=='__main__':
    dic=file_dic(sys.argv[1])
    for k,v in dic.items():
        #文件列表>1表示多个文件有相同的md5值
        if len(v)>1:
            print k,v
