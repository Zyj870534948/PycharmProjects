#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__
WordRecognized
memory = session.service("ALMemory")
print memory.getData("WordRecognized")
'''

"""Example: Use setParameter Method"""

"""Example: Use ALSpeechRecognition Module"""

import qi
import argparse
import sys
import time
import urllib, urllib2, sys,json
import requests
import base64


# def main(session):
#     """
#     This example uses the ALSpeechRecognition module.
#     """
#     # Get the service ALSpeechRecognition.
#
#     asr_service = session.service("ALSpeechRecognition")
#     sound_detect_service = session.service("ALSoundDetection")
#     memory = session.service("ALMemory")
#
#
#     asr_service.setLanguage("English")
#
#     # Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
#     vocabulary = ["Hello", "What's your name", "everybody", "The computer is out of order.","big","home","good","yes"]
#     asr_service.setVocabulary(vocabulary, False)
#
#     # Start the speech recognition engine with user Test_ASR
#     asr_service.pause(False)
#     for i in range(1):
#         asr_service.subscribe("Test_ASR") #开启短语监听
#         # print 'Speech recognition engine started'
#         print memory.getData("SpeechDetected")
#         # time.sleep(0.5)
#         time.sleep(3)
#         asr_service.unsubscribe("Test_ASR")
#         print memory.getData("WordRecognized")[0]
#     asr_service.pause(True)
#     print memory.getDataListName()

flag = False

def wavtotext():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=T21059gyQkCIIQit0xu7P4D9&client_secret=nupLEUtPdgGQEWqY3r4neFQTEpoZtwz8'
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        content = json.loads(content)
        print(content["access_token"])

    f = open("/data/home/nao/nplus/MrZhu/pytest.wav", "rb")
    fl = f.read()
    speech = base64.b64encode(fl)
    flen = len(fl)
    f.close()

    token = content["access_token"].encode("utf-8")
    # print token, type(token)

    url = "http://vop.baidu.com/server_api"  # + "?access_token=" + content["access_token"]
    header = {'Content-Type': 'application/json'}
    body = {
        "format": "wav",
        "rate": 16000,
        "channel": 1,
        "cuid": "04:92:26:D6:20:B1",
        "token": token,
        "dev_pid": 1737,
        "speech": speech,
        "len": flen
    }
    body = json.dumps(body)
    r = requests.post(url=url, data=body, headers=header)
    t = json.loads(r.text.encode("utf-8"))
    text = t["result"][0]
    print text
    if text == "Please out" or text == "please out" or text == "Please Out" or text == "please Out":
        global flag
        flag = True
    try:
        re = requests.get("http://sandbox.api.simsimi.com/request.p?key=c4c118f2-a89b-4cfe-9563-359c39046bb2&lc=en&ft=1.0&text=" + text)
        tb = json.loads(re.text.encode("utf-8"))
        try:
            return tb["response"]
        except:
            pass
    except:
        pass



def main(session):
    asr_service = session.service("ALSpeechRecognition")
    memory = session.service("ALMemory")
    audio_recorder = session.service("ALAudioRecorder")
    tts = session.service("ALTextToSpeech")

    asr_service.pause(True)
    asr_service.setLanguage("English")
    asr_service.setVocabulary(["Hello","help"], False)
    asr_service.pause(False)
    audio_recorder.startMicrophonesRecording("/data/home/nao/nplus/MrZhu/pytest.wav", "wav", 16000, (0, 0, 1, 0))
    i = 1
    k = 1
    asr_service.subscribe("Test_ASR")
    while i:
        # print "SpeechDetected=" + str(memory.getData("SpeechDetected")),
        if memory.getData("SpeechDetected")==1:
            # print "start  k=" + str(k) + "i=" + str(i)
            k = 2

        if k > 1 and memory.getData("SpeechDetected")==0:
            # print "outlittle  k=" + str(k) + "i=" + str(i)
            k += 1
        if k >= 10 and memory.getData("SpeechDetected")==0:
            # print "end  k=" + str(k) + "i=" + str(i)
            audio_recorder.stopMicrophonesRecording()
            k = 1
            i = 1
            try:
                text = wavtotext()
            except:
                text = ""
            if text == None:
                text = ""
            print text
            tts.say(text)
            print flag
            # break
            if flag:
                break
            audio_recorder.startMicrophonesRecording("/data/home/nao/nplus/MrZhu/pytest.wav", "wav", 16000,(0, 0, 1, 0))

        if k==1 and i>=50:
            print "again"
            audio_recorder.stopMicrophonesRecording()
            audio_recorder.startMicrophonesRecording("/data/home/nao/nplus/MrZhu/pytest.wav", "wav", 16000,(0, 0, 1, 0))
            i = 1

        elif i>=150:
            print "SpeechDetected worry"
            audio_recorder.stopMicrophonesRecording()
            try:
                text = wavtotext()
            except:
                text = ""
            if text == None:
                text = ""
            print text
            tts.say(text)
            # print flag
            # break
            if flag:
                break
            audio_recorder.startMicrophonesRecording("/data/home/nao/nplus/MrZhu/pytest.wav", "wav", 16000,(0, 0, 1, 0))
            k = 1
            i = 1

        time.sleep(0.1)
        i += 1
    asr_service.unsubscribe("Test_ASR")



if __name__ == "__main__":
    import os
    import socket, fcntl, struct
    ifname = 'wlan0'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=ip,
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)