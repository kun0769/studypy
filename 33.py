#!/usr/bin/env python

class FuncErr(Exception):
    def __str__(self):
        return 'I am Error...'

def fun():
    raise FuncErr()

try:
    fun()
except FuncErr,e:
    print e
