#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/22
import logging, json
import tornado.web
import requests
import manger.config.global_variables
import manger.config.globalvar as gl
from api_problem_analysis import Problem_api
import listener
from compare import Compare
from api_standby import Standby_api
from generate_code import GenerateCode
from api_func import Func_api
from api_jieshao import Jieshao_api
from api_xiaotieshi import Xiaotieshi_api
from api_question import Question_api
from api_problem_sort import ProblemSort_api
from api_game import Game_api
from logtiming import log1
import time
from funcName import variable

page = ''
flag_speech = True


def changePage(pageName):
    global page
    page = pageName

def changeFlag(statuFlag):
    global flag_speech
    flag_speech = statuFlag

class Speech:
    def speech(self, speech):
        gl.get_value('func').speech(gl.get_value('session'), speech)

class StopAllBehavior:
    def stopAllBehavior(self):
        di=[{'name':'takephoto-d9c45c/behavior_1'},{'name':'main-6e9d8d/emotion'},{'name':'dance1'},{'name':'test-115f38/behavior_1'},{'name':'handshake-aa1938/behavior_1'}]
        for index,value in enumerate(di):
            gl.get_value('func').stop_behavior(gl.get_value('session'), value['name'])



# 待机界面
class StandbyHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        global page
        page = 'standby'
        global flag_speech
        flag_speech = False
        url = 'http://' + gl.get_value('api_ip') + '/api/robot/' + gl.get_value(
            'pepper_id') + '/version/' + gl.get_value('edition')
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.put(url=url, headers=headers)
        print('edition'+str(resp.status_code))
        stopAll = StopAllBehavior()
        stopAll.stopAllBehavior()
        # 从文件中读取全局变量用于两个线程之间
        file_handle = open('status.txt', mode='w')
        file_handle.write('0')
        result = Standby_api().standby_get()
        if result ==None or len(result)==0:
            iconUrl='../static/images/1.png'
        else:
            iconUrl=result['standbyUrl']
        if result == None or len(result) == 0:
            typeid = 1
        elif result['type'] == 'L':
            typeid = 1
        elif result['type'] == 'R':
            typeid = 2
        else:
            typeid = 1

        resp = requests.get(url='http://127.0.0.1:20001/xunfei/Main/stateXunfei.json')
        print('xunfei' + str(resp.status_code))
        if typeid == 1:
            self.render('daiji1.html',iconUrl=iconUrl)
        else:
            self.render('daiji2.html',iconUrl=iconUrl)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        if Compare().conmpare(u'你好', listen) > 0.4:
            s="^start(Stand/Gestures/BowShort_1)你好,我是"+gl.get_value('pepperName')+"^wait(Stand/Gestures/BowShort_1)"
            self.endTime=time.time()
            gl.get_value('func').speech(gl.get_value('session'),s)
            # 往日志中插入运行时间
            runMsg = {'pageName': variable['standby'], 'startTime': self.startTime, 'endTime': self.endTime}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')

        if Compare().conmpare(u'首页', listen) > 0.4:
            Speech().speech('好的请稍等')
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')


