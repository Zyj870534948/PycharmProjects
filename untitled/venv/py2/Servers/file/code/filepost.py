#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import requests
import base64
import json


'''
filePath = r'C:\Users\Administrator\Desktop\005.txt'
n = 0
name = ''
for i in range(len(filePath)-1,-1,-1):
    if filePath[i] == "\\" or filePath[i] == "/":
        n = i
        break
n += 1
for i in range(n,len(filePath)):
    name += filePath[i]


f = open(filePath,'rb')

# files = {"img":open(r'C:\Users\Administrator\Desktop\005.jpg','rb')}
t2 = f.read()
t = base64.b64encode(t2)     #编码
t3 = base64.b64decode(t)     #解码

filedata = {"body":t,
            "name":name,
            "instructions":"1",
            "THdata":""}

rep1 = requests.post(url="http://192.168.3.21:11111/getfile",data=filedata )
# rep2 = requests.post(url="http://192.168.3.16:11111/controlppt",data=filedata )
'''

# data = {"services":"conversation.process","text":"关闭小米台灯"}
# # data = json.dumps(data)
# # rep1 = requests.get('http://192.168.3.27:8123/frontend_latest/3379eef44a1b08bf6356.chunk.js',data)
#
# filedata ={"date":"open",
#            "cmd":"people_come_in",
#            "instructions":"2"}
# # headers={'accept':'application/json'}
# # filedata = json.dumps(filedata)
#
# # rep1 = requests.post(url="http://192.168.3.5:11111/HAapi",headers=headers,data=filedata )
# rep1 = requests.post(url="http://192.168.3.5:11111/controlppt",data=filedata )
# print rep1

# rep1 = requests.post('http://192.168.3.5:11111/photofaces')
rep1 = requests.get('http://192.168.3.5:11111/faces')
data = rep1.text
print data
