#!/usr/bin/env python
#-*- coding:utf-8 -*-

#_author:"xiaolin"
#date:2018/9/12

import tornado.web
import manger.config.global_variables
import manger.config.globalvar as gl

class ZhiboHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('zhiboresult.html')