#!/usr/bin/env python
#coding:utf8

def h():
    print 'one'
    yield 1
    print 'two'
    yield 2
    print 'three'
    yield 3

#h()函数返回的是生成器对象，需要通过next方法来获得值
#先赋值给a变量，再执行next方法
a=h()
for i in a:
    print i
