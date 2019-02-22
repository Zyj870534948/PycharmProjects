#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"sidalin"
import os
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
from control.mainHandler import MainHandler
from control.downloadHandler import DownloadHandler
from control.localizationHandler import LocalizationHandler
from control.socketInfoHandler import SocketInfoHandler
from control.socketInfoHandler import DoorHandler

define("port", default=8083, help="run port", type=int)

TEMPLATE_PATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)), "template")
STATIC_PATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)), "static")


class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/menu", MainHandler),  # 待机界面
            (r"/download",DownloadHandler),
            # (r"/ht",HTHandler),
            (r"/localization",LocalizationHandler),
            (r"/socketInfo",SocketInfoHandler),
            (r"/door",DoorHandler),
        ]
        settings = dict(
            template_path=TEMPLATE_PATH,
            static_path=STATIC_PATH,
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)  # 监听端口
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
