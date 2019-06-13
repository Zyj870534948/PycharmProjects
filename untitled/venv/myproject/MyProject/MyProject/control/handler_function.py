#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import tornado.web
from api_function import Function_api
import handler_all
from handler_all import Speech
import listener
from compare import Compare
import manger.config.global_variables
import manger.config.globalvar as gl
import logging,time
from logtiming import log1
from funcName import variable


#功能界面也就是业务界面
class FunctionHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        handler_all.changePage('function')
        handler_all.changeFlag(False)
        menuId=self.get_argument('menuId')
        f = Function_api()
        self.result = f.main(menuId)['data']
        self.render('Function.html',funcdata=self.result)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        # 六大类返回的接口数据
        functionDate = self.result

        functionList = []
        d = {}
        # functionList:[{'operationName':'信息介绍,'menuId':'37','operationId':7,'fcode':'INTRUDUCE}]
        if functionDate:
            for h in functionDate:
                d['operationName'] = h['operationName']
                d['menuId'] = h['menuId']
                d['operationId'] = h['id']
                d['fcode'] = h['fcode']
                functionList.append(d)
                d={}

        # 获取语音相似度最大的值best_compare{'menuId':37,'compareValue':0.6,'fcode':'INTRCDUCE','operationId':7}
        best_compare = None
        for index, value in enumerate(functionList):
            if Compare().conmpare(value['operationName'], listen) > 0.4:
                if best_compare == None:
                    best_compare = {}
                    # 功能的menuId和相似度的值
                    best_compare['menuId'], best_compare['compareValue'],best_compare['fcode'],best_compare['operationId']= value['menuId'], Compare().conmpare(
                        value['operationName'], listen),value['fcode'],value['operationId']
                elif best_compare['compareValue'] < Compare().conmpare(value['operationName'], listen):
                    best_compare['menuId'], best_compare['compareValue'], best_compare['fcode'], best_compare[
                        'operationId'] = value['menuId'], Compare().conmpare(
                        value['operationName'], listen), value['fcode'], value['operationId']

        if best_compare != None:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['function'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'),
                                         gl.get_value('homepage_url')+ 'pepper/' + best_compare['fcode']+'?menuId='+str(best_compare['menuId'])+'&operationId='+str(best_compare['operationId']))

        if Compare().conmpare(u'返回首页', listen) > 0.4:
            self.endTime = time.time()
            Speech().speech('好的请稍等')
            flag_speech = False
            runMsg = {'pageName': variable['function'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')