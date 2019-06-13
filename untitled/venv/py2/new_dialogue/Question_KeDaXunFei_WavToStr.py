#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__
在科大讯飞设置好IP白名单后才能运行成功
'''

import requests
import time
import hashlib
import base64,json
import httplib as client

class KeDaXunFei:

    #科大讯飞AIUI的接口信息 默认音频编码（wav）和引擎类型（sms16k）
    def __init__(self, APPID="5cab19c9", API_KEY="642cfe74c65d25412baa0dff327ee45c" ,aue = "raw" ,engineType = "sms16k"):
        self.URL = "http://api.xfyun.cn/v1/service/v1/iat"
        self.APPID = APPID
        self.API_KEY = API_KEY

        self.aue = aue
        self.engineType = engineType



    #设置头文件
    def getHeader(self ,aue, engineType):

        # 通过百度获取世界时间来计算北京时间（机器人本机时间可能会无法获取网络时间）
        conn = client.HTTPConnection("www.baidu.com")
        conn.request("GET", "/")
        r = conn.getresponse()
        ts = r.getheader('date')
        local_time = time.mktime(time.strptime(ts[5:], "%d %b %Y %H:%M:%S GMT")) + (8 * 60 * 60)

        ##本机时间戳
        # curTime = str(int(time.time()))
        # 计算所得的时间戳为本机所在地的时间戳
        curTime = str(int(local_time))

        param = "{\"aue\":\"" + aue + "\"" + ",\"engine_type\":\"" + engineType + "\"}"
        # print("param:{}".format(param))
        paramBase64 = str(base64.b64encode(param.encode('utf-8')))
        # print("x_param:{}".format(paramBase64))
        m2 = hashlib.md5()
        m2.update((self.API_KEY + curTime + paramBase64).encode('utf-8'))
        checkSum = m2.hexdigest()
        # print('checkSum:{}'.format(checkSum))

        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': self.APPID,
            'X-CheckSum': checkSum,
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        # print(header)
        return header


    def getBody(self ,filepath):
        binfile = open(filepath, 'rb')
        data = {'audio': base64.b64encode(binfile.read())}
        # print(data)
        # print('data:{}'.format(type(data['audio'])))
        return data


    def getStr(self ,audioFilePath):        #传入音频位置
        r = requests.post(self.URL, headers=self.getHeader(self.aue, self.engineType), data=self.getBody(audioFilePath))
        s = r.content.decode('utf-8')
        # print(s)
        s = json.loads(s)
        return s["data"].encode("utf-8")

if __name__ == '__main__':
    audioFilePath = r"C:\Users\N-pod\out2.wav"
    Q = KeDaXunFei()
    print Q.getStr(audioFilePath)