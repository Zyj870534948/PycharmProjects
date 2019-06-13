#!/usr/bin/env python
#-*- coding:utf-8 -*-

#_author:"xiaolin"
#date:2018/9/4
import tornado.web
import manger.config.global_variables
import manger.config.globalvar as gl

class IdHandler(tornado.web.RequestHandler):
    def get(self):
        id=gl.get_value('pepper_id')
        self.write(id)