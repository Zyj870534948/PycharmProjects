#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"

import sys
sys.path.append("./listener")
import os
from tornado.websocket import WebSocketHandler
from tornado.options import define, options
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver, tornado.gen, tornado.websocket
import listener
import base64
import json
import socket
import time
import requests
import cv2

TData = '**℃'
HData = '**%'

# 将 tornado.web.RequestHandler 替换成 BaseHandler
class BaseHandler(tornado.web.RequestHandler):
    # 解决跨域问题
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',#'*')
                        'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

class TestHandler(tornado.web.RequestHandler):
    def classification(self,file,filename,filetype): #分类
        FileType = {'image': ['jpg', 'png', 'gif', 'jpeg', 'bmp'],
                    'voice': ['mp3', 'mp4', 'wav', 'cda', 'mp2', 'mp1', 'mid', 'mav'],
                    'text':['txt','pdf','docx','xlsx','pptx','doc','xls','ppt'],
                    'compress':['zip','rar','7z','jar'],
                    'code':['c','cpp','cs','java','py']}
        if filetype in FileType["image"]:
            f = open(r'./file/image/' + filename, 'wb')
            f.write(base64.b64decode(file))
        elif filetype in FileType["voice"]:
            f = open(r'./file/voice/' + filename, 'wb')
            f.write(base64.b64decode(file))
        elif filetype in FileType["text"]:
            f = open(r'./file/yexy/' + filename, 'wb')
            f.write(base64.b64decode(file))
        elif filetype in FileType["compress"]:
            f = open(r'./file/compress/' + filename, 'wb')
            f.write(base64.b64decode(file))
        elif filetype in FileType["code"]:
            f = open(r'./file/code/' + filename, 'wb')
            f.write(base64.b64decode(file))
        else :
            f = open(r'./file/'+filename,'wb')
            f.write(base64.b64decode(file))

    def get(self):
        pass

    def post(self):
        file = self.get_argument("body")
        filename = self.get_argument("name")
        filetype = self.get_argument("type")
        self.classification(file,filename,filetype)


        # f = open(r'./file/'+filename,'wb')
        # f.write(base64.b64decode(file))

