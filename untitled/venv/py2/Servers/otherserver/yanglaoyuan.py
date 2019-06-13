#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"MrZhu"

import os
s = os.path.dirname(__file__)
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
import base64



class PhotoHandler(tornado.web.RequestHandler):  #拍照
    def get(self):
        imgpath = "D:/HAphotos/ylyface.jpg"
        f = open(imgpath,"rb")
        f = base64.b64encode(f.read())
        self.write(f)
        pass
    def post(self):
        pass

class androidshowimg(tornado.web.RequestHandler):
    def get(self):
        self.render('showpicture.html')


define("port", default=11696, help="run port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/photo", PhotoHandler),
            (r"/androidimg", androidshowimg),
        ]
        settings = dict(
            template_path=r"D:\GitHub\PycharmProjects\untitled\venv\py2\Servers\html",
            static_path=r"D:\GitHub\PycharmProjects\untitled\venv\py2\Servers\static",
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
