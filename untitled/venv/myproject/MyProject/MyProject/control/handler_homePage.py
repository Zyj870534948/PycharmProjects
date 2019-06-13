#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"sidalin"

import tornado.web
from api_homePage import HomePage_api
import handler_all
from handler_all import Speech
import listener
from compare import Compare
import manger.config.global_variables
import manger.config.globalvar as gl
import time
from logtiming import log1
from funcName import variable


# 首页
class HomePageHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        handler_all.changePage('homePage')
        handler_all.changeFlag(True)
        hp = HomePage_api()
        self.home_date = hp.main()
        if self.home_date:
            self.render('HomePage.html', homeDate=self.home_date)
        else:
            self.home_date=[]
            self.render('HomePage.html', homeDate=self.home_date)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        #六大类返回的接口数据
        homepageDate = self.home_date
        homepageList=[]
        d={}
        #homepageList:[{'menuName':'模块一,'menuId':'37'},{'menuName':'模块二,'menuId':'38'}]
        if homepageDate:
            for h in homepageDate:
                d['menuName']=h['menuName']
                d['menuId']=h['id']
                homepageList.append(d)
                d = {}

        #获取语音相似度最大的值best_compare{'menuId':37,'compareValue':0.6}
        best_compare = None
        for index,value in enumerate(homepageList):
            if Compare().conmpare(value['menuName'],listen)>0.4:
                if best_compare==None:
                    best_compare = {}
                    #功能的menuId和相似度的值
                    best_compare['menuId'],best_compare['compareValue']=value['menuId'], Compare().conmpare(value['menuName'], listen)
                elif best_compare['compareValue'] < Compare().conmpare(value['menuName'], listen):
                    best_compare['menuId'], best_compare['compareValue'] = value['menuId'],Compare().conmpare(value['menuName'], listen)


        if best_compare != None:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            #往日志中插入信息
            runMsg = {'pageName': variable['homePage'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'),gl.get_value('homepage_url')+'pepper/FUNCTION?menuId='+ str(best_compare['menuId']))


        if Compare().conmpare(u'返回首页', listen) > 0.4:
            Speech().speech('好的请稍等')
            flag_speech = False
            runMsg = {'pageName': variable['homePage'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')
        if Compare().conmpare(u'过来', listen) > 0.4:
            Speech().speech('好的请稍等')
            gl.get_value('func').stop_behavior(gl.get_value('session'), 'walking-148f83/behavior_1')
            gl.get_value('func').start_behavior(gl.get_value('session'), 'walking-148f83/behavior_1')
