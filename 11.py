#!/usr/bin/env python

def fun():
    string=raw_input('Please input one number:')
    try:
        if type(int(string))==type(int(1)):
            print '%s is number...' %string
    except ValueError:
            print '%s is not number...' %string

fun()
