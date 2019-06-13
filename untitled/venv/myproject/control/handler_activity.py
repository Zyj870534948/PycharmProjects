#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"sidalin"

import tornado.web
from api_activity import Activity_api
from generate_code import GenerateCode
import listener
import handler_all
from handler_all import Speech
from compare import Compare
import manger.config.global_variables
import manger.config.globalvar as gl
import time
from funcName import variable
from log import log1

# 功能界面也就是业务界面
class ActivityHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        handler_all.changePage('homePage')
        handler_all.changeFlag(False)
        operationId = self.get_argument('operationId')
        activityId = self.get_argument('activityId')
        menuId = self.get_argument('menuId')
        ad = Activity_api()
        avtivityDate = ad.main(activityId)
        if avtivityDate != False:
            url = 'http://h5.robot.nplus5.com/#/activity/' + activityId
            # url='www.baidu.com'
            activityName = avtivityDate['activityName']
            introduce = avtivityDate['activityIntroduce']
            #生成二维码图片
            g = GenerateCode()
            #保存二维码的图片
            g.save_code(url, 'code')
            self.render('Activity.html', activityName=activityName, introduce=introduce, menuId=menuId,
                        operationId=operationId)
        else:
            self.render('Activity.html', activityName='get data error', introduce='get data error', menuId=menuId,
                        operationId=operationId)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        msg = msg['listen']
        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            handler_all.changeFlag(False)
            runMsg = {'pageName': variable['activityContent'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')
