#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/9/7

import tornado.web


# 待机界面
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('main.html')
