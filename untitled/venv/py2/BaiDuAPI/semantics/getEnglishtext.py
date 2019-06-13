#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import urllib, urllib2, sys,json
import requests
import base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=T21059gyQkCIIQit0xu7P4D9&client_secret=nupLEUtPdgGQEWqY3r4neFQTEpoZtwz8'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    content = json.loads(content)
    print(content["access_token"])

f = open("./pytest.wav","rb")#/data/home/nao/nplus/MrZhu
fl = f.read()
speech = base64.b64encode(fl)
flen = len(fl)
f.close()

token = content["access_token"].encode("utf-8")
print token,type(token)

url = "http://vop.baidu.com/server_api" # + "?access_token=" + content["access_token"]
header={'Content-Type':'application/json'}
body = {
    "format":"wav",
    "rate":16000,
    "channel":1,
    "cuid":"04:92:26:D6:20:B1",
    "token":token,
    "dev_pid":1737,
    "speech":speech,
    "len":flen
}
body = json.dumps(body)

r = requests.post(url=url,data=body,headers=header)

t = json.loads(r.text.encode("utf-8"))
print t