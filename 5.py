#!/usr/bin/python

import random

num=random.randint(1,20)

for i in xrange(6):
    n1=input("Please input one number:")
    if n1 > num:
        print "too big..."
    elif n1 < num:
        print "too small..."
    else:
        print "you are rigth..."
        break
    print "you has %s times chance" %(5-i)
else:
    print "sorry, you are lose..."
