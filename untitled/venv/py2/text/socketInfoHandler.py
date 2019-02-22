#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import tornado.websocket
import tornado.web
import listener



class SocketInfoHandler(tornado.websocket.WebSocketHandler):
    users = set()
    def open(self):
        print("connect success")
        self.users.add(self)  # 建立连接后添加用户到容器中
        listener.instance.set_listener("view", self.sendMessage)

    def sendMessage(self,msg):
        for u in self.users:  # 向在线用户广播消息
            u.write_message(u"%s" % (msg))


    def on_message(self, message):
        pass

    def on_close(self):
        try:
            listener.instance.remove_listener("view")
            self.users.remove(self)  # 用户关闭连接后从容器中移除用户
        except Exception as e:
            print(e.message)





class DoorHandler(tornado.websocket.WebSocketHandler,tornado.web.RequestHandler):
    def get(self):
        result=self.get_argument('data')
        print(result=='on')
        print(type(result))
        if result=='on':
            try:
                listener.instance.send_msg(result)
            except Exception as e:
                print(e.message)
        else:
            pass
