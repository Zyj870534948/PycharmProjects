#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import urllib2
import json
import base64
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'http://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=74kEsjZ4G9j7WjGOPC123oS2&client_secret=501VUQmzNUpUGXUUQukH5x1OP3rkPHvV'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()

# body = {}
# header = {'Content-Type': 'application/x-www-form-urlencoded'}
# content = requests.post(url=host,data=body,headers=header)
# content = json.loads(content.text)

content = json.loads(content)

access_token = content["access_token"]

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/search"

request_url = request_url + "?access_token=" + access_token

locpath = ""
f1 = open(r"C:\Users\N-pod\Desktop\book.jpg","rb")
img1 = base64.b64encode(f1.read())

body = {"image": img1}
header = {'Content-Type':'application/x-www-form-urlencoded'}
content = requests.post(url=request_url,data=body,headers=header)
content = json.loads(content.text)

print(content)

try:
    print content["result"][0]["brief"].encode("utf-8")
except:
    print "未找到"

# print(content)
print(content["result"][0]["score"])
print(content["result"][0]["brief"])