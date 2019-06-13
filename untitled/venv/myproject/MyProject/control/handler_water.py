#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"
import tornado
from control.api_standby import Standby_api


class WaterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('waterDispenser.html')
