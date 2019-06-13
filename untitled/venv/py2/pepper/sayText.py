#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import time

class PepperFunc:
    def __init__(self,IP):
        self.ip = IP
        self.pepperSay = ALProxy("ALAnimatedSpeech", IP, 9559)
        self.saytext = ALProxy("ALTextToSpeech", IP, 9559)
        self.memory = ALProxy("ALMemory", IP, 9559)

    def speak(self,saycontent):
        self.pepperSay.say(saycontent)
        # while 1:
        #     print self.memory.getData("ALTextToSpeech/Status")
        #     time.sleep(3)

if __name__ == '__main__':
    p=PepperFunc('192.168.3.33')
    p.speak('你好')
