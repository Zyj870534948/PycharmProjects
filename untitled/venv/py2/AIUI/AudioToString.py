#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import time
import json
import base64
import hashlib
import requests
import urllib

apiKey = "642cfe74c65d25412baa0dff327ee45c"     #b8d94d4c771f80c5bb5f96bfd2186f88
appid = "5cab19c9"      #5ca57271
curTime = str(int(time.time()))

js = {
    "engine_type": "sms16k",
    "aue": "raw"
}

param = str(base64.b64encode(json.dumps(js),'utf-8'))

m2 = hashlib.md5()
m2.update((apiKey+curTime+param).encode('utf-8'))
checkSum = m2.hexdigest()

header = {
    "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
    "X-Appid":appid,
    "X-CurTime":curTime,
    "X-Param":param,
    "X-CheckSum":str(checkSum)
}

f = open(r"C:\Users\N-pod\out.wav","rb")
a = f.read()

print "1"
# print base64.b64encode(a,'utf-8')

print "2"
# print urllib.quote(base64.b64encode(a,'utf-8'))

body = {
    "audio":urllib.quote(base64.b64encode(a,'utf-8'))
}
print "3",
re = requests.post(url="http://api.xfyun.cn/v1/service/v1/iat",headers=header,data=body)

print re.text