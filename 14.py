#!/usr/bin/env python
#
#函数的递归 计算阶层

def fun(n):
    if n==0:
        return 1
    else:
        return n*fun(n-1)

print fun(5)
