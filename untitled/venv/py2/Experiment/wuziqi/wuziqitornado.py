#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import sys
import os
s = os.path.dirname(__file__)
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
import base64
import pyautogui
import time

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "html")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

class WuZiQiHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        pass
    def post(self):
        pass

define("port", default=11112, help="run port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/wuziqi", WuZiQiHandler),
        ]
        settings = dict(
            template_path=TEMPLATE_PATH,
            static_path=STATIC_PATH,
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)  # 监听端口
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

