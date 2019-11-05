#!/usr/bin/env python
#coding:utf8

import os
import sys
import operator

def get_dic(dir):
    dic={}
    for i,j,k in os.walk(dir):
        for file in k:
            #得到文件路径
            filedir=os.path.join(i,file)
            #得到文件的大小
            filesize=os.path.getsize(filedir)
            dic[filedir]=filesize
    #返回{文件名:大小}的字典
    return dic

if __name__ =='__main__':
    dic=get_dic(sys.argv[1])    
    #字典根据文件大小倒序排序
    dic=sorted(dic.iteritems(),key=operator.itemgetter(1),reverse=True)
    #遍历自动的前10个
    for k,v in dic[:10]:
        print k,v
