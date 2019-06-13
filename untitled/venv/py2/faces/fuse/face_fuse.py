#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"

import os
import requests
import base64
import json
import cv2

def face_base64(photoPath):
    filePath = photoPath
    f = open(filePath, 'rb')
    t = f.read()
    bt = base64.b64encode(t)
    return bt

def face_position(photoPath):
    bt = face_base64(photoPath)
    filedata = {"api_key": "ZXaddlIuXG-txwMF3vo-zVLD4AG0RdTt",
                "api_secret": "5OVudi95FGM5R7ePI79OLd0pL7tYFBai",
                "image_base64": bt}

    rep1 = requests.post(url="https://api-cn.faceplusplus.com/facepp/v3/detect", data=filedata)
    data = rep1.json()
    x1,y1 = data["faces"][0]["face_rectangle"]["left"],data["faces"][0]["face_rectangle"]["top"]
    x2,y2 = data["faces"][0]["face_rectangle"]["width"],data["faces"][0]["face_rectangle"]["height"]
    return str(y1) + "," + str(x1) + "," + str(x2) + "," + str(y2)



modefacepath = r'./face3.jpg'
artworkfacepath = r'./face2.jpg'

modefacepic = face_base64(modefacepath)
artworkfacepic = face_base64(artworkfacepath)

modefaceloc = face_position(modefacepath)
artworkfaceloc = face_position(artworkfacepath)

filedata = {"api_key": "ZXaddlIuXG-txwMF3vo-zVLD4AG0RdTt",
            "api_secret": "5OVudi95FGM5R7ePI79OLd0pL7tYFBai",
            "template_base64": modefacepic,
            "template_rectangle": modefaceloc,
            "merge_base64": artworkfacepic,
            "merge_rectangle": artworkfaceloc}

rep1 = requests.post(url="https://api-cn.faceplusplus.com/imagepp/v1/mergeface", data=filedata)
data = rep1.json()

f = open(r'./faceout.jpg', 'wb')
f.write(base64.b64decode(data["result"]))



