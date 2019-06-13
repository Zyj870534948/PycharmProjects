#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__
将点的信息通过post请求json格式()发送至SpotSaveHandler的接口 以json的格式存储在本地
向SpotGetHandler的接口get请求获取已记录的点的名字
'''


import os
from tornado.websocket import WebSocketHandler
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver, tornado.gen, tornado.websocket
from BaseHandler import BaseHandler

Spot_json_path = os.path.dirname(os.path.dirname(__file__)) + "/static/json/Spot.json"
Say_json_path = os.path.dirname(os.path.dirname(__file__)) + "/static/json/Say.json"
Do_json_path = os.path.dirname(os.path.dirname(__file__)) + "/static/json/Do.json"

class SpotSaveHandler(BaseHandler):
    def get(self):
        pass
    def post(self):
        a = self.get_argument("Spot")
        # a = json.loads(a)
        print type(a), a
        f = open(Spot_json_path,"w")
        f.write(a)
        f.close()
        print Spot_json_path
        pass


class SpotGetHandler(BaseHandler):
    def get(self):
        a = self.get_argument("data")
        if a=="1":
            f = open(Spot_json_path, "r")
        if a == "2":
            f = open(Say_json_path, "r")
        if a == "3":
            f = open(Do_json_path, "r")
        j = f.read()
        f.close()
        print type(j),j
        self.write(j)
        pass
    def post(self):
        pass