class PptColHandler(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        ist = self.get_argument("instructions")
        if ist == '1':
            os.system(r'C:\Python27\python C:\pyfun\controlppt\LclickPPT.py')
        elif ist == '2':
            os.system(r'C:\Python27\python C:\pyfun\controlppt\PlayPPT.py')

class THdataHandler(tornado.web.RequestHandler):
    def get(self):
        global TData,HData
        TData = self.get_argument("Tdata")
        HData = self.get_argument("Hdata")
        pass
    def post(self):
        global TData, HData
        TData = self.get_argument("Tdata")
        HData = self.get_argument("Hdata")
        pass


class THShow(tornado.web.RequestHandler):
    def get(self):
        self.write('<!DOCTYPE html>\
<html>\
<head>\
<meta charset="utf-8">\
<title>THData</title>\
<script>\
function replaceDoc()\
{\
    window.location.replace("http://192.168.3.21:11111/THShow")\
}\
</script>\
</head>\
<body>\
<p>' + TData +'</p>\
<p>' + HData + '</p>\
<input type="button" value="Refresh" onclick="replaceDoc()">\
\
</body>\
</html>')


class HAHandler(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        # Data = self.get_argument("date")
        # print Data
        param = self.request.body.decode('utf-8')
        prarm = json.loads(param)
        print(param)
        if prarm["cmd"]:
            data = prarm["cmd"]
            if data=="people_come_in":
                ip_port = ('192.168.3.18', 12322)
                sk = socket.socket()
                sk.connect(ip_port)
                sk.sendall('请求占领')
                server_reply = sk.recv(1024)
                print server_reply
                sk.close()
        if prarm["cmd"]:
            data = prarm["cmd"]
            if data=="people_is_ready":
                ip_port = ('192.168.3.18', 12323)
                sk = socket.socket()
                sk.connect(ip_port)
                sk.sendall('请求占领')
                server_reply = sk.recv(1024)
                print server_reply
                sk.close()

        pass


class WSHandler(WebSocketHandler):

    def open(self, *args, **kwargs):
        print '{0} connected'.format(self.request.remote_ip)

    def on_message(self, message):
        if message:
            if message:
                yield sleep(5)
                self.write_message("it\'s is done")

    def on_close(self):
        print 'client is exit'


# 机器人链接
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
        if result=='on':
            try:
                listener.instance.send_msg(result)
            except Exception as e:
                print(e.message)
        else:
            pass



class CamFaces(BaseHandler):   #tornado.web.RequestHandler

    def get(self):
        f = open('C:\\pyfun\\file\\picture\\faces.txt')
        result = f.read()
        print result
        self.write(result)
        pass
    def post(self):
        pass


class FacesPhoto(tornado.web.RequestHandler):
    def get(self):

        pass
    def post(self):
        from requests import get
        from requests import post
        url = 'http://192.168.3.5:8123/api/services/camera/snapshot'  # http://localhost:8123/api/services/switch/turn_on
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmNmJkNmEyOWM4ZjY0ZjI1OWY4ZDBlOWI4YWU2MTNiZSIsImlhdCI6MTU0ODIyMzg2MiwiZXhwIjoxODYzNTgzODYyfQ.-q8mDUy48ifCGaxXU7uo6xXy-4O1pQTpurRNgJ3aPJk',
            'content-type': 'application/json',
        }
        # data = '{"entity_id": "remote.xiaomi_rm","command":"' + air_tmp["close"] + '"}'
        data = '{"entity_id":"camera.cam1","filename":"C:/pyfun/file/picture/faces.jpg"}'
        response = post(url, data=data, headers=headers)

        filePath = r'C:\pyfun\file\picture\faces.jpg'
        f = open(filePath, 'rb')
        t = f.read()
        t2 = base64.b64encode(t)  # 编码

        filedata = {"api_key": "ZXaddlIuXG-txwMF3vo-zVLD4AG0RdTt",
                    "api_secret": "5OVudi95FGM5R7ePI79OLd0pL7tYFBai",
                    "image_base64": t2,
                    "return_attributes": "gender,age,smiling,emotion,ethnicity,eyestatus,skinstatus"}

        rep1 = requests.post(url="https://api-cn.faceplusplus.com/facepp/v3/detect", data=filedata)
        data = rep1.json()
        # print type(data),data
        print type(data["faces"]), data["faces"]
        print type(data["faces"][0]["face_rectangle"]), data["faces"][0]["face_rectangle"]

        filePath = r'C:\pyfun\file\picture\faces.jpg'
        img = cv2.imread(filePath)
        size = img.shape
        h = size[0]
        w = size[1]
        print h, w
        list1 = []
        j = 1
        for i in data["faces"]:
            y1, y2 = int(i["face_rectangle"]["top"]), int(i["face_rectangle"]["height"])
            x1, x2 = int(i["face_rectangle"]["left"]), int(i["face_rectangle"]["width"])
            y2 += y1
            x2 += x1
            if y1 - 50 < 0:
                y1 = 0
            if y2 + 5 >= h:
                y2 = h - 1
            if x1 - 10 < 0:
                x1 = 0
            if x2 + 10 > w:
                x2 = w - 1
            cut = img[y1 - 50:y2 + 5, x1 - 10:x2 + 10]
            cv2.imwrite('C:\\pyfun\\file\\picture\\face' + str(j) + '.jpg', cut)
            i["url"] = 'C:\\pyfun\\file\\picture\\face' + str(j) + '.jpg'
            list1.append(i)
            j += 1

        result = {
            "list": list1,
            "main": "C:\\pyfun\\file\\picture\\faces.jpg"
        }

        txt = json.dumps(result)

        f = open('C:\\pyfun\\file\\picture\\faces.txt', 'w')
        f.write(txt)
        f.close()

        pass