#!/usr/bin/env python
#coding:utf8
#
#program:
#    判断密码是否正确
#
#history:
#2019/11/26    kun    V1.0

import getpass

def check_pass(user,password):
    if user=='kun' and password=='123456':
        return True
    else:
        return False

if __name__=='__main__':
    user=getpass.getuser()
    password=getpass.getpass('Please input password:')
    if check_pass(user,password):
        print 'OK!'
    else:
        print 'Error!'
