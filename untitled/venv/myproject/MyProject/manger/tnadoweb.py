#!/usr/bin/env python
        # -*- coding:utf-8 -*-
        # _author:"sidalin"

        import sys
        from tornado.options import define, options
        import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
        import json
        import time

        class PptColHandler(tornado.web.RequestHandler):
            def get(self):
                pass
            def post(self):
                pass

        class APP(tornado.web.RequestHandler):
            def get(self):
                print "1"
                pass
            def post(self):
                pass


        define("port", default=11111, help="run port", type=int)
        class Application(tornado.web.Application):
            def __init__(self):
                # 路由
                handlers = [
                    (r"/controlppt", PptColHandler),
                    (r"/app", APP),
                ]
                tornado.web.Application.__init__(self, handlers)

        def main():
            tornado.options.parse_command_line()
            app = tornado.httpserver.HTTPServer(Application())
            app.listen(options.port)  # 监听端口
            tornado.ioloop.IOLoop.instance().start()

        if __name__ == '__main__':
            main()
        