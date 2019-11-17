#!/usr/bin/python

dic={}
name=raw_input("Please input you name:")
age=raw_input("Please input you age:")
gender=raw_input("Please input you gender(M/F):")

dic['name']=name
dic['age']=age
dic['gender']=gender

for k,v in dic.items():
    print "%s: %s" %(k,v)
