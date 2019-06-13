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
from naoqi import ALProxy
import time
import pyautogui

timestar = 0

class PhotoHandler(tornado.web.RequestHandler):  #拍照
    def get(self):

        pass
    def post(self):
        # param = self.request.body.decode('utf-8')
        # prarm = json.loads(param)

        imgpath = "D:/HAphotos/imgphoto.jpg"
        picture = self.get_argument('data')
        # print type(picture),picture
        f = open(imgpath, "wb")
        f.write(base64.b64decode(picture))
        f.close()
        time.sleep(1)
        os.system(imgpath)
        time.sleep(1)
        pyautogui.press("f5")
        time.sleep(10)
        pyautogui.hotkey('altleft', 'f4')
        pass


define("port", default=11112, help="run port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/photo", PhotoHandler),
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)  # 监听端口
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
