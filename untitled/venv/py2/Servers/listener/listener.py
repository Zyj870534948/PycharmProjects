#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/21

# 监听事件
class Listener(object):
    listeners = {}

    # 设置监听事件
    def set_listener(self, key, listener):
        self.listeners[key] = listener

    def remove_listener(self, key):
        self.listeners.pop(key)

    def exist(self,key):
        for k in self.listeners.keys():
            if k == key:
                return True

    # 遍历所有的监听事件，并想该事件发送消息
    def send_msg(self, msg):
        for key in self.listeners.keys():
            self.listeners[key](msg)



    def send_chat_msg(self, msg):
        for key in self.listeners.keys():
            if key == 'chat':
                self.listeners[key](msg)


instance = Listener()
