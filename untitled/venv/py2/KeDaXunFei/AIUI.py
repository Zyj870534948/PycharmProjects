#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''
#-*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import httplib as client
import json

URL = "https://openapi.xfyun.cn/v2/aiui"
APPID = "5cab19c9"
API_KEY = "0c58bdfdb06a871af662eed5d9250aac"

def getHeader():


    conn = client.HTTPConnection("www.baidu.com")
    conn.request("GET", "/")
    r = conn.getresponse()
    ts = r.getheader('date')
    local_time = time.mktime(time.strptime(ts[5:], "%d %b %Y %H:%M:%S GMT")) + (8 * 60 * 60)    #通过世界时间计算北京时间

    curTime = str(int(local_time))             #本机所在地的时间戳
    param = "{\"result_level\":\"complete\",\"auth_id\":\"c104d15777ab2486dcc45698c209d47f\",\"data_type\":\"text\",\"scene\":\"main\"}"
    paramBase64 = base64.b64encode(param)   #base64加码

    m2 = hashlib.md5()  #md5哈希值加密计算
    m2.update(API_KEY + curTime + paramBase64)
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
    }   #配置头文件
    # print header
    return header

def getBody(filepath):
    binfile = open(filepath, 'rb')
    data = binfile.read()
    return data

r = requests.post(URL, headers=getHeader(), data="醉翁亭记")    #详细看AIUI文档
text = r.content
text = json.loads(text)     #字符串转字典
text = text["data"][0]["intent"]["answer"]["text"].encode("utf-8")      #获取文字后将unicode格式的文字转化为utf-8格式

for i in range(11):     #消除所有多余的[ki]字符串
    text = text.replace('[k' + str(i) + ']', '')

print(text)