#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用multiprocessing模块和paramiko模块实现多台机器并行执行命令
#    使用multiprocessing.Pool方法来实现多进程让多个CPU同时处理命令
#
#history:
#2020/04/18    kun    V1.0

import multiprocessing
import paramiko
import sys

def sshFun(ip,cmd):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey_file="/home/kun/.ssh/id_rsa"
    key=paramiko.RSAKey.from_private_key_file(pkey_file)
    try:
        ssh.connect(hostname=ip,username="root",pkey=key,timeout=3)
    except:
        print "%s: Timeout or not permission" % ip
        return 1
    stdin,stdout,stderr=ssh.exec_command(cmd)
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

    #创建multiprocessing.Pool对象 开启是个进程
    pool=multiprocessing.Pool(processes=10)

    try:
        cmd=sys.argv[1]
    except IndexError:
        print "%s need to follow a command" % __file__
        sys.exit(1)

    #向进程池中提交IP地址
    for ip in ips:
        pool.apply_async(func=sshFun,args=(ip,cmd))

    pool.close()
    #阻塞主进程(脚本本身)
    pool.join()
