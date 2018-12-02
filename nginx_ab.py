#!/usr/bin/python
# coding:utf-8

import sys

class Class(object):

    a = '10.0.0.'
    b = '192.168.0.'

    def __init__(self,nc):
        self.nc = nc
    
    def shang(self,ip):           #去#
        new_lines = ''
        with open(self.nc,'r') as f:
            lines = f.readlines()
            for i in lines:
                if ip in i:
                    n = i.strip('#')
                    i = i.replace(i,n)
                    print(i)
                new_lines += i
        with open(self.nc, 'w') as d:
             d.write(new_lines)


    def xia(self,ip):            #加上#
        new_lines = ''
        with open(self.nc,'r') as f:
            lines = f.readlines()
            for i in lines:
                if ip in i:
                    n = '#'+i
                    i = i.replace(i,n)
                    print(i)
                new_lines += i
        with open(self.nc, 'w') as d:
             d.write(new_lines)


    def xuanA(self):
        self.shang(self.a)

    def xuanB(self):
        self.xia(self.a)

    def xuanC(self):
        self.shang(self.b)

    def xuanD(self):
        self.xia(self.b)

def main():
    cmd = input('A.将A组切上去\nB.将A组切下来\nC.将B组切上去\nD.将B组切下来\nE.重启Nginx服务\nF.完成迭代\nG.更新代码\n请输入：')

    nginx_conf = '/root/111.txt'
    cm = Class(nc=nginx_conf)

    if cmd == 'A':
        cm.xuanA()

    elif cmd == 'B':
        cm.xuanB()

    elif cmd == 'C':
        cm.xuanC()

    elif cmd == 'D':
        cm.xuanD()

    elif cmd == 'E':
        print('重启Nginx服务')
    elif cmd == 'F':
        print('完成迭代')
    elif cmd == 'G':
        print('更新代码')
    else:
        print('你输入格式错误！')
        sys.exit()

if __name__ == '__main__':
    main()
