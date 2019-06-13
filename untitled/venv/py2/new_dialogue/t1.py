#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import time
import os

for i in range(20):
    time.sleep(0.1)
    print "1"

t = time.clock()
os.system(r"python D:\GitHub\PycharmProjects\untitled\venv\py2\new_dialogue\t2.py")
print time.clock() - t

for i in range(20):
    time.sleep(0.1)
    print "2"

