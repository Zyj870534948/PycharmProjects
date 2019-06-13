#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__
启动后 用get请求发送instructions=1 打开ppt 发送instructions=2 ppt翻页
'''

import sys
import os
s = os.path.dirname(__file__)
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
import base64
import pyautogui
import time

PYthonPATH = "C:/Python27/python"


class PptColHandler(tornado.web.RequestHandler):  #接收post 运行脚本
    PPTPATH = r"C:\pyfun\file\nvwa.pptx"
    def get(self):
        ist = self.get_argument("instructions")
        if ist == '1':
            try:
                path = self.get_argument("path")
                self.PPTPATH = path
                print("true")
            except:
                print("false")
                pass
            os.system(r'start ' + self.PPTPATH)
            time.sleep(3)
            pyautogui.press("f5")
        elif ist == '2':
            pyautogui.scroll(-200)
        pass
    def post(self):
        pass

define("port", default=11111, help="run port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/controlppt", PptColHandler),
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)  # 监听端口
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
'''
#打开ppt的方式
import requests
requests.get("http://ip:11111/controlppt?" + "instructions=1" + ";" + "path=C:/pyfun/file/nvwa.pptx")
requests.get("http://ip:11111/controlppt?" + "instructions=2")
'''

