#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib, urllib2, sys,json
import ssl
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=2IGSwzTFgz2pfVhT0I9YYQoH&client_secret=uRXVkhwE0eFm033hxUskzc0erurRw97I'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    content = json.loads(content)
    print(content["access_token"])


url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer" + "?access_token=" + content["access_token"]
header={'Content-Type':'application/json'}
body = {"text":"我去西天取经了"}
body = json.dumps(body)

r = requests.post(url=url,data=body,headers=header)

print r.text

