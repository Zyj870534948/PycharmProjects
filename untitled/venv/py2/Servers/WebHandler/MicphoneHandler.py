#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import json

# 用于记录页面时间的长短
class MicphoneHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("micphone.html")