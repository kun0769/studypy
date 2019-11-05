#!/usr/bin/env python

mac='00:0c:29:bf:21:01'
mac_prefix=mac[:-3]
mac_suffix=mac[-2:]
mac_suffix1=int(mac_suffix,16)+1

if mac_suffix1 in range(10):
    new_mac_suffix='0'+hex(mac_suffix1)[2:]
else:
    new_mac_suffix=hex(mac_suffix1)[2:]
    if len(new_mac_suffix)==1:
        new_mac_suffix='0'+hex(mac_suffix1)[-1:]

print mac_prefix+':'+new_mac_suffix.upper()