# 功能界面
class FuncHandler(tornado.web.RequestHandler):
    def get(self):
        stopAll = StopAllBehavior()
        stopAll.stopAllBehavior()
        global page
        page = 'func'
        global flag_speech
        flag_speech = True
        self.render('zhujiao.html')
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        f = Func_api()
        json = f.main_get()
        # 获得接口中keyname用于关键字监听
        keyword_li = []
        if json:
            for j in json['data']:
                # test
                if j['functionName'] != u'待机':
                    keyword_li.append(j['functionName'])
        keyword_di = self.jump_url(keyword_li)
        best_compare = None
        for k, v in keyword_di.items():
            if Compare().conmpare(k, listen) > 0.4:
                if best_compare == None:
                    best_compare = {}
                    best_compare['v'], best_compare['c'] = v, Compare().conmpare(k, listen)
                elif best_compare['c'] < Compare().conmpare(k, listen):
                    best_compare['v'], best_compare['c'] = v, Compare().conmpare(k, listen)

        if best_compare != None:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'), best_compare['v'])

        if Compare().conmpare(u'返回首页', listen) > 0.4:
            Speech().speech('好的请稍等')
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'func')
        if Compare().conmpare(u'过来', listen) > 0.4:
            Speech().speech('好的请稍等')
            gl.get_value('func').stop_behavior(gl.get_value('session'), 'walking-148f83/behavior_1')
            gl.get_value('func').start_behavior(gl.get_value('session'), 'walking-148f83/behavior_1')

    # 页面的跳转
    def jump_url(self, li):
        di = {}
        for i in li:
            if i == u'课堂':
                di[i] = gl.get_value('homepage_url') + 'sort'
            if i == u'信息介绍':
                di[i] = gl.get_value('homepage_url') + 'jieshao'
            if i == u'中英翻译':
                di[i] = gl.get_value('homepage_url') + 'translation'
            if i == u'信息搜索':
                di[i] = gl.get_value('homepage_url') + 'message_search'
            if i == u'小贴士':
                di[i] = gl.get_value('homepage_url') + 'xiaotieshi'
            if i == u'小游戏':
                di[i] = gl.get_value('homepage_url') + 'yule'
            if i == u'自定义问答':
                di[i] = gl.get_value('homepage_url') + 'daogou'
            if i == u'智能饮水机':
                di[i] = gl.get_value('homepage_url') + 'water'
            if i == u'小贴士':
                di[i] = gl.get_value('homepage_url') + 'xiaotieshi'

        return di


# 助教介绍界面
class JieshaoHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        self.operationId = self.get_argument('operationId')
        self.menuId = self.get_argument('menuId')
        j = Jieshao_api()
        json = j.main_get(self.operationId)
        # 获得接口中keyname用于关键字监听
        keyword_di = {}
        if json:
            for j in json['data']:
                keyword_di[j['title']] = j['materialId']
        self.keyword_di = keyword_di
        self.render('zhujiaojieshao.html', json=json['data'],menuId=self.menuId,operationId=self.operationId)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        best_compare = None
        for k, v in self.keyword_di.items():
            if Compare().conmpare(k, listen) > 0.5:
                if best_compare == None:
                    best_compare = {}
                    # value中的值是比较的匹配度的值
                    best_compare['b_id'], best_compare['value'] = v, Compare().conmpare(
                        k, listen)
                elif best_compare['value'] <= Compare().conmpare(k.decode('utf-8'), listen):
                    best_compare['b_id'], best_compare['value'] = v, Compare().conmpare(
                        k, listen)
        if best_compare != None:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['jieshao'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'),
                                         gl.get_value('homepage_url') + 'jieshao/content?classId=' + str(
                                             best_compare['b_id'])+'&menuId='+str(self.menuId)+'&operationId='+str(self.operationId))

        if Compare().conmpare(u'返回首页', listen) > 0.4:
            Speech().speech('好的请稍等')
            flag_speech = False
            runMsg = {'pageName': variable['jieshao'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')



# 助教介绍展示界面
class School_introductionHandler(tornado.web.RequestHandler):
    def get(self):
        self.operationId = self.get_argument('operationId')
        self.menuId = self.get_argument('menuId')
        global page
        page = 'school'
        global flag_speech
        flag_speech = False
        if listener.instance.exist('chat'):
            listener.instance.remove_listener('chat')
        if listener.instance.exist('view'):
            listener.instance.remove_listener('view')
        classId = self.get_argument('classId')
        self.render('jieshao.html', classId=classId,operationId=self.operationId,menuId=self.menuId)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        msg = msg['listen']
        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')


# 知识点分类的处理类
class PSortHandler(tornado.web.RequestHandler):
    def get(self):
        global page
        page = 'zhishidiansort'
        global flag_speech
        flag_speech = True
        p = ProblemSort_api()
        data_list = p.main_get()
        # 获得接口中keyname用于关键字监听
        keyword_di = {}
        for j in data_list:
            keyword_di[j['categoryName']] = j['id']
        self.keyword_di = keyword_di

        self.render('zhishidian_fenlei.html', json=data_list)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        best_compare = None
        for k, v in self.keyword_di.items():
            if Compare().conmpare(k, listen) > 0.5:
                if best_compare == None:
                    best_compare = {}
                    # value中的值是比较的匹配度的值
                    best_compare['b_id'], best_compare['value'] = v, Compare().conmpare(
                        k, listen)
                elif best_compare['value'] <= Compare().conmpare(k.decode('utf-8'), listen):
                    best_compare['b_id'], best_compare['value'] = v, Compare().conmpare(
                        k, listen)

        if best_compare != None:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'),
                                         gl.get_value('homepage_url') + 'problem_sol?categoryId=' + str(best_compare[
                                                                                                            'b_id']))

        if Compare().conmpare(u'返回首页', listen) > 0.4:
            Speech().speech('好的请稍等')
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'func')


