#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"

import sys
import os
s = os.path.dirname(__file__)
sys.path.append(s + "/controlppt")
sys.path.append(s + "/WebHandler")
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
import base64
from WebHandler.WebHandler import TestHandler
from WebHandler.WebHandler import PptColHandler
from WebHandler.WebHandler import HAHandler
from WebHandler.WebHandler import WSHandler
from WebHandler.WebHandler import SocketInfoHandler
from WebHandler.WebHandler import DoorHandler
from WebHandler.WebHandler import CamFaces
from WebHandler.WebHandler import FacesPhoto
from WebHandler.WebHandler import Welcome
from WebHandler.WebHandler import Http
from WebHandler.WebHandler import Http2
from WebHandler.WebHandler import Test
from WebHandler.SpotHandler import SpotSaveHandler,SpotGetHandler
# from WebHandler.BehaviorHandler import BehaviorHandler
from WebHandler.MicphoneHandler import MicphoneHandler
from WebHandler.GettimeHandler import GetTime

Filelist = {"1":['file','controlppt','WebHandler'],
            "2":['file/code','file/image','file/voice','file/compress','file/yexy']}

for fl in Filelist:
    for fln in Filelist[fl]:
        if os.path.exists('./'+ fln):
            pass
        else :
            os.mkdir('./'+ fln)

define("port", default=11111, help="run port", type=int)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "html")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/getfile", TestHandler),      #
            (r"/controlppt", PptColHandler),
            (r"/HAapi", HAHandler),
            (r'/Robotscoket', WSHandler),
            (r"/socketInfo",SocketInfoHandler),
            (r"/door",DoorHandler),
            (r"/faces",CamFaces),
            (r"/photofaces",FacesPhoto),
            (r"/welcome", Welcome),
            (r"/test", Http),
            (r"/test2", Http2),
            (r"/tx", Test),
            (r"/savespot", SpotSaveHandler),
            (r"/getspot", SpotGetHandler),
            # (r"/starbehavior", BehaviorHandler),
            (r"/mic", MicphoneHandler),  #
            (r"/gettime",GetTime), #获取时间
        ]
        settings = dict(
            template_path=TEMPLATE_PATH,
            static_path=STATIC_PATH,
            debug=True
        )
        tornado.web.Application.__init__(self, handlers,**settings)

def main():
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)  # 监听端口
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
