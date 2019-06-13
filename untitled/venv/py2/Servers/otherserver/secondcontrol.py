#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"MrZhu"

import os
s = os.path.dirname(__file__)
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
import base64
import requests
import urllib, urllib2, sys
import ssl
import json
import pyautogui
import time

class CanHandler(tornado.web.RequestHandler):  #拍照
    def get(self):
        imgpath = "D:/HAphotos/img.jpg"
        url = 'http://192.168.8.108:8123/api/services/camera/snapshot'  # http://localhost:8123/api/services/switch/turn_on
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmNmJkNmEyOWM4ZjY0ZjI1OWY4ZDBlOWI4YWU2MTNiZSIsImlhdCI6MTU0ODIyMzg2MiwiZXhwIjoxODYzNTgzODYyfQ.-q8mDUy48ifCGaxXU7uo6xXy-4O1pQTpurRNgJ3aPJk',
            'content-type': 'application/json',
        }
        # data = '{"entity_id": "remote.xiaomi_rm","command":"' + air_tmp["close"] + '"}'
        data = '{"entity_id":"camera.cam1","filename":"'+ imgpath +'"}'
        re = requests.post(url, data=data, headers=headers)


        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=rdgzB4UQDLXMVgLyN6etijfm&client_secret=Ymsvjr5gDhbtW712ZKBVQQFXk1jLojhb'
        request = urllib2.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib2.urlopen(request)
        content = response.read()
        content = json.loads(content)

        access_token = content["access_token"]

        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"

        request_url = request_url + "?access_token=" + access_token

        f1 = open(imgpath, "rb")
        img = base64.b64encode(f1.read())

        params = json.dumps({"image": img,
                             "image_type": "BASE64",
                             "group_id_list": "VIP,OU"})

        request = urllib2.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(request)
        content = response.read()
        content = json.loads(content)

        try:
            print content["result"]["user_list"][0]["user_id"], content["result"]["user_list"][0]["score"],content["result"]["user_list"][0]["group_id"]
            dic = {
                "group_id":content["result"]["user_list"][0]["group_id"],
                "user_id":content["result"]["user_list"][0]["user_id"],
            }
            if content["result"]["user_list"][0]["score"] >80:
                self.write(json.dumps(dic))
            else :
                dic = {
                    "group_id": "no",
                    "user_id": "no",
                }
                self.write(json.dumps(dic))

        except:
            dic = {
                "group_id": "no",
                "user_id": "no",
            }
            self.write(json.dumps(dic))
            print content
        os.system(imgpath)
        time.sleep(0.5)
        pyautogui.press("f5")

        pass
    def post(self):
        imgpath = "D:/HAphotos/img.jpg"

        time.sleep(10)
        pyautogui.hotkey('altleft', 'f4')
        pass


define("port", default=11113, help="run port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/photo", CanHandler),
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)  # 监听端口
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
