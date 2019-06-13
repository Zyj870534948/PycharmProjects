#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import requests
import time
import hashlib
import base64
import httplib as client
import json
from Question_KeDaXunFei_WavToStr import KeDaXunFei

class AIUI:

    #科大讯飞AIUI的接口信息
    def __init__(self ,APPID="5cab19c9" ,API_KEY="0c58bdfdb06a871af662eed5d9250aac"):
        self.URL = "http://openapi.xfyun.cn/v2/aiui"
        self.APPID = APPID
        self.API_KEY = API_KEY

    # 设置头文件
    def getHeader(self):

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

        param = "{\"result_level\":\"complete\",\"auth_id\":\"c104d15777ab2486dcc45698c209d47f\",\"data_type\":\"text\",\"scene\":\"main\"}"
        paramBase64 = base64.b64encode(param)   #base64加码

        m2 = hashlib.md5()  #md5哈希值加密计算
        m2.update(self.API_KEY + curTime + paramBase64)
        checkSum = m2.hexdigest()

        # 配置头文件
        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': self.APPID,
            'X-CheckSum': checkSum,
        }
        # print header
        return header

    ##如果需要可获取文本提问
    # def getBody(self ,filepath):
    #     binfile = open(filepath, 'rb')
    #     data = binfile.read()
    #     return data

    def getAnswer(self ,question):      #传入问题 返回回答
        r = requests.post(self.URL, headers=self.getHeader(), data=question)    #详细看AIUI文档
        text = r.content
        text = json.loads(text)     #字符串转字典
        text = text["data"][0]["intent"]["answer"]["text"].encode("utf-8")      #获取文字后将unicode格式的文字转化为utf-8格式

        for i in range(11):     #消除所有多余的[ki]字符串
            text = text.replace('[k' + str(i) + ']', '')

        return text

#测试
if __name__ == '__main__':
    A = AIUI()
    Q = KeDaXunFei()
    print A.getAnswer(Q.getStr(r"C:\Users\N-pod\out2.wav"))