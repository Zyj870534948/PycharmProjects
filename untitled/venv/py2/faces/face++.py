#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"

import os
import requests
import base64
import json
import cv2


filePath = r'C:\pyfun\file\picture\faces.jpg'
f = open(filePath,'rb')
t = f.read()
t2 = base64.b64encode(t)     #编码

filedata = {"api_key":"ZXaddlIuXG-txwMF3vo-zVLD4AG0RdTt",
            "api_secret":"5OVudi95FGM5R7ePI79OLd0pL7tYFBai",
            "image_base64":t2,
            "return_attributes":"gender,age,smiling,emotion,ethnicity,eyestatus,skinstatus"}

rep1 = requests.post(url="https://api-cn.faceplusplus.com/facepp/v3/detect",data=filedata )
data = rep1.json()
# print type(data),data
print type(data["faces"]),data["faces"]
print type(data["faces"][0]["face_rectangle"]),data["faces"][0]["face_rectangle"]


filePath = r'C:\pyfun\file\picture\faces.jpg'
img = cv2.imread(filePath)
size = img.shape
h = size[0]
w = size[1]
print h,w
list1 = []
j = 1
for i in data["faces"]:
    y1, y2 = int(i["face_rectangle"]["top"]), int(i["face_rectangle"]["height"])
    x1, x2 = int(i["face_rectangle"]["left"]), int(i["face_rectangle"]["width"])
    y2 += y1
    x2 += x1
    if y1-50 < 0:
        y1 = 0
    if y2+5 >= h:
        y2 = h-1
    if x1-10 <0:
        x1 = 0
    if x2+10 > w:
        x2 = w-1
    cut = img[y1-50:y2+5,x1-10:x2+10]
    cv2.imwrite('C:\\pyfun\\file\\picture\\face' + str(j) +  '.jpg', cut)
    i["url"] = 'C:\\pyfun\\file\\picture\\face' + str(j) +  '.jpg'
    list1.append(i)
    j += 1

print list1

