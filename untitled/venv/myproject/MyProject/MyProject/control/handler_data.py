#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/21

import tornado.web
import listener
import json
import manger.config.globalvar as gl
import manger.config.global_variables
import handler_all
from compare import Compare


# data类获取听到的数据,是给后台的接口，获得后台发送来的数据
class DataHandler(tornado.web.RequestHandler):
    def get(self):
        data = self.get_argument('data')
        data = data.encode('utf-8')
        data_json = json.loads(data)
        # 获得听到的数据
        # 可能text是说的消息
        speech = data_json['text']
        # 获得说的数据
        listen = data_json['sayText']
        url = data_json['url']
        chat_msg = {'speech': speech, 'listen': listen, 'url': url}
        #change
        view_msg = {'speech': speech, 'listen': listen}
        # 消息监听的信息发送
        listener.instance.send_msg(view_msg)
        listener.instance.send_chat_msg(chat_msg)

        if handler_all.page=='func':
            if url!="":
                self.goto_url(chat_msg['url'])


    def goto_url(self, url):
        gl.get_value('func').webview(gl.get_value('session'), url)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        if Compare().conmpare(u'返回首页', listen) > 0.4:
            gl.get_value('func').speech(gl.get_value('session'), '好的请稍等')
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'func')


