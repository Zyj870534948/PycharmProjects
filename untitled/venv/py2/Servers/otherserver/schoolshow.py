#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"MrZhu"

import os,sys
s = os.path.dirname(__file__)
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
import base64
import time
import pyautogui



class PhotoHandler(tornado.web.RequestHandler):  #拍照
    def get(self):
        imgpath = "D:/HAphotos/ylyface.jpg"
        f = open(imgpath,"rb")
        f = base64.b64encode(f.read())
        self.write(f)
        os.system(r'D:/HAphotos/ylyface.jpg')
        pass
    def post(self):
        pass


define("port", default=11696, help="run port", type=int)


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