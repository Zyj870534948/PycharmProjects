#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import qi
import argparse
import sys
import time
from naoqi import ALProxy

robotIP = "192.168.3.18"
PORT = 9559

motionProxy  = ALProxy("ALMotion", robotIP, PORT)
localizationProxy = ALProxy("ALLocalization", robotIP, PORT)

# # Learning home.学习家。
# ret = localizationProxy.learnHome()
#
# # Check that no problem occurred.检查是否没有问题。
# if ret == 0:
#   print "Learning OK"
# else:
#   print "Error during learning " + str(ret)
#
# # Make some moves.做一些动作。
# motionProxy.moveTo(0.5, 0.0, 0.2)
#
# # Go back home.回家吧。
# ret = localizationProxy.goToHome()
# # Check that no problem occurred.检查是否没有问题。
# if ret == 0:
#   print "go to home OK"
# else:
#   print "error during go to home " + str(ret)
#
# # Save the data for later use.保存数据供以后使用。
# ret = localizationProxy.save("nplushys")
#
# # Check that no problem occurred.检查是否没有问题。
# if ret == 0:
#   print "saving OK"
# else:
#   print "error during saving" + str(ret)

# ret = localizationProxy.learnHome()
# if ret == 0:
#   print "Learning OK"
# else:
#   print "Error during learning " + str(ret)
# print "123"
# time.sleep(10)

ret = localizationProxy.load("nplushys")

ret = localizationProxy.goToHome()

if ret == 0:
  print "go to home OK"
else:
  print "error during go to home " + str(ret)