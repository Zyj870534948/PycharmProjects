#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import os
from BaseHandler import BaseHandler
from naoqi import ALProxy
import json
import time
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver, tornado.gen, tornado.websocket

class GetTime(BaseHandler):
    def get(self):
        t = time.time()
        print t
        self.write(str(int(t)))
        pass
    def post(self):
        pass