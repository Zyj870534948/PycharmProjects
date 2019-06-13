#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import time


tts = ALProxy('ALTextToSpeech', "192.168.3.18", 9559)
ttsStop = ALProxy('ALTextToSpeech', "192.168.3.18", 9559, True) #Create another proxy as wait is blocking if audioout is remote

bIsRunning = False
ids = []

def onUnload():
    global bIsRunning
    for id in ids:
        try:
            ttsStop.stop(id)
        except:
            pass
    while( bIsRunning ):
        time.sleep( 0.2 )

def onInput_onStart():
    global bIsRunning
    bIsRunning = True
    try:
        sentence = "\RSPD=100\ "
        sentence += "\VCT=100\ "
        sentence += "你好"
        sentence +=  "\RST\ "
        id = tts.post.say(str(sentence))
        ids.append(id)
        tts.wait(id, 0)
    finally:
        try:
            ids.remove(id)
        except:
            pass
        if( ids == [] ):
            onStopped() # activate output of the box
            bIsRunning = False

def onInput_onStop():
    onUnload()



onInput_onStart()




