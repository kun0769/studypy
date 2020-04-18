#!/usr/bin/env python
#coding:utf8
#
#program:
#    使用multiprocessing模块和paramiko模块实现多台机器并行执行命令
#    使用multiprocessing.Pool方法来实现多进程让多个CPU同时处理命令
#    使用optparse模块优化脚本使用参数执行ip地址
#    Python 脚本.py -a ip地址 命令
#    支持分号 192.168.161.100,192.168.161.101
#    支持破折号 192.168.161.100-192.168.161.200
#
#history:
#2020/04/18    kun    V1.0

import optparse
import multiprocessing
import paramiko
import sys

# 自定义参数-a模块
def opt():
    #实例化parse对象
    parse=optparse.OptionParser("Usage: %prog -a addr command")
    parse.add_option("-a",dest="addr",action="store",help="ip or iprange Ex:192.168.161.1,192.168.161.3 or 192.168.161.1-192.168.161.100")
    options,args=parse.parse_args()
    return options,args

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

#接收ip地址解析它们
def parseIP(option):
    if ',' in option:
        ips=option.split(',')
        return ips
    elif '-' in option:
        ipStart,ipEnd=option.split('-')
        start=int(ipStart.split('.')[-1])
        end=int(ipEnd.split('.')[-1])+1
        ipNet='.'.join(ipStart.split('.')[:-1])
        ips=[ ipNet+'.'+str(i) for i in xrange(start,end)]
        return ips
    elif ',' not in option or '-' not in option:
        ips=[option]
        return ips
    else:
        print "%s -h" % __file__


if __name__=="__main__":
    #记录日志
    paramiko.util.log_to_file("/tmp/paramiko.log")

    #创建两个变量接收opt函数返回值
    options,args=opt()

    if options.addr:
        #把-a后的IP地址给parseIP接收解析对应的IP段
        ips=parseIP(options.addr)
    else:
        print "%s -h" % __file__
        sys.exit(1)

    #创建multipeocessing.Pool对象 开启10个进程
    pool=multiprocessing.Pool(processes=10)

    try:
        cmd=args[0]
    except IndexError:
        print "%s need to follow a command" % __file__
        sys.exit(1)

    #向进程池中提交IP地址
    for ip in ips:
        pool.apply_async(func=sshFun,args=(ip,cmd))

    pool.close()
    #阻塞主进程(脚本本身)
    pool.join()
