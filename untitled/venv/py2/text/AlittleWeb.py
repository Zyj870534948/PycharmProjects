#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"

import sys
import os
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
import json
import time

# os.system("python ./sayText.py")
class APP(tornado.web.RequestHandler):
    def get(self):
        print "app"
        pass
    def post(self):
        pass

class B(tornado.web.RequestHandler):
    def get(self):
        print "b"
        pass
    def post(self):
        print "c"
        pass


define("port", default=11111, help="run port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/app", APP),
            (r"/b", B),  #http://192.168.3.5:11111/b
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)  # 监听端口
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

