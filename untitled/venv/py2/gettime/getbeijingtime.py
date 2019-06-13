#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import time
import httplib
import logging

import httplib as client
import time
import os
def get_webservertime(host):
    conn=client.HTTPConnection(host)
    conn.request("GET", "/")
    r=conn.getresponse()
    ts=  r.getheader('date') #获取http头date部分
                             #将GMT时间转换成北京时间
    local_time= time.mktime(time.strptime(ts[5:], "%d %b %Y %H:%M:%S GMT")) + (8 * 60 * 60)
    # ltime = time.gmtime(local_time)
    #                          #使用date设置时间
    # dat = 'date -u -s "%d-%d-%d %d:%d:%d" ' % (ltime.tm_year,ltime.tm_mon,ltime.tm_mday,ltime.tm_hour,ltime.tm_min,ltime.tm_sec)
    # # os.system(dat)
    return local_time

print int(get_webservertime('www.baidu.com'))
print int(time.time())
print int(get_webservertime('www.baidu.com')) - int(time.time())
# print getBeijinTime()