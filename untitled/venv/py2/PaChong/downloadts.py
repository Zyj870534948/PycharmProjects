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

name = "刀剑圣域3_01"
fp = open("D:\\pythondownload\\" + name + ".mp4",'wb+')
for i in range(6000,6714):
    url = "https://fuli.zuida-youku-le.com/20181006/34275_29c69316/800k/hls/ce38844130" + str(i) + ".ts"
    request = download(url)
    if request:
        for chunk in request.iter_content(chunk_size=1024):
            if chunk:
                fp.write(chunk)
        fp.flush()
        print(i-5999,"/",714)
print("OK")
