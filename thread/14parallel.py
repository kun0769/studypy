#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用threading模块和paramiko模块实现多台机器并行执行命令
#
#history:
#2020/04/15    kun    V1.0

import threading
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
    ips=["192.168.161.100","192.168.161.101","192.168.161.102"]
    try:
        cmd=sys.argv[1]
    except IndexError:
        print "%s need to follow a command" % __file__
        sys.exit(1)
    for ip in ips:
        t=threading.Thread(target=sshFun,args=(ip,cmd))
        t.start()
        t.join()
