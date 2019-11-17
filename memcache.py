#!/usr/bin/env python
#coding:utf8
#
#program:
#    启停memcache脚本

import sys
import os
from subprocess import Popen, PIPE

class Process(object):
    
    def __init__(self,name,program,args,workdir):
        self.name=name
        self.program=program
        self.args=args
        self.workdir=workdir

    def _init(self):
        if not os.path.exists(self.workdir):
            os.mkdir(self.workdir)
            os.chdir(self.workdir)

    def _pidFile(self):
        return os.path.join(self.workdir,'%s.pid' %self.name)

    def _writePid(self):
        if self.pid:
            with open(self._pidFile(),'w') as fd:
                fd.write(str(self.pid))

    def start(self):
        pid=self._getPid()
        if pid:
            print "Warming:%s is running..." %self.name
            sys.exit()
        self._init() #创建pid目录
        cmd=self.program+' '+self.args
        p=Popen(cmd,stdout=PIPE,shell=True)  #执行memcached命令
        self.pid=p.pid
        self._writePid()  #写入pid
        print "%s start sucessful..." %self.name

    def _getPid(self):
        p=Popen(['pidof',self.name],stdout=PIPE)
        pid=p.stdout.read().strip()
        return pid

    def stop(self):
        pid=self._getPid()
        if pid:
            os.kill(int(pid),15)
            if os.path.exists(self._pidFile()):
                os.remove(self._pidFile())
            print "%s is stopped..." %self.name

    def reload(self):
        self.stop()
        self.start()

    def status(self):
        pid=self._getPid()
        if pid:
            print "%s is running..." %self.name
        else:
            print "%s is not running..." %self.name

    def help(self):
        print "Usage: %s [start|stop|status|reload]" %__file__

def Main():
    name='memcached'
    program='/usr/bin/memcached'
    args='-u nobody -p 11211 -c 1024 -m 64'
    workdir='/var/tmp/memcached'
    pm=Process(name=name,program=program,args=args,workdir=workdir)

    try:
        cmd=sys.argv[1]
    except IndexError, e:
        print "Option Error"
        sys.exit()

    if cmd=='start':
        pm.start()
    elif cmd=='stop':
        pm.stop()
    elif cmd=='reload':
        pm.reload()
    elif cmd=='status':
        pm.status()
    else:
        pm.help()

if __name__=='__main__':
    Main()
