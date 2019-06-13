#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__
'''

NAO_IP = "192.168.3.33"     #在机器人外部运行
# NAO_IP = "127.0.0.1"      # 放在机器人本地

import sys
import os
path = os.path.dirname(__file__)
if not path in sys.path:
    sys.path.append(path)

from optparse import OptionParser
import naoqi
import time

from Answer_AIUI import AIUI
from Question_KeDaXunFei_WavToStr import KeDaXunFei


class SoundReceiverModule(naoqi.ALModule):

    def __init__( self, strModuleName, strNaoIp ):
        try:
            naoqi.ALModule.__init__(self, strModuleName );
            self.BIND_PYTHON( self.getName(),"callback" );
            self.strNaoIp = strNaoIp;
            self.outfile = None;
            self.aOutfile = [None]*(4-1); # ASSUME max nbr channels = 4
        except BaseException, err:
            print( "ERR: abcdk.naoqitools.SoundReceiverModule: loading error: %s" % str(err) );

    def __del__( self ):
        print( "INF: abcdk.SoundReceiverModule.__del__: cleaning everything" );
        self.stop();

    def start( self ):      #设置麦克风录制方向
        audio = naoqi.ALProxy( "ALAudioDevice", self.strNaoIp, 9559 );
        nNbrChannelFlag = 3; # ALL_Channels: 0,  AL::LEFTCHANNEL: 1, AL::RIGHTCHANNEL: 2; AL::FRONTCHANNEL: 3  or AL::REARCHANNEL: 4.
        nDeinterleave = 0;
        nSampleRate = 16000;
        audio.setClientPreferences( self.getName(),  nSampleRate, nNbrChannelFlag, nDeinterleave ); # setting same as default generate a bug !?!
        audio.subscribe( self.getName() );
        print( "INF: SoundReceiver: started!" );

        # on romeo, here's the current order:
        # 0: right;  1: rear;   2: left;   3: front,

    def start_EnergyComputation(self):      #打开麦克风能量监听
        audio = naoqi.ALProxy("ALAudioDevice", self.strNaoIp, 9559)
        audio.enableEnergyComputation()

    def start_recording( self ,path):       #打开麦克风录制
        audio = naoqi.ALProxy("ALAudioDevice", self.strNaoIp, 9559)
        audio.startMicrophonesRecording(path)

    def stop_recording( self ):       #关闭麦克风录制
        audio = naoqi.ALProxy("ALAudioDevice", self.strNaoIp, 9559)
        audio.stopMicrophonesRecording()

    def stop_EnergyComputation(self):       #关闭麦克风能量监听
        audio = naoqi.ALProxy("ALAudioDevice", self.strNaoIp, 9559)
        audio.disableEnergyComputation()

    def get_FrontMicEnergy(self):       #获取前置麦克风能量大小
        audio = naoqi.ALProxy("ALAudioDevice", self.strNaoIp, 9559)
        return audio.getFrontMicEnergy()

    def stop( self ):       #中止所有监听
        print( "INF: SoundReceiver: stopping..." );
        audio = naoqi.ALProxy( "ALAudioDevice", self.strNaoIp, 9559 );
        audio.unsubscribe( self.getName() );
        print( "INF: SoundReceiver: stopped!" );
        if( self.outfile != None ):
            self.outfile.close();


def main():

    pepperSay = naoqi.ALProxy("ALAnimatedSpeech", NAO_IP, 9559)

    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    myBroker = naoqi.ALBroker("myBroker",
        "0.0.0.0",  # listen to anyone
        0,  # find a free port and use it
        pip,  # parent broker IP
        pport)  # parent broker port


    global SoundReceiver

    SoundReceiver = SoundReceiverModule("SoundReceiver", pip)
    SoundReceiver.start()
    SoundReceiver.start_EnergyComputation()

    # t1 = time.clock()
    # for i in range(100):
    #     time.sleep(0.1)
    #     print SoundReceiver.get_FrontMicEnergy()
    # t2 = time.clock()
    # print t2 - t1

    an = AIUI()
    qu = KeDaXunFei()
    # print an.getAnswer("开心不")


    str = ""
    Dialog = True
    f1 = False
    f2 = False
    energy = 2600
    t = [0,0,0,0,0,0]
    while Dialog:
        t[0] = time.clock()
        SoundReceiver.start_recording("/data/home/nao/nplus/MrZhu/out.ogg")
        t[1] = time.clock()
        for i in range(6):
            time.sleep(0.1)
            if SoundReceiver.get_FrontMicEnergy() > energy:
                f1 = True
        for i in range(3):
            time.sleep(0.1)
            if SoundReceiver.get_FrontMicEnergy() > energy:
                f2 = True

        t[2] = time.clock()

        if f2:
            f2 = False
            for i in range(12):
                print "+++"
                for j in range(3):
                    time.sleep(0.1)
                    if SoundReceiver.get_FrontMicEnergy() > energy:
                        f2 = True
                if f2:
                    f2 = False
                else:
                    break

            t[3] = time.clock()

            SoundReceiver.stop_recording()
            os.rename("/data/home/nao/nplus/MrZhu/out.ogg", "/data/home/nao/nplus/MrZhu/out.wav")

            t[4] = time.clock()

            str = qu.getStr("/data/home/nao/nplus/MrZhu/out.wav")

        else :
            if f1:
                f1 = False
                SoundReceiver.stop_recording()
                os.rename("/data/home/nao/nplus/MrZhu/out.ogg", "/data/home/nao/nplus/MrZhu/out.wav")
                str = qu.getStr("/data/home/nao/nplus/MrZhu/out.wav")
            else :
                SoundReceiver.stop_recording()
                os.rename("/data/home/nao/nplus/MrZhu/out.ogg", "/data/home/nao/nplus/MrZhu/out.wav")

        f1 = False
        f2 = False

        if "退出" in str:
            break
        if str != "":
            print str , type(str)
            str = an.getAnswer(str)

            t[5] = time.clock()

            pepperSay.say(str)
        print "----------"
        print "开启时间：" , t[1] - t[0]
        print "基本录制时间：", t[2] - t[1]
        print "额外录制时间：", t[3] - t[2]
        print "关闭转化时间：", t[4] - t[3]
        print "结束时间：", t[5] - t[4]
        print "总时间：", t[5] - t[0]

        str = ""



    # SoundReceiver.start_recording("/data/home/nao/nplus/MrZhu/out.ogg")
    # SoundReceiver.stop_recording()
    # os.rename("/data/home/nao/nplus/MrZhu/out.ogg","/data/home/nao/nplus/MrZhu/out.wav")


    SoundReceiver.stop_EnergyComputation()


if __name__ == "__main__":
    main()


    pass
