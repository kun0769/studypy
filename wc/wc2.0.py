#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用optparse模块实现对文件标准输入和参数做统计

from optparse import OptionParser
import sys

parser=OptionParser()
parser.add_option('-c','--char',dest='chars',action='store_true',default=False,help='only count chars')
parser.add_option('-w','--word',dest='words',action='store_true',default=False,help='only count words')
parser.add_option('-l','--line',dest='lines',action='store_true',default=False,help='only count lines')

option,args=parser.parse_args()

#都没带参数会显示三个对应参数的值
if not (option.chars or option.words or option.lines):
    option.chars,option.words,option.lines=True,True,True

if args:
    fn=args[0]
    with open(fn) as fd:
        file=fd.read()
else:
    fn=''
    file=sys.stdin.read()

char=len(file)
word=len(file.split())
line=file.count('\n')

if option.lines:
    print line,
if option.words:
    print word,
if option.chars:
    print char,
print fn
