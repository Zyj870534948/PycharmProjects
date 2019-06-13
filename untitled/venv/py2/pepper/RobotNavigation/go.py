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






# navigation.navigateToInMap([1, -0.3, 0])
# navigation.navigateToInMap([0, 0, 0])      #移动到地图的标记位置

re = navigation.getRobotPositionInMap()[0]   #[0.09629068523645401, -0.7858160734176636, -2.5796892642974854]     #显示
print re
re = navigation.getRobotPositionInMap()[1]   #[0.09629068523645401, -0.7858160734176636, -2.5796892642974854]     #显示
print re
try:
    re = navigation.getRobotPositionInMap()[2]  # [0.09629068523645401, -0.7858160734176636, -2.5796892642974854]     #显示
    print re
except:
    pass


#记录
# [-0.003624433884397149, 0.25341907143592834, -0.2305673360824585]
# [1.452305555343628, 0.9517713189125061, 3.8695125579833984]

# [-0.03826332837343216, -0.9771316647529602, -0.5537741780281067]
# [0.29583480954170227, 0.28103742003440857, 0.32883206009864807]

# [0.1890820562839508, -0.5992516279220581, 0.09844373911619186]
# [0.4919433295726776, 1.7900376319885254, 3.9114301204681396]

#
# time.sleep(10)
#
# re = navigation.getRobotPositionInMap()[0]
# print re


navigation.stopLocalization()  #关闭本地化
navigation.stopExploration()



# try:
#     while 1:
#         re = navigation.getRobotPositionInMap()[0]
#         print re
#         r=input("是否继续")
#         if r==1:
#             x=input("X轴：")
#             y=input("Y轴：")
#             navigation.navigateToInMap([float(x), float(y), 0])
#         elif r == 2:
#             Ax = float(re[0])
#             Ay = float(re[1])
#             print type(Ax) , Ay
#         elif r == 3:
#             navigation.navigateToInMap([Ax, Ay, 0])
#         else :
#             break
#         # navigation.navigateToInMap([float(x),float(y),0])
# except:
#     navigation.stopLocalization()
#
# navigation.stopLocalization()
