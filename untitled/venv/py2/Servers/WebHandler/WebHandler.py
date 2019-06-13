#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:""

import sys
import os
s = os.path.dirname(os.path.dirname(__file__))
sys.path.append(s + "/listener")
sys.path.append(s + "/pepper")
# print sys.path
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
import pyautogui
import time
import os
from sayText import PepperFunc


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

# 给文件夹分类存储
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

    def post(self):      #获取文件
        file = self.get_argument("body")
        filename = self.get_argument("name")
        filetype = self.get_argument("type")
        self.classification(file,filename,filetype)


        # f = open(r'./file/'+filename,'wb')
        # f.write(base64.b64decode(file))

class PptColHandler(tornado.web.RequestHandler):  #接收post 运行脚本
    def get(self):
        pass
    def post(self):
        ist = self.get_argument("instructions")
        if ist == '1':
            os.system(r'C:\Python27\python C:\pyfun\controlppt\LclickPPT.py')   #打开ppt的脚本
        elif ist == '2':
            os.system(r'C:\Python27\python C:\pyfun\controlppt\PlayPPT.py')     #ppt翻页脚本



class HAHandler(tornado.web.RequestHandler):    #从homeassistant中获取http请求
    def get(self):
        pass
    def post(self):
        # Data = self.get_argument("date")
        # print Data
        param = self.request.body.decode('utf-8')
        prarm = json.loads(param)
        print(param)
        if prarm["cmd"]:                                #自动化接收门磁传感器
            data = prarm["cmd"]
            if data=="people_come_in":
                ip_port = ('192.168.3.18', 12322)
                sk = socket.socket()
                sk.connect(ip_port)
                sk.sendall('请求占领')
                server_reply = sk.recv(1024)
                print server_reply
                sk.close()
        if prarm["cmd"]:                                #自动化接收人体传感器
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


class WSHandler(WebSocketHandler):              #socket

    def open(self, *args, **kwargs):
        print '{0} connected'.format(self.request.remote_ip)

    def on_message(self, message):
        if message:
            if message:
                yield sleep(5)
                self.write_message("it\'s is done")

    def on_close(self):
        print 'client is exit'


# 机器人socket链接''''''''''''
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

''''''''''''


class CamFaces(BaseHandler):   #tornado.web.RequestHandler  #网页请求face++数据

    def get(self):
        f = open('C:\\pyfun\\file\\picture\\faces.txt')
        result = f.read()
        print result
        self.write(result)
        pass
    def post(self):
        pass


class FacesPhoto(tornado.web.RequestHandler):       #摄像头拍照并调用face++  opencv处理抠图
    def get(self):

        pass
    def post(self):
        from requests import get
        from requests import post


        #调用HA摄像头拍照
        url = 'http://192.168.3.5:8123/api/services/camera/snapshot'  # http://localhost:8123/api/services/switch/turn_on
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmNmJkNmEyOWM4ZjY0ZjI1OWY4ZDBlOWI4YWU2MTNiZSIsImlhdCI6MTU0ODIyMzg2MiwiZXhwIjoxODYzNTgzODYyfQ.-q8mDUy48ifCGaxXU7uo6xXy-4O1pQTpurRNgJ3aPJk',
            'content-type': 'application/json',
        }
        # data = '{"entity_id": "remote.xiaomi_rm","command":"' + air_tmp["close"] + '"}'
        data = '{"entity_id":"camera.cam1","filename":"C:/pyfun/file/picture/faces.jpg"}'
        response = post(url, data=data, headers=headers)


        #调用face++ Api
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
        # print type(data["faces"]), data["faces"]
        # print type(data["faces"][0]["face_rectangle"]), data["faces"][0]["face_rectangle"]



        #将头像抠出来
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
            y1 -= 50
            y2 += 4
            x1 -= 10
            x2 += 10
            if y1 - 50 < 0:
                y1 = 0
            if y2 + 4 >= h:
                y2 = h - 1
            if x1 - 27 < 0:
                x1 = 0
            if x2 + 27 > w:
                x2 = w - 1
            cut = img[y1:y2, x1:x2]

            # 将人脸加上图片地址
            cv2.imwrite('C:\\pyfun\\file\\picture\\face' + str(j) + '.jpg', cut)
            i["url"] = 'C:\\pyfun\\file\\picture\\face' + str(j) + '.jpg'
            list1.append(i)
            j += 1

        result = {
            "list": list1,
            "main": "C:\\pyfun\\file\\picture\\faces.jpg"
        }


        #将数据存在本地txt
        txt = json.dumps(result)
        f = open('C:\\pyfun\\file\\picture\\faces.txt', 'w')
        f.write(txt)
        f.close()

        #刷新网页
        pyautogui.hotkey('ctrl', 'w')
        os.system(r'start "C:\Users\N-pod\AppData\Local\Google\Chrome\Application\chrome.exe" file:///C:/pyfun/file/picture/dist/index.html#/videos')
        # pyautogui.press("f5")
        pass



class Welcome(tornado.web.RequestHandler):    #接收HA 门磁post请求 并说话
    def get(self):
        pass
    def post(self):
        from requests import get
        from requests import post

        param = self.request.body.decode('utf-8')
        prarm = json.loads(param)
        if prarm["cmd"]:
            data = prarm["cmd"]
            if data=="Welcome":
                p = PepperFunc(unicode.encode(prarm["IP"]))
                print unicode.encode(prarm["IP"]),type(unicode.encode(prarm["IP"]))
                p.speak('欢迎光临')

class Http(BaseHandler):                #探索地图/标记点位/跳转到配置界面
    def get(self):
        self.render("test.html")
        pass

class Http2(BaseHandler):               #配置界面/选择点/选择说话内容（向后台请求）/选择动作
    def get(self):
        self.render("D:\\GitHub\\PycharmProjects\\untitled\\venv\\py2\\Servers\\html\\test2.html")
        pass

class GetHttpText(BaseHandler):               #配置界面/选择点/选择说话内容（向后台请求）/选择动作
    def get(self):
        self.render("D:\\GitHub\\PycharmProjects\\untitled\\venv\\py2\\Servers\\html\\test2.html")
        pass

class Test(BaseHandler):
    def get(self):
        a = self.get_argument("dian")
        a = json.loads(a)
        print type(a),a
        self.write('{"123":1}')
        pass