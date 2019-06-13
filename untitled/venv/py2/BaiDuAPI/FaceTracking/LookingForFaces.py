#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''
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

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

request_url = request_url + "?access_token=" + access_token

f1 = open("./image.jpg","rb")
img = base64.b64encode(f1.read())

params = json.dumps({"image":img,
                     "image_type":"BASE64",
                     "face_field":"location,expression,type,gender"})

request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request)
content = response.read()
content = json.loads(content)

print type(content["result"]["face_list"][0]["gender"]["type"])
