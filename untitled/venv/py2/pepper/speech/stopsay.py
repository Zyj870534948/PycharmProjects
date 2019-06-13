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
        self.saytext = ALProxy("ALTextToSpeech", IP, 9559)
        self.memory = ALProxy("ALMemory", IP, 9559)

    def speak(self,saycontent):
        # id = self.saytext.post.say(saycontent)
        # print id
        # time.sleep(1)
        self.saytext.stopAll()   #(id)
        # while 1:
        #     print self.memory.getData("ALTextToSpeech/Status")
        #     time.sleep(3)

if __name__ == '__main__':
    p=PepperFunc('192.168.8.146')
    p.speak('一二三四五六七八九十')

    # i = 1
    # while i:
    #     try:
    #         open("./" + str(i) + ".txt", "r")
    #         i += 1
    #     except:
    #         open("./"+str(i)+".txt","w")
    #         break