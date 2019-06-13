#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
from naoqi import ALProxy

class PepperFunc:
    def __init__(self,IP):
        self.ip = IP
        self.pepperSay = ALProxy("ALAnimatedSpeech", IP, 9559)

    def speak(self,saycontent):
        self.pepperSay.say(saycontent)

if __name__ == '__main__':
    p=PepperFunc('192.168.3.18')
    p.speak('请你出去')
