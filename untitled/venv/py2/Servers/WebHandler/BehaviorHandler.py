#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__
前端将流程通过post（behavior）发送至BehaviorHandler接口将流程存储至本地并获取流程执行流程
'''


import os
from BaseHandler import BaseHandler
from explorhandler import ExplorFunc
from naoqi import ALProxy
import json
from iotcontrol import *
import time

Behavior_json_path = os.path.dirname(os.path.dirname(__file__)) + "/static/json/behavior.json"
Spot_json_path = os.path.dirname(os.path.dirname(__file__)) + "/static/json/Spot.json"
Say_json_path = os.path.dirname(os.path.dirname(__file__)) + "/static/json/Say.json"
Do_json_path = os.path.dirname(os.path.dirname(__file__)) + "/static/json/Do.json"

class BehaviorHandler(BaseHandler):
    def get(self):
        pass
    def post(self):
        a = self.get_argument("behavior")
        a = a.encode("utf-8")
        f = open(Behavior_json_path, "w")
        f.write(a)
        f.close()
        '''执行步骤'''
        f = open(Behavior_json_path, "r")
        a = f.read()
        f.close()
        a = json.loads(a)
        ef = ExplorFunc()
        for i in a:
            for j in i:
                if j == "move":
                    f = open(Spot_json_path,"r")
                    b = f.read()
                    f.close()
                    b = json.loads(b)
                    text1 = i[j]
                    print(type(b[text1]),b[text1])
                    ef.moveToTarget(b[text1]) #.encode("utf-8")
                    print("移动到点：",i[j].encode("utf-8"),b[text1])
                    time.sleep(0.5)
                elif j == "say":
                    f = open(Say_json_path, "r")
                    b = f.read()
                    f.close()
                    b = json.loads(b)
                    text2 = i[j]
                    ef.sayS(b[text2].encode("utf-8"))
                    time.sleep(0.5)

                elif j == "do":
                    f = open(Do_json_path, "r")
                    b = f.read()
                    f.close()
                    c = json.loads(b)
                    text3 = i[j]
                    iot = Iot(c[text3].encode("utf-8"))
                    iot.control()
                    print(i[j].encode("utf-8"),c[text3].encode("utf-8"))
                    time.sleep(0.5)





