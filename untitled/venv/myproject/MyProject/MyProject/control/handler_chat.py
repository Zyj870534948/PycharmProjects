#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/20


import datetime
from tornado.websocket import WebSocketHandler
import tornado.web
import listener, re, json
import handler_all
from transfer import Transfer
import manger.config.global_variables
import manger.config.globalvar as gl
import time, logging


class Speech:
    def speech(self, speech):
        gl.get_value('func').speech(gl.get_value('session'), speech)


class CviewHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('duida.html')


# 主要处理类
class ChatHandler(WebSocketHandler):
    users = set()
    flag = ''

    def open(self):
        self.users.add(self)  # 建立连接后添加用户到容器中

        if handler_all.page == 'xiti':
            listener.instance.set_listener("chat", self.send_answer)
        elif handler_all.page == 'trans':
            listener.instance.set_listener("chat", self.send_transfer)
        else:
            listener.instance.set_listener("chat", self.send_message)
            self.flag = 'chat'

        # for u in self.users:  # 向已在线用户发送消息
        #     u.write_message(
        #         u"[%s]-[%s]-进入聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # 消息发送
    def send_message(self, msg):
        msg = {'speech': msg['speech'], 'listen': msg['listen'], 'url': msg['url']}
        # print msg
        spee = msg['speech']
        msg = json.dumps(msg)
        if msg:
            for u in self.users:  # 向在线用户广播消息
                u.write_message(u"%s" % (msg))
        else:
            for u in self.users:  # 向在线用户广播消息
                u.write_message(u"%s" % ('不好意思，没有消息'))

        if handler_all.flag_speech:
            s = Speech()
            s.speech(spee)

    # 向前端发送答案（用于习题解答界面）
    def send_answer(self, msg):
        msg = msg['listen']
        if msg.find(u'一') != -1:
            msg = '1'
        elif msg.find(u'二') != -1:
            msg = '2'
        elif msg.find(u'三') != -1:
            msg = '3'
        elif msg.find(u'四') != -1:
            msg = '4'
        msg = re.sub("\D", "", msg)
        if msg:
            for u in self.users:
                u.write_message(u"%s" % (msg[0]))
        else:
            print 5
            for u in self.users:  # 向在线用户广播消息
                u.write_message(u"%s" % ('5'))

    def send_transfer(self, msg):
        msg = msg['listen'].encode('utf-8')
        t = Transfer()
        result = t.transfer(msg)
        if isinstance(result, dict):
            result1 = {'listen': result['src'], 'speech': result['dst']}
            result2 = json.dumps(result1)
            logging.info(result2)
            for u in self.users:
                u.write_message(u"%s" % (result2))

            time.sleep(3)

        else:
            for u in self.users:
                u.write_message(u"%s" % (result))
            time.sleep(3)

    def on_message(self, message):
        for u in self.users:  # 向在线用户广播消息
            u.write_message(u"[%s]-[%s]-说：%s" % (
                self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

    def on_close(self):
        self.users.remove(self)  # 用户关闭连接后从容器中移除用户
        if listener.instance.exist('chat'):
            listener.instance.remove_listener("chat")

    def check_origin(self, origin):
        return True
