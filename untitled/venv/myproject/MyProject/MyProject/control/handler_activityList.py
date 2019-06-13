#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import tornado.web
import handler_all
from handler_all import Speech
import listener
from compare import Compare
import manger.config.global_variables
import manger.config.globalvar as gl
import logging
from api_activityList import ActivityList_api
import time
from funcName import variables
from logtiming import log1

#活动列表页面
class ActivityListHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        handler_all.changePage('activity')
        handler_all.changeFlag(False)
        self.operationId = self.get_argument('operationId')
        self.menuId = self.get_argument('menuId')
        al = ActivityList_api()
        self.activityData = al.main(self.operationId)['data']
        self.render('ActivityList.html', activityData=self.activityData,menuId=self.menuId,operationId=self.operationId)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        # 六大类返回的接口数据
        activityData = self.activityData
        activityList = []
        d = {}
        # activityList:[{'activityName':'活动一,'menuId':'37','operationId':13,'activityId':1}]
        if activityData:
            for h in activityData:
                d['activityName'] = h['activityName']
                d['menuId'] = self.menuId
                d['operationId']=h['operationId']
                d['activityId']=h['activityId']
                activityList.append(d)
                d = {}

        # 获取语音相似度最大的值best_compare{'compareValue':0.5,'menuId':'37','operationId':13,'activityId':1}
        best_compare = None
        for index, value in enumerate(activityList):
            if Compare().conmpare(value['activityName'], listen) > 0.4:
                if best_compare == None:
                    best_compare = {}
                    # 功能的menuId和相似度的值
                    best_compare['menuId'], best_compare['compareValue'],best_compare['operationId'],best_compare['activityId'] = value['menuId'], Compare().conmpare(
                        value['activityName'], listen),value['operationId'],value['activityId']
                elif best_compare['compareValue'] < Compare().conmpare(value['activityName'], listen):
                    best_compare['menuId'], best_compare['compareValue'], best_compare['operationId'], best_compare[
                        'activityId'] = value['menuId'], Compare().conmpare(
                        value['activityName'], listen), value['operationId'], value['activityId']

        if best_compare != None:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['activityList'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'),
                                         gl.get_value('homepage_url') + 'pepper/ACTIVITYCONTENT?activityId='+str(best_compare['activityId'])+'&operationId='+str(best_compare['operationId'])+'&menuId=' + str(
                                             best_compare['menuId']))

        if Compare().conmpare(u'返回首页', listen) > 0.4:
            Speech().speech('好的请稍等')
            flag_speech = False
            runMsg = {'pageName': variable['activityList'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')

