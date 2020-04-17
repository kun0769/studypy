#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用threading模块和paramiko模块实现多台机器并行执行命令
#    使用Queue模块 一边生产ip 另一边连接ip执行命令
#    重写threading.Thread的run方法定义生产和消费模型
#    使用线程锁lock来控制线程
#
#history:
#2020/04/17    kun    V1.0

import threading
import paramiko
import sys
import Queue

#生产ip,把ip地址放在队列中
class produceIP(threading.Thread):
    def __init__(self,ips,queue):
        threading.Thread.__init__(self)
        self.queue=queue
        self.ips=ips

    def run(self):
        for ip in self.ips:
            self.queue.put(ip)

#消费ip 把ip从队列中拿出来并远程执行命令
class consumeIP(threading.Thread):
    def __init__(self,cmd,queue):
        threading.Thread.__init__(self)
        self.queue=queue
        self.cmd=cmd
    
    def run(self):
        try:
            lock.acquire()
            ip=self.queue.get(1,5)
            self.sshFun(ip)
            lock.release()
        except:
            return 

    def sshFun(self,ip):
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pkey_file="/home/kun/.ssh/id_rsa"
        key=paramiko.RSAKey.from_private_key_file(pkey_file)
        try:
            ssh.connect(hostname=ip,username="root",pkey=key,timeout=3)
        except:
            print "%s: Timeout or not permission" % ip
            return 1
        stdin,stdout,stderr=ssh.exec_command(self.cmd)
        stdout=stdout.read()
        stderr=stderr.read()
        if stdout:
            print "%s:\t%s" %(ip,stdout)
            ssh.close()
        else:
            print "%s:\t%s" %(ip,stderr)
            ssh.close()

if __name__=="__main__":
    #记录日志
    paramiko.util.log_to_file("/tmp/paramiko.log")
    #192.168.161.1~192.168.161.100
    ips=[ "192.168.161."+str(i) for i in xrange(1,101)]
    #创建队列对象和锁对象
    queue=Queue.Queue(2)
    lock=threading.Lock()

    try:
        cmd=sys.argv[1]
    except IndexError:
        print "%s need to follow a command" % __file__
        sys.exit(1)

    #创建一个线程生产ip
    t1=produceIP(ips,queue)
    t1.start()

    #创建100个线程消费ip执行远程命令
    for i in xrange(len(ips)):
        t2=consumeIP(cmd,queue)
        t2.start()
