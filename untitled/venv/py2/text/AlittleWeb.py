#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"

import sys
import os
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
import base64
import json
import socket
import time

class PptColHandler(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        ist = self.get_argument("instructions")
        if ist == '1':
            os.system(r'C:\Python27\python C:\pyfun\controlppt\LclickPPT.py')
        elif ist == '2':
            os.system(r'C:\Python27\python C:\pyfun\controlppt\PlayPPT.py')

