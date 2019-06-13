#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"njj"

import urllib, urllib2, sys
import ssl
import json
import base64

 # client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=rdgzB4UQDLXMVgLyN6etijfm&client_secret=Ymsvjr5gDhbtW712ZKBVQQFXk1jLojhb'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
content = json.loads(content)

access_token = content["access_token"]

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

request_url = request_url + "?access_token=" + access_token


imgpath = "./"
locpath = "./"
facedic = {
    "VIP1":"崔翔",
    "VIP2":"陈冠希",
    "FV1":"倪佳俊",
    "FV2":"吴彦祖",
}
Vcon = 2
Fcon = 2

f1 = open(imgpath + "image.jpg","rb")
img1 = base64.b64encode(f1.read())

flag = 1

for i in range(1,Vcon+1):
    try:
        f1 = open(locpath + "VIP" + str(i) + ".jpg","rb")
        img2 = base64.b64encode(f1.read())
        params = json.dumps(
            [{"image": img1, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
             {"image": img2, "image_type": "BASE64", "face_type": "IDCARD", "quality_control": "LOW"}])
        request = urllib2.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(request)
        content = response.read()
        content = json.loads(content)

        try:
            if content["result"]["score"] > 80:
                print "尊敬的VIP用户" + facedic["VIP" + str(i)] + "你好"
                flag = 2
        except:
            pass
    except:
        pass

for i in range(1, Fcon + 1):
    try:
        f1 = open(locpath + "FV" + str(i) + ".jpg", "rb")
        img2 = base64.b64encode(f1.read())
        params = json.dumps(
            [{"image": img1, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
             {"image": img2, "image_type": "BASE64", "face_type": "IDCARD", "quality_control": "LOW"}])
        request = urllib2.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(request)
        content = response.read()
        content = json.loads(content)

        try:
            if content["result"]["score"] > 80:
                print "尊敬用户" + facedic["FV" + str(i)] + "你好"
                flag = 3
        except:
            pass
    except:
        pass


if flag == 1:
    print "尊敬顾客你好"