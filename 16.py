#!/usr/bin/env python
#coding:utf8

class People(object):
    color="yellow"
    __age=30

    def think(self):
        self.color="black"
        print "I am a %s man" %self.color
        print self.__age


kun=People()

kun.think()
print kun.color
print kun.__dict__
print People.__dict__

        
