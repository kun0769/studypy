#!/usr/bin/env python
#coding:utf8
#
#program:
#    此插件是nagoins自定义插件
#    根据给点的值来返回警告或严重等信息
#    ./check_mem.py -w 500 -c 100 当内存少于500M报警告，少于100M报严重警告
#
#history:
#2019/11/17    kun    V1.0

from optparse import OptionParser
import sys

def opt():
    parse=OptionParser('Usage: %prog [-w WARNING] [-c CRITICAL]')
    parse.add_option('-w',dest='warning',action='store',default='100',help='WARNING')
    parse.add_option('-c',dest='critical',action='store',default='50',help='CRITICAL')

    option,args=parse.parse_args()
    return option,args

def getMem(f):
    with open(f) as fd:
        for line in fd:
            if line.startswith('MemFree'):
                mem=line.split()[1].strip()
                break
    return int(mem)/1024

def main():
    option,args=opt()
    w=int(option.warning)
    c=int(option.critical)
    mem=getMem('/proc/meminfo')
    if mem > w:
        print "OK "+str(mem)+"MB"
        sys.exit(0)
    elif c < mem <= w:
        print "WARNING "+str(mem)+"MB"
        sys.exit(1)
    elif mem < c:
        print "CRITICAL "+str(mem)+"MB"
        sys.exit(2)
    else:
        print "UNKOWN "+str(mem)+"MB"
        sys.exit(3)


if __name__=='__main__':
    main()
