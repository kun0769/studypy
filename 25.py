#!/usr/bin/env python
#coding:utf8

from optparse import OptionParser
import sys
import os

def opt():
    parse=OptionParser()
    parse.add_option('-c','--char',dest='char',action='store_true',default=False,help='show count chars')
    parse.add_option('-w','--word',dest='word',action='store_true',default=False,help='show count words')
    parse.add_option('-l','--line',dest='line',action='store_true',default=False,help='show count lines')

    option,args=parse.parse_args()
    return option,args

def getwc(file):
    char=len(file)
    word=len(file.split())
    line=file.count('\n')
    return char, word, line

def printwc(option,char,word,line,fn):
    if option.char:
        print char,
    if option.word:
        print word,
    if option.line:
        print line,
    print fn
    
def main():
    option,args=opt()
    #print option,args
    if not (option.char or option.word or option.line):
        option.char,option.word,option.line=True,True,True

    if args:
        total_char=0
        total_word=0
        total_line=0
        for fn in args:
            if os.path.isfile(fn):
                with open(fn) as fd:
                    file=fd.read()
                    char,word,line=getwc(file)
                    printwc(option,char,word,line,fn)
                    total_char+=char
                    total_word+=word
                    total_line+=line
            elif os.path.isdir(fn):
                print >> sys.stderr,'%s: Is a directory' %fn
            else:
                print >> sys.stderr,'%s: No such file or directory' %fn
        if len(args)>1:
            printwc(option,total_char,total_word,total_line,'total')
    else:
        fn=''
        file=sys.stdin.read()
        char,word,line=getwc(file)
        printwc(option,char,word,line,fn)   

if __name__ == '__main__':
    main()
