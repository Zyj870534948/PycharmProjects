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





    # SoundReceiver.start_recording("/data/home/nao/nplus/MrZhu/out.ogg")
    SoundReceiver.stop_recording()
    os.rename("/data/home/nao/nplus/MrZhu/out.ogg","/data/home/nao/nplus/MrZhu/out.wav")


    SoundReceiver.stop_EnergyComputation()


if __name__ == "__main__":
    main()


    pass