# 知识点的处理类
class Problem_SolutionHandler(tornado.web.RequestHandler):
    def get(self):
        global page
        page = 'zhishidian'
        global flag_speech
        flag_speech = True
        self.categoryId = self.get_argument('categoryId')
        p = Problem_api()
        json1 = p.problem_api_get(int(self.categoryId))
        # 获得接口中keyname用于关键字监听
        keyword_di = {}
        if json1['data']:
            for j in json1['data']:
                keyword_di[j['title']] = j['id']

        self.keyword_di = keyword_di
        self.render('zhishidian.html', json=json1['data'], categoryId=self.categoryId)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        best_compare = None
        for k, v in self.keyword_di.items():
            if Compare().conmpare(k, listen) > 0.5:
                if best_compare == None:
                    best_compare = {}
                    # value中的值是比较的匹配度的值
                    best_compare['b_id'], best_compare['value'] = v, Compare().conmpare(
                        k, listen)
                elif best_compare['value'] <= Compare().conmpare(k.decode('utf-8'), listen):
                    best_compare['b_id'], best_compare['value'] = v, Compare().conmpare(
                        k, listen)

        if best_compare != None:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'),
                                         gl.get_value('homepage_url') + 'problem_sol/content?id=' + str(
                                             best_compare['b_id']) + '&categoryId=' + self.categoryId)

        if Compare().conmpare(u'返回首页', listen) > 0.4:
            Speech().speech('好的请稍等')
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'func')


# 习题的内容展示界面
class ContentHandler(tornado.web.RequestHandler):
    def get(self):
        if listener.instance.exist('chat'):
            listener.instance.remove_listener('chat')
        if listener.instance.exist('view'):
            listener.instance.remove_listener('view')
        id = self.get_argument('id')
        categoryId = self.get_argument('categoryId')
        self.render('zhishidian-word.html', id=id, categoryId=categoryId)


