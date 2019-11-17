#!/usr/bin/env python 
#coding:utf8
#
#program:
#    计算出整个目录的文件大小

from optparse import OptionParser 
import os
import sys

def opt():
    cmd=OptionParser()
    cmd.add_option('-H','--human',dest='human',action='store_true',default=False,help='human-readable display')
    option,args=cmd.parse_args()
    return option,args

#获得文件路径和文件大小的字典
def getSize(targetdir):
    dic={}
    for i,j,k in os.walk(targetdir):
        for file in k:
            filedir=os.path.join(i,file)
            filesize=os.path.getsize(filedir)
            dic[filedir]=filesize
    return dic

def human(num):
    if num < 1024:
        return '%s' %num
    elif num >= 1024 and num < 1024**2:
        return '%sK' %(num/1024)
    elif num >= 1024**2 and num < 1024**3:
        return '%sM' %(num/1024/1024)
    else:
        return '%sG' %(num/1024/1024/1024)
        
def main():
    option,args=opt()
    print option,args
    if option.human:
        for k,v in getSize(args[0]).iteritems():
            if v !=0:
                print k,human(v)
    else:
        for k,v in getSize(args[0]).iteritems():
            #过滤掉文件大小是0的文件
            if v !=0:
                print k,v    
            
if __name__=='__main__':
    main()
