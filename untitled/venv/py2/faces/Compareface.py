#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import base64
import json
import socket
import time
import requests
import cv2
from requests import get
from requests import post


filePath = r'C:\pyfun\file\picture\faces.jpg'
f = open(filePath, 'rb')
t = f.read()
t2 = base64.b64encode(t)  # 编码
filePath = r'C:\pyfun\file\picture\faces.jpg'
f = open(filePath, 'rb')
t = f.read()
t3 = base64.b64encode(t)  # 编码

filedata = {"api_key": "ZXaddlIuXG-txwMF3vo-zVLD4AG0RdTt",
            "api_secret": "5OVudi95FGM5R7ePI79OLd0pL7tYFBai",
            "image_base64_1": t2,
            "image_base64_2": t3}

rep1 = requests.post(url="https://api-cn.faceplusplus.com/facepp/v3/compare", data=filedata)
data = rep1.json()
print data
