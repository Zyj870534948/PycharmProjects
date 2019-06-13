#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

from naoqi import ALProxy
import time

class PepperFunc:
    def __init__(self,IP):
        self.ip = IP
        self.behavior = ALProxy("ALBehaviorManager", IP, 9559)
        self.memory = ALProxy("ALMemory", IP, 9559)

    def do(self):
        self.behavior.runBehavior("takephoto2-4af670/behavior_1")

if __name__ == '__main__':
    p=PepperFunc('192.168.3.33')
    p.do()
