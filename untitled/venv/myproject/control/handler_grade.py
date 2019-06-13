#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/8
import tornado.web
import json
import random


# 主要处理类
class GradeHandler(tornado.web.RequestHandler):

    #将收到的li=[1,1]转化成分数输出到屏幕上
    def get(self):
        li = self.get_argument('li')
        li = json.loads(li)
        score=random.randint(0,10)
        for i in li:
            if i==1:
                score=score+40
        sw = score/10
        gw = score%10
        # # data=[{"aaa":11,"user":222},{"aaa":22,"user":333}]
        self.render('grade.html', sw=sw, gw=gw)

