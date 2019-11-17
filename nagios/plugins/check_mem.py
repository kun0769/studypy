#!/usr/bin/env python
#coding:utf8
#
#program:
#    此插件是nagoins自定义插件
#    根据给点的值来返回警告或严重等信息
#    ./check_mem.py -w 500 -c 100 当内存少于500M报警告，少于100M报严重警告
#    使用参数可以带定位和人性化显示 ./check_mem.py -w 1.5g -c 1g 
#
#history:
#2019/11/17    kun    V2.0

from optparse import OptionParser
import sys

unit={'b':1,'k':2**10,'m':2**20,'g':2**30,'t':2**40}

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
    return int(mem)*1024

def scaleUnit(s):
    #获得字符串最后的定位并统一为小写字母
    lastchar=s[-1]
    lastchar=lastchar.lower()
    #定位前的数字
    num=float(s[:-1])
    if lastchar in unit:
        return num * unit[lastchar]  #取得对应单位的byte值
    else:
        return int(s)  #没有带单位的

#让byte值和字典值作比较在0-1024间获得其对应单位
def human(byte):
    for k,v in unit.items():
        num=float(byte)/v
        if 0 < num <= 1024:
            num="%.2f" %num
            result=str(num)+k.upper()
            return result

def main():
    option,args=opt()
    w=scaleUnit(option.warning)
    c=scaleUnit(option.critical)
    mem=getMem('/proc/meminfo')
    h_mem=human(mem)
    if mem > w:
        print "OK ",h_mem
        sys.exit(0)
    elif c < mem <= w:
        print "WARNING ",h_mem
        sys.exit(1)
    elif mem < c:
        print "CRITICAL ",h_mem
        sys.exit(2)
    else:
        print "UNKOWN ",h_mem
        sys.exit(3)


if __name__=='__main__':
    main()
