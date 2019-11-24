#!/usr/bin/env python
#coding:utf8
#
#program:
#    此插件是nagoins自定义插件
#    检测日志文件同一个时刻同一个进程出现报错的最多的次数的日志数量并进行报告
#    
#history:
#2019/11/19    kun    V1.0

from optparse import OptionParser
from subprocess import Popen,PIPE
import shlex
import datetime
import operator
import sys
import re

MONTH={'jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jan':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
#匹配日志每行信息
LOG_RE=re.compile(r'(?P<logtime>\w{3}\s{1,2}\d{1,2}\s[\d:]{8})\s(?P<hostname>[\w\.]+)\s(?P<program>\w+(\[\d+\])?):\s(?P<msg>.*)')

def opt():
    parse=OptionParser("Usage: %prog [-w WARNING] [-c CRITICAL]")
    parse.add_option('-w',dest='warning',action='store',default=5,help='WARNING')
    parse.add_option('-c',dest='critical',action='store',default=10,help='CRITICAL')
    option,args=parse.parse_args()
    return option,args

#取得日志内容
def getLog(f,n):
    cmd='tail -n %s %s' %(n,f)
    p=Popen(shlex.split(cmd),stdout=PIPE,stderr=PIPE)
    stdout,stderr=p.communicate()
    return stdout

#获得日志每行的时间并用datetime.datetiem格式显示
def parseLogTime(line):
    now=datetime.datetime.now()
    #取每行日志的时间段
    month,day,time=line.split()[:3]
    hour,minute,secend=[int(i) for i in time.split(':')]
    logtime=datetime.datetime(now.year,MONTH[month],int(day),hour,minute,secend)
    return logtime

def count(k,d):
    if k in d:
        d[k]+=1
    else:
        d[k]=1

def parseLog(data):
    dic={}
    now=datetime.datetime.now()
    ten_min_ago=now-datetime.timedelta(minutes=10)
    data=[ i for i in data.split('\n') if i ]
    for line in data:
        logtime=parseLogTime(line)
        #当行时间大于10分钟前的时间
        if logtime > ten_min_ago:
            match=LOG_RE.search(line)
            if match:
                #匹配的每行日志信息通过字典形式返回
                match_dic=match.groupdict()
                k=str(logtime)+' '+match_dic['program']
                if 'error' or 'failed' in match_dic['msg'].lower():
                    count(k,dic)
    return dic   

def main():
    #获得当前执行用户 默认是nagios
    p=Popen('whoami',stdout=PIPE,shell=True)
    user=p.stdout.read()
    option,args=opt()
    w=int(option.warning)
    c=int(option.critical)
    lines= c*600
    data=getLog('/var/log/messages',lines)
    dic=parseLog(data)
    if not dic:
        print "OK,the log is null.",user
        sys.exit(0)
    #对字典进行排序取value最大的值和w,c比较
    sort_dic=sorted(dic.iteritems(),key=operator.itemgetter(1),reverse=True)[0]
    num=sort_dic[1]
    if num < w:
        print "OK :",sort_dic,user
        sys.exit(0)
    elif w <= num < c:
        print "WARNING :",sort_dic,user
        sys.exit(1)
    elif num >= c:
        print "CRITICAL :",sort_dic,user
        sys.exit(2)
    else:
        print "NUKOWN :",sort_dic,user
        sys.exit(3)

if __name__=='__main__':
    main()
