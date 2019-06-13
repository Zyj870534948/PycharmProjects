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
from naoqi import ALProxy

robotIP = "192.168.3.18"
PORT = 9559

motionProxy  = ALProxy("ALMotion", robotIP, PORT)
visualcompass = ALProxy("ALVisualCompass", robotIP, PORT)
navigation = ALProxy("ALNavigation", robotIP, PORT)
basicawareness = ALProxy("ALBasicAwareness", robotIP, PORT)

name = "地图"

name = raw_input("设置地图名称：")

while 1:
    r = raw_input("设置半径：")
    try:
        r = float(r)
        break
    except:
        print "输入错误，请重输。"

navigation.explore(r)
mapurl = navigation.saveExploration()
print mapurl
f = open('./mapurl.txt')
s = f.read()
s += '"' + name + '":"' + mapurl + '",'
f.close()
f = open('./mapurl.txt','w')
f.write(s)
f.close()

re = navigation.getMetricalMap()
result_map = navigation.getMetricalMap()
map_width = result_map[1]
map_height = result_map[2]
img = numpy.array(result_map[4]).reshape(map_width, map_height)
img = (100 - img) * 2.55  # from 0..100 to 255..0
img = numpy.array(img, numpy.uint8)
Image.frombuffer('L', (map_width, map_height), img, 'raw', 'L', 0, 1).show()

