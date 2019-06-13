#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

from requests import get
from requests import post
import time
import urllib, urllib2, sys
import ssl
import json
import base64
import time
import requests
import urllib2


host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=rdgzB4UQDLXMVgLyN6etijfm&client_secret=Ymsvjr5gDhbtW712ZKBVQQFXk1jLojhb'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
content = json.loads(content)

access_token = content["access_token"]


f1 = open("laoren.jpg","rb")
img = base64.b64encode(f1.read())

for i in range(1000):
    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    url = url + "?access_token=" + access_token
    params = json.dumps({"image":img,
                        "image_type":"BASE64",
                        "group_id":"YangLao",
                        "user_id":str(i+1)})
    request = urllib2.Request(url=url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    content = json.loads(content)
    print "Success:" + str(i+1)