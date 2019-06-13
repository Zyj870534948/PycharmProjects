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

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
# request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/delete"

request_url = request_url + "?access_token=" + access_token

f1 = open("./001.jpg","rb")
img = base64.b64encode(f1.read())


# params = json.dumps({"group_id":"VIP2"})

params = json.dumps({"image":img,
                     "image_type":"BASE64",
                     "group_id_list":"VIP"})

request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request)
content = response.read()
content = json.loads(content)

try:
    # print content["result"]["user_list"][0]["user_id"],content["result"]["user_list"][0]["score"],content["result"]["user_list"][0]["group_id"]
    print content
except:
    print content

# ["result"]["user_list"][0]["user_id"]

def getfacedate():
    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers"
    url = url + "?access_token=" + access_token
    params = json.dumps({"group_id": "OU"})
    request = urllib2.Request(url=url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    content = json.loads(content)
    return content["result"]["user_id_list"]


def addfase(img, i):
    url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    url = url + "?access_token=" + access_token
    params = json.dumps({"image": img,
                         "image_type": "BASE64",
                         "group_id": "OU",
                         "user_id": str(i)})
    request = urllib2.Request(url=url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    content = json.loads(content)

t = getfacedate()
print t
# addfase(img, len(t)+1)



'''
yess:{u'log_id': 1345050762724776442L, u'timestamp': 1556272477, u'cached': 0, u'result': {u'user_list': [{u'user_info': u'', u'group_id': u'VIP', u'user_id': u'1', u'score': 92.296241760254}], u'face_token': u'2d87cdedecc2e2b144d770b8778cbee6'}, u'error_code': 0, u'error_msg': u'SUCCESS'}
youn:{u'log_id': 1368654462725292401L, u'timestamp': 1556272529, u'cached': 0, u'result': None, u'error_code': 222207, u'error_msg': u'match user is not found'}
wurn:{u'log_id': 1368654462723330311L, u'timestamp': 1556272333, u'cached': 0, u'result': None, u'error_code': 222202, u'error_msg': u'pic not has face'}
'''