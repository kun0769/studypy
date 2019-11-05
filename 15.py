#!/usr/bin/env python
#coding=utf-8
#
#递归目录下的文件 find . -type f

import os
import sys

def findFile(path):
    dir=[ i for i in os.listdir(path) if os.path.isdir(os.path.join(path,i)) ]
    file=[ i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) ]
    
    if dir:
        for d in dir:
            findFile(os.path.join(path,d))

    if file:
        for f in file:
            print os.path.join(path,f)


findFile(sys.argv[1])
