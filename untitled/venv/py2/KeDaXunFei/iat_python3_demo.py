# -*- coding: utf-8 -*-

import requests
import time
import hashlib
import base64,json

URL = "http://api.xfyun.cn/v1/service/v1/iat"
APPID = "5cab19c9"

API_KEY = "642cfe74c65d25412baa0dff327ee45c"

def getHeader(aue, engineType):
    curTime = str(int(time.time()))

    param = "{\"aue\":\"" + aue + "\"" + ",\"engine_type\":\"" + engineType + "\"}"
    print("param:{}".format(param))
    paramBase64 = str(base64.b64encode(param.encode('utf-8')))
    print("x_param:{}".format(paramBase64))
    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
    checkSum = m2.hexdigest()
    print('checkSum:{}'.format(checkSum))

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    print(header)
    return header


def getBody(filepath):
    binfile = open(filepath, 'rb')
    data = {'audio': base64.b64encode(binfile.read())}
    print(data)
    print('data:{}'.format(type(data['audio'])))
    return data


aue = "raw"
engineType = "sms16k"
audioFilePath = r"C:\Users\N-pod\out2.wav"
r = requests.post(URL, headers=getHeader(aue, engineType), data=getBody(audioFilePath))
s = r.content.decode('utf-8')
print(s)
s = json.loads(s)
print s["data"]

f = "你"
print(len(f),len(s["data"]),len(s["data"].encode("utf-8")))