# 习题解答界面
class SolutionHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        global page
        page = 'xiti'
        global flag_speech
        flag_speech = True
        operationId = self.get_argument('operationId')
        menuId = self.get_argument('menuId')
        self.render('xiti.html', operationId=operationId,menuId=menuId)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        msg = msg['listen']
        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['ask'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')


# 习题解答的二维码页面
class AnswerHandler(tornado.web.RequestHandler):
    def get(self):
        global flag_speech
        flag_speech = True
        # 生成新的二维码
        g = GenerateCode()

        operationId = self.get_argument('operationId')
        menuId = self.get_argument('menuId')
        url = 'http://' + gl.get_value('api_ip') + '/api/robot/answer/' + str(operationId)
        resp=requests.get(url=url)
        codeUrl='http://h5.robot.nplus5.com/#/exercise/'+operationId
        logging.info(codeUrl)
        g.save_code(codeUrl,'answer')
        self.render('result.html',menuId=menuId)
        # listener.instance.remove_except_chat()
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        msg = msg['listen']
        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')


# 中英互译的处理类
class TranslationHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        menuId=self.get_argument('menuId')
        global page
        page = 'trans'
        global flag_speech
        flag_speech = True
        self.render('zhongyinghuyi.html',menuId=menuId)
        # listener.instance.remove_except_chat()
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        msg = msg['listen']
        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['transfer'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')


# 消息搜索的处理类
class Message_SearchHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        # global page
        # page = 'search'
        global flag_speech
        flag_speech = True
        self.render('tupiansousuo.html')
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        msg = msg['listen']
        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['search'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'func')


# 小贴士的列表界面
class XiaotieshiHandler(tornado.web.RequestHandler):
    def get(self):
        global page
        page = 'xiaotieshi'
        # change
        m = Xiaotieshi_api()
        json = m.main_get()
        # 获得接口中keyname用于关键字监听
        keyword_di = {}
        if json:
            for j in json['data']:
                keyword_di[j['title']] = j['id']
        self.keyword_di = keyword_di
        self.render('xiaotieshi.html', json=json['data'])
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        listen = msg['listen']
        best_compare = None
        for k, v in self.keyword_di.items():
            if Compare().conmpare(k, listen) > 0.5:
                if best_compare == None:
                    best_compare = {}
                    # value中的值是比较的匹配度的值
                    best_compare['b_id'], best_compare['value'] = v, Compare().conmpare(
                        k, listen)
                elif best_compare['value'] <= Compare().conmpare(k.decode('utf-8'), listen):
                    best_compare['b_id'], best_compare['value'] = v, Compare().conmpare(
                        k, listen)

        if best_compare != None:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            # change
            gl.get_value('func').webview(gl.get_value('session'),
                                         gl.get_value('homepage_url') + 'xiaotieshi/content?tipsId=' + str(
                                             best_compare['b_id']))

        if Compare().conmpare(u'返回首页', listen) > 0.4:
            Speech().speech('好的请稍等')
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')


# 小贴士的详情界面
class TieshicontentHandler(tornado.web.RequestHandler):
    def get(self):
        global page
        page = 'xiaotieshicontent'
        # change
        global flag_speech
        flag_speech = True
        if listener.instance.exist('chat'):
            listener.instance.remove_listener('chat')
        if listener.instance.exist('view'):
            listener.instance.remove_listener('view')
        tipsId = self.get_argument('tipsId')
        # change
        self.render('xiaotieshijieshao.html', tipsId=tipsId)


# 小游戏界面
class YuleHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        global page
        page = 'yule'
        global flag_speech
        flag_speech = False
        menuId = self.get_argument('menuId')
        operationId = self.get_argument('operationId')
        ga = Game_api()
        self.gameData=ga.main(operationId)['data']
        if self.gameData!=False:
            if listener.instance.exist('chat'):
                listener.instance.remove_listener('chat')
            self.render('yule.html',menuId=menuId,gameData=self.gameData)
            listener.instance.set_listener("view", self.on_listen)
        else:
            if listener.instance.exist('chat'):
                listener.instance.remove_listener('chat')
            gameData=[{'id':0,'icon':'hehe','activityName':'no game'}]
            self.render('yule.html',menuId=menuId,gameData=gameData)


    def on_listen(self, msg):
        msg = msg['listen']
        li=[
            {'fcode':'paizhao','b_name': 'takephoto-d9c45c/behavior_1'},
            {'fcode':'tiaowu','b_name': 'dance1'},
            {'fcode':'bangqiu','b_name': 'tbangqiu-4fc719/behavior_1'},
            {'fcode':'face','b_name': 'test-115f38/behavior_1'},
            {'fcode':'hand','b_name': 'handshake-aa1938/behavior_1'},
            {'fcode':'smile','b_name': 'main-6e9d8d/emotion'},
            {'fcode':'dance1','b_name': '98kdance-c48261/behavior_1'},
            {'fcode':'dance2','b_name': 'dance2'},
            {'fcode':'jingli','b_name': 'jingli-75c157/behavior_1'},
            ]
        gameDataList=[]
        gd={}
        if self.gameData:
            for g in self.gameData:
                for l in li:
                    if g['fcode']==l['fcode']:
                        gd['name']=g['title']
                        gd['fcode']=g['fcode']
                        gd['b_name']=l['b_name']
                        gameDataList.append(gd)
                        gd={}

        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['yule'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')

        best_compare = None
        for i, l in enumerate(gameDataList):
            if Compare().conmpare(l['name'].decode('utf-8'), msg) > 0.4:
                if best_compare == None:
                    best_compare = {}
                    # value中的值是比较的匹配度的值
                    best_compare['b_name'], best_compare['value'] = l['b_name'], Compare().conmpare(
                        l['name'].decode('utf-8'), msg)
                elif best_compare['value'] <= Compare().conmpare(l['name'].decode('utf-8'), msg):
                    best_compare['b_name'], best_compare['value'] = l['b_name'], Compare().conmpare(
                        l['name'].decode('utf-8'), msg)

        if best_compare != None:
            Speech().speech('好的请稍等')
            flag_speech = False
            gl.get_value('func').start_behavior(gl.get_value('session'), best_compare['b_name'])


# 自定义问答界面
class QAHandler(tornado.web.RequestHandler):
    def get(self):
        self.startTime=time.time()
        self.menuId=self.get_argument('menuId')
        self.operationId=self.get_argument('operationId')
        global page
        page = 'QA'
        global flag_speech
        flag_speech = True
        if listener.instance.exist('chat'):
            listener.instance.remove_listener('chat')
        self.render('QAlist.html',menuId=self.menuId,operationId=self.operationId)
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        msg = msg['listen']
        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['qa'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'pepper/HOMEPAGE')

        q = Question_api()
        temp_li = q.main_get(str(self.operationId))
        best_compare = None
        length = len(temp_li)
        for index, content in enumerate(temp_li):
            if Compare().conmpare(content["question"], msg) > 0.4:
                if best_compare == None:
                    best_compare = {}
                    # value中的值是比较的匹配度的值
                    best_compare['index'], best_compare['value'] = index, Compare().conmpare(
                        content["question"], msg)
                elif best_compare['value'] <= Compare().conmpare(content["question"], msg):
                    best_compare['index'], best_compare['value'] = index, Compare().conmpare(
                        content["question"], msg)

        # 如果列表中type值为0时表示跳转内容界面，当type为1时表示跳转二维码界面
        if best_compare != None:
            # Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            runMsg = {'pageName': variable['qa'], 'startTime': self.startTime, 'endTime': time.time()}
            runMsg = str(runMsg)
            log1.addLog('log.txt', runMsg)
            gl.get_value('func').webview(gl.get_value('session'),
                                         gl.get_value('homepage_url') + 'daogou/content?contentId=' + str(
                                             best_compare['index'])+'&menuId='+self.menuId+'&operationId='+self.operationId)
        else:
            logging.info('没有匹配到相应信息，查询信息为空')

    # 打开json文件，将data对象取出返回data列表
    def openfile(self, file):
        with open(file, 'r') as f:
            temp = json.loads(f.read())
            temp = temp['data']

        return temp


# 自定义问答详情界面
class QAContentHandler(tornado.web.RequestHandler):
    def get(self):
        menuId = self.get_argument('menuId')
        operationId = self.get_argument('operationId')
        global flag_speech
        flag_speech = True
        if listener.instance.exist('chat'):
            listener.instance.remove_listener('chat')
        id = self.get_argument('contentId')
        self.render('QAcontent.html', id=id,menuId=menuId,operationId=operationId)


# 导购问答二维码码界面
class DaogouPicHandler(tornado.web.RequestHandler):
    def get(self):
        global flag_speech
        flag_speech = True
        self.render('daogoupic.html')
        listener.instance.set_listener("view", self.on_listen)

    def on_listen(self, msg):
        msg = msg['listen']
        if Compare().conmpare(u'返回首页', msg) > 0.4:
            Speech().speech('好的请稍等')
            global flag_speech
            flag_speech = False
            gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'func')
