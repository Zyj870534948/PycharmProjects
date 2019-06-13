#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import tornado.web
from api_personalCenter import PersonalCenter_api
from api_homePage import HomePage_api
import manger.config.global_variables
import manger.config.globalvar as gl
import listener
import handler_all
from handler_all import Speech
from compare import Compare
import time
from funcName import variable
from log import log1




# 个人中心界面
class PersonalCenterHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        handler_all.changePage('homePage')
        handler_all.changeFlag(True)
        hp = HomePage_api()
        hpData = hp.main()
        hpName =''
        for h in hpData:
            hpName=hpName+h['menuName']+','

        pc = PersonalCenter_api()
        result=pc.main()

        buyDate=str(result['purchaseTime']).split(" ")[0]
        address=result['customerAddress']
        print('----------------')
        print(buyDate)
        print('----------------')
        myIntruduce='上海御慕智能科技有限公司'
        robotEdition=gl.get_value('robot_edition')
        currentEdition=gl.get_value('robot_edition')+'_'+gl.get_value('edition')+'.'+gl.get_value('update_date')+'_'+gl.get_value('state_edition')
        newEdition=result['version']
        self.render('PersonalCenter.html',hpName=hpName,buyDate=buyDate,address=address,myIntruduce=myIntruduce,robotEdition=robotEdition,currentEdition=currentEdition,newEdition=newEdition)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        msg = msg['listen']
        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['personal'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')