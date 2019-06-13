#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__
WordRecognized
memory = session.service("ALMemory")
print memory.getData("WordRecognized")
'''


"""Example: Use ALSpeechRecognition Module"""

import qi
import argparse
import sys
import time


def main(session):
    audio_recorder = session.service("ALAudioRecorder")

    audio_recorder.startMicrophonesRecording("/data/home/nao/nplus/MrZhu/pytest.wav", "wav", 16000, (0,0,1,0))

    time.sleep(3)
    audio_recorder.stopMicrophonesRecording()






if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
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