#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/21


from naoqi import *
import config.globalvar as gl
import config.global_variables
import requests
import logging



# create python module
class myModule(ALModule):

    def pythondatachanged(self, strVarName, value):
        # print "datachanged", strVarName, " ", value, " "

        file_handle = open('status.txt', mode='r')
        check = file_handle.read(1)

        if check == "0":

            file_handle = open('status.txt', mode='w')
            file_handle.write('1')

            if len(value[1]) - 1:
                # test
                gl.get_value('func').speech(gl.get_value('session'),
                                            "^start(Stand/Gestures/BowShort_1)你好^wait(Stand/Gestures/BowShort_1)")
                resp = requests.get(url='http://127.0.0.1:20001/xunfei/Main/stateXunfei.json')
                gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')
                # print '服务开启'
                logging.info('开启服务')

    # def _pythonPrivateMethod(self, param1, param2, param3):
    #     global check
