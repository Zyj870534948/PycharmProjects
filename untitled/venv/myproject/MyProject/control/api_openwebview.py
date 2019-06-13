#!/usr/bin/env python
#-*- coding:utf-8 -*-

#_author:"xiaolin"
#date:2018/9/8

#用于开启pepper的页面
import tornado.web
import manger.config.globalvar as gl
import manger.config.global_variables
import time
from threading import Thread


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper

# 待机界面
class OpenwebviewHandler(tornado.web.RequestHandler):


    def get(self):
        name = self.get_argument('name')
        self.A(name)
        self.write('success')


    @async
    def A(self,name):
        time.sleep(4)
        if name=='main':
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')
        elif name=='standby':
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'standby')
        elif name=='stop':
            gl.get_value('func').stopSpeak(gl.get_value('session'))


