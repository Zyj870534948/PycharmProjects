#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

from naoqi import ALProxy

class PepperFunc:
    def __init__(self,IP):
        self.ip = IP
        self.pepperSay = ALProxy("ALAnimatedSpeech", IP, 9559)
        self.memory_service = ALProxy("ALMemory", IP, 9559)
        self.sonar_service = ALProxy("ALSonar", IP, 9559)
        self.i=0

    def speak(self,saycontent):
        self.pepperSay.say(saycontent)

    def sensor(self):
        self.sonar_service.subscribe("myApplication")
        self.distance=self.memory_service.getData("Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value")
        self.sonar_service.unsubscribe("myApplication")
        self.distance = float(self.distance)
        self.i = self.i + 1
        print self.distance

if __name__ == '__main__':
    p=PepperFunc('192.168.3.33')
    # p.speak('你好')
    p.sensor()


#self.onStopped() #activate the output of the box





# if i==4:
#     print ("put")
#     pass
# elif distance<1.5:
#     print('离我太近啦，请靠后一些')
# elif self.distance>2:
#     print('离我太远啦，请靠前一些')
# else:
#     print ("put")
#     pass