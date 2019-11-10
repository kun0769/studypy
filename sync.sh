#!/bin/bash
#
#program:
#
#    判断当前目录的host/host.conf与/etc/nagois/conf.d/host/host.conf是否一致
#    再复制最新的配置文件到/etc/nagois/conf.d/host/host.conf中
#
#history:
#2019/11/10    kun    V1.0

cur=`dirname $0`
cd $cur
python gen.py
cur_md5=`find host/ -type f -exec md5sum {} \;|md5sum`
cd /etc/nagios/conf.d/
host_md5=`find host/ -type f -exec md5sum {} \;|md5sum`

#比较当前host/host.conf和/etc/nagois/conf.d/host/host.conf的字符串是否一致
if [ "$host_md5" != "$cur_md5" ];then
    cd -
    \cp -af host/ /etc/nagios/conf.d/
    systemctl restart nagios
fi
