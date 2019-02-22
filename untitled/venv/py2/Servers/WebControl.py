#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"

import sys
sys.path.append("./controlppt")
sys.path.append("./WebHandler")
import os
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
import base64
from WebHandler.WebHandler import TestHandler
from WebHandler.WebHandler import PptColHandler
from WebHandler.WebHandler import THdataHandler
from WebHandler.WebHandler import THShow
from WebHandler.WebHandler import HAHandler
from WebHandler.WebHandler import WSHandler
from WebHandler.WebHandler import SocketInfoHandler
from WebHandler.WebHandler import DoorHandler
from WebHandler.WebHandler import CamFaces
from WebHandler.WebHandler import FacesPhoto

Filelist = {"1":['file','controlppt','WebHandler'],
            "2":['file/code','file/image','file/voice','file/compress','file/yexy']}

for fl in Filelist:
    for fln in Filelist[fl]:
        if os.path.exists('./'+ fln):
            pass
        else :
            os.mkdir('./'+ fln)

define("port", default=11111, help="run port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/getfile", TestHandler),      #
            (r"/controlppt", PptColHandler),
            (r"/THdata", THdataHandler),
            (r"/THShow", THShow),
            (r"/HAapi", HAHandler),
            (r'/Robotscoket', WSHandler),
            (r"/socketInfo",SocketInfoHandler),
            (r"/door",DoorHandler),
            (r"/faces",CamFaces),
            (r"/photofaces",FacesPhoto),
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)  # 监听端口
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
