#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

# encoding:utf-8
import urllib, urllib2, sys,json,base64
import ssl
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=i01HkFlrkXULjCYIf7EVGqjn&client_secret=CDQseU9rGDmH6rgx1qDTlH0iXIQl36dX'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    content = json.loads(content)
    print(content["access_token"])

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

f1 = open("./towface.jpg","rb")
img1 = base64.b64encode(f1.read())
f1 = open("./003.jpg","rb")
img2 = base64.b64encode(f1.read())
# print img2

params = json.dumps(
    [{"image": img1, "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
     {"image": img2, "image_type": "BASE64", "face_type": "IDCARD", "quality_control": "LOW"}])

access_token = content["access_token"]
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print json.loads(content),json.loads(content)["cached"],type(json.loads(content)["result"]["score"])


#对比度  json.loads(content)["result"]["score"]
#成功 json.loads(content)["cached"]