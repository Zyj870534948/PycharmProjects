#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"MrZhu"

from tornado.websocket import WebSocketHandler
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver, tornado.gen, tornado.websocket

# 将 tornado.web.RequestHandler 替换成 BaseHandler
class BaseHandler(tornado.web.RequestHandler):
    # 解决跨域问题
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',#'*')
                        'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
