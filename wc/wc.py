#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用函数化实现对文件标准输入和参数做统计

from optparse import OptionParser
import sys
import os

def opt():
    parser=OptionParser()
    parser.add_option('-c','--char',dest='chars',action='store_true',default=False,help='only count chars')
    parser.add_option('-w','--word',dest='words',action='store_true',default=False,help='only count words')
    parser.add_option('-l','--line',dest='lines',action='store_true',default=False,help='only count lines')
    parser.add_option('-n','--nototal',dest='nototal',action='store_true',default=False,help='not display total')
    
    option,args=parser.parse_args()
    return option,args

def cout(file):
    char=len(file)
    word=len(file.split())
    line=file.count('\n')
    return char,word,line

def print_wc(option,line,word,char,fn):
    if option.chars:
        print char,
    if option.words:
        print word,
    if option.lines:
        print line,
    print fn

def main():
    option,args=opt()
    #都没带参数会显示三个对应参数的值
    if not (option.chars or option.words or option.lines):
        option.chars,option.words,option.lines=True,True,True
    
    if args:
        total_lines,total_words,total_chars=0,0,0
        for fn in args:
            if os.path.isfile(fn):
                with open(fn) as fd:
                    file=fd.read()
                    lines,words,chars=cout(file)
                    print_wc(option,lines,words,chars,fn)
                    total_lines+=lines
                    total_words+=words
                    total_chars+=chars
            #判断是否是目录 错误输出
            elif os.path.isdir(fn):
                print >> sys.stderr,'%s: is a directory' %fn
            #判断是否非文件或者目录 错误输出
            else:
                sys.stderr.write('%s: No such file or directory\n' %fn)
        #多个文件才显示total
        if len(args)>1:
            #默认option.nototal值为falue 加-n为true 就不显示total
            if not option.nototal:
                print_wc(option,total_lines,total_words,total_chars,'total')
    else:
        fn=''
        file=sys.stdin.read()
        lines,words,chars=cout(file)
        print_wc(option,lines,words,chars,fn)

if __name__ == '__main__':
    main()
