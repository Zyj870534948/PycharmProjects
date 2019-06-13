#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''
import os
import time

# os.system('ps -ef | grep "arecord.py" | grep -v grep | awk "{print $2}"')
time.sleep(5)
os.system('ps -ef|grep "arecord.py"|grep -v grep|awk "{print $2}"|xargs kill -9 ')
