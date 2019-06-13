#!/usr/bin/env python
# coding=utf-8

import os, re

fp = open(r"D:\video2\alita.mp4",'wb+')
for i in range(1000,1999):
    s = r"D:\video2\399" + str(i) + ".ts"
    f1 = open(s,'rb')
    fp.write(f1.read())
    fp.flush()

for i in range(1000,1775):
    s = r"D:\video2\3991" + str(i) + ".ts"
    f1 = open(s,'rb')
    fp.write(f1.read())
    fp.flush()

fp.close()