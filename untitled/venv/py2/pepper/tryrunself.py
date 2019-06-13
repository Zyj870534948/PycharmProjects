#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''
import time

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.3.71", 9559)
tts.say("")