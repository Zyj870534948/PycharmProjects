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

Ax = 0.0
Ay = 0.0

robotIP = "192.168.3.18"
PORT = 9559

motionProxy  = ALProxy("ALMotion", robotIP, PORT)
visualcompass = ALProxy("ALVisualCompass", robotIP, PORT)
navigation = ALProxy("ALNavigation", robotIP, PORT)
basicawareness = ALProxy("ALBasicAwareness", robotIP, PORT)


basicawareness.setEnabled(False)


# re = navigation.explore(2.5)
#
# re = navigation.saveExploration()
# print re
#
# re = navigation.getMetricalMap()
# result_map = navigation.getMetricalMap()
# map_width = result_map[1]
# map_height = result_map[2]
# img = numpy.array(result_map[4]).reshape(map_width, map_height)
# img = (100 - img) * 2.55  # from 0..100 to 255..0
# img = numpy.array(img, numpy.uint8)
# Image.frombuffer('L', (map_width, map_height), img, 'raw', 'L', 0, 1).show()

navigation.loadExploration("/home/nao/.local/share/Explorer/2019-02-27T071633.300Z.explo")    #/home/nao/.local/share/Explorer/2014-04-04T012831.156Z.explo    #/home/nao/.local/share/Explorer/2019-02-27T071633.300Z.explo
navigation.relocalizeInMap([0.0,0.0])
navigation.startLocalization()
try:
    while 1:
        re = navigation.getRobotPositionInMap()[0]
        print re
        r=input("是否继续")
        if r==1:
            x=input("X轴：")
            y=input("Y轴：")
            basicawareness.setEnabled(True)
            navigation.navigateToInMap([float(x), float(y), 0])
        elif r == 2:
            Ax = float(re[0])
            Ay = float(re[1])
            print type(Ax) , Ay
        elif r == 3:
            basicawareness.setEnabled(True)
            navigation.navigateToInMap([Ax, Ay, 0])
        else :
            break
        # navigation.navigateToInMap([float(x),float(y),0])
except:
    navigation.stopLocalization()

navigation.stopLocalization()
