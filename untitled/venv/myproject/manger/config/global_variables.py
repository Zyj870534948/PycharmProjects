#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/9

import sys
# sys.path.append("..")

import globalvar as gl
import socket
# from connect_pepper import Open_pepper
# from function_pepper import Func

# test
from manger.connect_pepper import Open_pepper
from manger.function_pepper import Func
from api_standby import Standby_api
# 设置全局变量
# 初始化全局变量函数
gl._init()


# 连接pepper机器人，并获取session

# 或者linux
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    return str(ip)



gl.set_value('ip', get_ip())
open_pepper = Open_pepper()




#连接机器人
# test
# open_pepper.star_pepper('192.168.43.179')
open_pepper.star_pepper(get_ip())

gl.set_value('connection_url', 'tcp://' + str(get_ip()) + ':9559')

session = open_pepper.get_session()
gl.set_value('session', session)

#机器人的功能
func = Func()
gl.set_value('func', func)

# test
gl.set_value('robot_ip', get_ip())
# gl.set_value('robot_ip', '192.168.43.179')

#正式服地址
# gl.set_value('api_ip', 'api.pepper.nplusgroup.com')
#pepper更新版本测试服地址
gl.set_value('api_ip', 'api.robot.nplus5.com')


# 设置每台pepper机器人所特有的Id
def get_ID(session):
    memory = session.service("ALMemory")
    bodyId = memory.getData("Device/DeviceList/ChestBoard/BodyId")
    return bodyId


# test
# gl.set_value('pepper_id', 'AP990438A00Y6A100377')
gl.set_value('pepper_id', get_ID(open_pepper.get_session()))

gl.set_value('check', 0)


# *****************linux写法*************************************


def get_webview_url():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    port = '8888'
    webview_ip = 'http://' + str(ip) + ':' + port + '/'
    return webview_ip


gl.set_value('homepage_url', get_webview_url())


# *****************linux写法*************************************


#***********************版本信息*********************************
#机器人系统版本
gl.set_value('robot_edition', '1.8A')
#更新版本号
gl.set_value('edition', '2.1.0')
#更新日期
gl.set_value('update_date', '190121')
#版本状态:正式版是R，测试版本和发布之前的版本用Beta和RC
gl.set_value('state_edition', 'R')
#***********************版本信息*********************************

########################设置机器人名字##################################
def getName():
    result = Standby_api().standby_get()
    pepperName=result['robotName'].encode('utf-8')
    return pepperName

gl.set_value('pepperName', getName())
##########################################################