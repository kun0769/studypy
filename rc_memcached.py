#!/usr/bin/env python
#coding:utf-8

from subprocess import Popen, PIPE   ##插入subprocess包两个模块 用于执行命令
import os
import sys

class Process(object):
    
    def __init__(self, name, program, args, workdir):  #实例化自动加载该方法 name命令名字 program 执行文件路径
        self.name = name                               #args 命令带的参数 workdir PID目录
        self.program = program                         #类的属性接受参数
        self.args = args
        self.workdir = workdir

#'''  自定义初始化方法 '''   
    def pidDir(self):
        if not os.path.exists(self.workdir):     ##判断自定义的PID目录var/tmp/memcached不存在，并创建进入该目录
            os.mkdir(self.workdir)
            os.chdir(self.workdir) 

#'''  创建memcached的PID文件 '''
    def pidFile(self):                             ##返回memcachedPID的文件路径 var/tmp/memcached/memcached.pid
        return os.path.join(self.workdir,'%s.pid' %self.name)

#'''  把PID的数值写入PID文件中 '''
    def writePid(self):
        if self.pid:                               #判断pid存在并把pid写入var/tmp/memcached/memcached.pid中
            with open(self.pidFile(),'w') as fd:
                fd.write(str(self.pid))

#'''  定义start方法 '''
    def start(self):
        pid = self.getPid()
        if pid:
            print '%s 已经在跑了...' %self.name      #进程已经有了再此运行start会退出
            sys.exit()
        self.pidDir()                                #调用pidDir方法创建目录
        cmd = self.program + ' ' + self.args
        p = Popen(cmd, stdout=PIPE, shell=True)      #命令通过管道输出
        self.pid = p.pid                             #得到pid数值并定义对象公有属性 让weiterPid方法可以调用 
        self.writePid()                              #调用writePid方法
        print '%s 启动成功...' %self.name

#''' 获得memcached的pid '''
    def getPid(self):
        p = Popen(['pidof',self.name],stdout=PIPE)   #获得pidof memcached命令来得到pid
        pid = p.stdout.read().strip()                #strip()去\n
        return pid

#'''  定义stop方法 '''
    def stop(self):
        pid = self.getPid()                               #调用getPid方法获取pid
        if pid:
            os.kill(int(pid), 15)                         #pid存在就傻掉pid
            if os.path.exists(self.pidFile()):            #再删除/tmp/memcached/memcached.pid
                os.remove(self.pidFile())
            print '%s 正在关闭...' %self.name

#'''  定义restart方法 '''
    def restart(self):
        self.stop()
        self.start()

#'''  定义status方法 '''
    def status(self):
        pid =self.getPid()
        if pid:
            print '%s 已经在运行中...' %self.name
        else:
            print '%s 没有运行...' %self.name

#'''  定义status方法  '''
    def helps(self):
        print '你可以按以下格式输入 %s {start|stop|restart|status}' %__file__ #__file__表示脚本本身

def main():       ##定义一个主函数
    
    name = 'memcached'
    prog = '/usr/bin/memcached'
    args = '-u nobody -p 11211 -c 1024 -m 64'
    wd = '/var/tmp/memcached'
    pm = Process(name = name, program = prog, args = args, workdir = wd)   ##实例化对象 并传参
    
    try:                   ##抓取脚本后是否带上选项,没有退出
        cmd = sys.argv[1]
    except IndexError:
        print '没有带上选项'
        sys.exit()

    if cmd == 'start':     ##判断选项来调用对象对应的方法
        pm.start()

    elif cmd == 'stop':
        pm.stop()

    elif cmd == 'restart': 
        pm.restart()

    elif cmd == 'status':
        pm.status()

    else:
        pm.helps()


if __name__ == '__main__':   ##当自己执行自己会调用主函数 当被其他脚本作为模块时就不调用主函数
    main()
