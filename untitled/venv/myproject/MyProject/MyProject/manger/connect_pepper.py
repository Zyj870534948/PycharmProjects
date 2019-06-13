#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/7

import qi
import sys


class Open_pepper:
    def __init__(self):
        self.port = '9559'


    def star_pepper(self, ip):
        self.ip = ip
        session = qi.Session()
        try:
            session.connect("tcp://" + self.ip + ":" + self.port)
            self.session=session
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + self.port + "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)

    def get_session(self):
        return self.session


if __name__ == '__main__':
    open_pepper = Open_pepper()
    open_pepper.star_pepper('192.168.43.179')
