#!/usr/bin/env python
#coding:utf8
#
#program:
#    启停memcache脚本(使用-d 守护进程) 可根据配置文件来配置端口等信息

import sys
import os
from subprocess import Popen, PIPE

class Process(object):

    args={'USER':'memcached',
          'PORT':11211,
          'MAXCONN':1024,
          'CACHESIZE':64,
          'OPTIONS':''}

    def __init__(self,name,program,workdir):
        self.name=name
        self.program=program
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

    #读取配置文件的参数 返回字典
    def _readConfig(self,f):
        with open(f) as fd:
            line=fd.readlines()
            return dict([i.strip().replace('"','').split('=') for i in line])

    #配置文件参数替换默认定义的参数,返回列表       
    def _diffconfig(self):
        conf=self._readConfig('/etc/sysconfig/memcached')
        if 'USER' in conf:
            self.args['USER']=conf['USER']
        if 'PORT' in conf:
            self.args['PORT']=conf['PORT']
        if 'MAXCONN' in conf:
            self.args['MAXCONN']=conf['MAXCONN']
        if 'CACHESIZE' in conf:
            self.args['CACHESIZE']=conf['CACHESIZE']

        options=['-u',self.args['USER'],
                '-p',self.args['PORT'],
                '-m',self.args['MAXCONN'],
                '-c',self.args['CACHESIZE']]
     
        os.system('chown %s %s' %(self.args['USER'], self.workdir))
        return options

    def start(self):
        pid=self._getPid()
        if pid:
            print "Warming:%s is running..." %self.name
            sys.exit()
        self._init() #创建pid目录
        cmd=[self.program]+self._diffconfig()+['-d','-P',self._pidFile()]
        print cmd
        p=Popen(cmd,stdout=PIPE)  #执行memcached命令
        #self.pid=p.pid
        #self._writePid()  #写入pid
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
    workdir='/var/tmp/memcached'
    pm=Process(name=name,program=program,workdir=workdir)

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
