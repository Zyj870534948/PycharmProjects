#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
import time
import argparse
import sys
import numpy
import Image

class PepperFunc:
    def __init__(self,IP):
        self.ip = IP
        self.pepperSay = ALProxy("ALAnimatedSpeech", IP, 9559)
        self.pepperLocal = ALProxy("ALNavigation", IP, 9559)
        self.pepperweb = ALProxy("ALTabletService", IP, 9559)

    def openweb(self,url):
        self.pepperweb.showWebview(url)

    def speak(self,saycontent):
        self.pepperSay.say(saycontent)

    def Explore_map(self,radius):
        self.pepperLocal.explore(radius)
        path = self.pepperLocal.saveExploration()
        print "地图路径: \"" + path + "\""

    def Loading_map(self,path):
        self.pepperLocal.loadExploration(path)

    def Open_localization(self,guess):
        self.pepperLocal.relocalizeInMap(guess)
        self.pepperLocal.startLocalization()

    def Relocalize(self,guess):
        self.pepperLocal.relocalizeInMap(guess)

    def Move_In_Map(self,coordinate):
        self.pepperLocal.navigateToInMap(coordinate)

    def Close_localization(self):
        self.pepperLocal.stopLocalization()

    def Stop_explore(self):
        self.pepperLocal.stopExploration()

    def Read_coordinate(self):
        return self.pepperLocal.getRobotPositionInMap()[0]

    def Get_Map(self):
        return self.pepperLocal.getMetricalMap()

    def Show_Map(self):
        result_map = self.Get_Map()
        map_width = result_map[1]
        map_height = result_map[2]
        img = numpy.array(result_map[4]).reshape(map_width, map_height)
        img = (100 - img) * 2.55  # from 0..100 to 255..0
        img = numpy.array(img, numpy.uint8)
        Image.frombuffer('L', (map_width, map_height), img, 'raw', 'L', 0, 1).show()

if __name__ == '__main__':
    p=PepperFunc('192.168.3.71')
    # p.Explore_map(3)

    # path = "/home/nao/.local/share/Explorer/2019-03-29T015218.973Z.explo"
    # #"/home/nao/.local/share/Explorer/2019-03-28T095414.137Z.explo"
    # p.Loading_map(path)
    # p.Open_localization([0.,0.])

    while 1:
        print p.Read_coordinate()
        time.sleep(0.5)

    # -0.7225240468978882, -1.0624651908874512

    # print p.Read_coordinate()

    # p.Move_In_Map([-0.2,0.2])
    # p.Move_In_Map([0.,0.,0.])

    # p.speak("你好")
    # p.openweb("http://192.168.3.20:8083/main")
    # p.openweb("http://198.18.0.1/apps/boot-config/preloading_dialog.html")

    # p.Close_localization()


    # print p.Get_Map()
    # p.Show_Map()

    # # p.Relocalize([0.0,0.0,0.0])

    # # print p.Read_coordinate()
    # p.Close_localization()
    # p.Stop_explore()


