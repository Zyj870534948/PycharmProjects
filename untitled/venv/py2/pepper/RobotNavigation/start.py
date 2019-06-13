#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import qi
import argparse
import sys
import time
import numpy
import Image
import argparse
import os
import json
from naoqi import ALProxy

robotIP = "192.168.3.18"
PORT = 9559

motionProxy  = ALProxy("ALMotion", robotIP, PORT)
visualcompass = ALProxy("ALVisualCompass", robotIP, PORT)
navigation = ALProxy("ALNavigation", robotIP, PORT)
basicawareness = ALProxy("ALBasicAwareness", robotIP, PORT)

# f = open('./mapurl.txt')
# s = f.read()
# f.close()
# s = '{' + s + '}'
# data = json.loads(s)
# print type(data["nvwashiyanshi"]),data["nvwashiyanshi"]

navigation.loadExploration("/home/nao/.local/share/Explorer/2019-02-27T071633.300Z.explo")    #/home/nao/.local/share/Explorer/2014-04-04T012831.156Z.explo    #/home/nao/.local/share/Explorer/2019-02-27T071633.300Z.explo
navigation.relocalizeInMap([0.0,0.0])
navigation.startLocalization()    #开启本地化

