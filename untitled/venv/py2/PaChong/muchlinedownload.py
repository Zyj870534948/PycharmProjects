#!/usr/bin/env python
# coding=utf-8

from requests import get
from requests import post
import time
import json
import os, re
import _thread

urlstar = "https://fuli.zuida-youku-le.com/20181006/34275_29c69316/800k/hls/ce388441306000.ts"
urlend = "https://fuli.zuida-youku-le.com/20181006/34275_29c69316/800k/hls/ce388441306713.ts"


def download(url):
    request = get(url)
    if request.text[0]=="<" and request.text[1] == "h":
        return False
    else:
        return request


def alld(nub):
    name = nub
    f = open("D:\\pythondownload\\try\\" + name + ".ts", 'wb')
    url = "https://fuli.zuida-youku-le.com/20181006/34275_29c69316/800k/hls/ce38844130" + nub + ".ts"
    request = download(url)
    for chunk in request.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
    f.close()
    print(nub + " is OK")

n = 6350
m = n + 100
try:
   while n != m:
       _thread.start_new_thread( alld, (str(n) ,))
       n += 1
       if n >6713:
           break
except:
   print ("Error: 无法启动线程")

while 1:
   pass
