#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/1

import sys
import os

if not '/home/nao/nplus/MyProject/' in sys.path:
    sys.path.append('/home/nao/nplus/MyProject/')

# if not '/home/nao/nplus/MyProject/manger/config/' in sys.path:
#     sys.path.append('/home/nao/nplus/MyProject/manger/config/')

import threading, face_detect, time,requests
import tornado.ioloop, tornado.web, tornado.options, tornado.httpserver
from tornado.options import define, options
from control.handler_grade import GradeHandler
from control.handler_chat import ChatHandler, CviewHandler
from control.handler_data import DataHandler
from control.handler_all import StandbyHandler, School_introductionHandler \
    , Problem_SolutionHandler, TranslationHandler, Message_SearchHandler, FuncHandler, \
    ContentHandler, SolutionHandler, AnswerHandler, JieshaoHandler, XiaotieshiHandler, \
    TieshicontentHandler,YuleHandler,QAHandler,QAContentHandler,DaogouPicHandler,PSortHandler
from control.handler_water import WaterHandler
from control.handler_download import DownloadHandler
from control.handler_homePage import HomePageHandler
from control.handler_function import FunctionHandler
from control.handler_activity import ActivityHandler
from control.handler_personalCenter import PersonalCenterHandler
from control.handler_activityList import ActivityListHandler
from control.recordFileHandler import RecordFileHandler
import config.globalvar as gl
import config.global_variables
from control.api_openwebview import OpenwebviewHandler
from control.handler_id import IdHandler
from touch import ReactToTouch
from naoqi import *
from control.handler_main import MainHandler
from changeip import Changeip
import qi,logging,time
# from control.log import log1

define("port", default=8888, help="run port", type=int)

TEMPLATE_PATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)), "template")
STATIC_PATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)), "static")


class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/standby", StandbyHandler),  # 待机界面
            (r"/func", FuncHandler),  # 功能界面
            (r"/grade", GradeHandler),  # 分数展示界面
            (r"/data", DataHandler),  # 数据接收的handler
            (r"/chat", ChatHandler),  # 闲聊界面
            (r"/chat/view", CviewHandler),  # 闲聊的展示界面
            (r"/jieshao", JieshaoHandler),  # 学校介绍界面
            (r"/jieshao/content", School_introductionHandler),  # 学校介绍界面的详细内容
            (r"/problem_sol", Problem_SolutionHandler),  # 习题知识点和解答的主界面
            (r"/sort",PSortHandler),#知识点的分类界面
            (r"/problem_sol/content", ContentHandler),  # 习题知识点展示界面
            (r"/problem_sol/solution", SolutionHandler),  # 习题解答界面
            (r"/problem_sol/answer", AnswerHandler),  # 习题回答界面
            (r"/translation", TranslationHandler),  # 翻译界面
            (r"/message_search", Message_SearchHandler),  # 信息搜索
            (r'/openwebview', OpenwebviewHandler),  # 用于开启页面方法
            (r"/xiaotieshi", XiaotieshiHandler),  # 小贴士的列表界面
            (r"/xiaotieshi/content", TieshicontentHandler),  # 小贴士的详情界面
            (r"/daogou",QAHandler),#卡朋电动车的列表页面
            (r"/daogou/content",QAContentHandler),#卡朋电动车列表的详情界面
            (r"/daogou/pic", DaogouPicHandler),  # 卡朋电动车买单二维码界面
            (r"/water",WaterHandler), #智能饮水机界面
            (r"/id", IdHandler),
            (r"/yule",YuleHandler),
            (r"/", MainHandler),
            (r"/download",DownloadHandler), #下载界面
            (r"/pepper/HOMEPAGE",HomePageHandler), #六大类界面
            (r"/pepper/FUNCTION",FunctionHandler), #业务也就是功能界面，六大类下的功能界面
            (r"/pepper/INTRODUCE", JieshaoHandler), #信息介绍界面
            (r"/pepper/SEARCH", Message_SearchHandler), #信息搜索界面
            (r"/pepper/QA", QAHandler), #自定义问答界面
            (r"/pepper/ACTIVITYCONTENT", ActivityHandler), #活动界面
            (r"/pepper/ACTIVITY", ActivityListHandler), #活动列表界面
            (r"/pepper/TRANSLATE", TranslationHandler), #中英互译界面
            (r"/pepper/ASK", SolutionHandler), #习题解答界面
            (r"/pepper/PERSONALCENTER", PersonalCenterHandler), #个人中心界面
            (r"/pepper/GAME", YuleHandler), #小游戏界面
            (r"/recordfile", RecordFileHandler), #小游戏界面

        ]

        settings = dict(
            template_path=TEMPLATE_PATH,
            static_path=STATIC_PATH,
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    #获取当前日期写入日志文件
    day=time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
    # log1.addLog('log.txt', '------------------------------------------'+str(day)+'--------------------------------------')        #！！！
    #修改js中aulluse.js的ip
    c = Changeip()
    c.changeIp('../static/js/alluse.js',gl.get_value('ip'))
    #tornado固定
    tornado.options.parse_command_line()
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(options.port)  # 监听端口
    #平板打开机器人待机界面
    gl.get_value('func').webview(gl.get_value('session'), gl.get_value('homepage_url') + 'standby')
    tornado.ioloop.IOLoop.instance().start()


# broker = ALBroker("pythonBroker", gl.get_value('ip'), 8889, gl.get_value('robot_ip'), 9559)
# try:
#     pythonModule = face_detect.myModule("pythonModule")
# except Exception as e:
#     print("error" + str(e))
#     exit(1)
#
#
# def start():
#     global flag
#     flag = True
#     proxy = ALProxy("ALMemory")
#     proxy.subscribeToEvent("FaceDetected", "pythonModule", "pythondatachanged")
#     while flag:
#         time.sleep(2)

def touch():
    app = qi.Application(["ReactToTouch", "--qi-url=" + str(gl.get_value('connection_url'))])
    # app = qi.Application(["ReactToTouch", "--qi-url=tcp://192.168.8.115:9559"])
    react_to_touch = ReactToTouch(app)
    app.run()


if __name__ == "__main__":
    threads = []
    t1 = threading.Thread(target=main)
    threads.append(t1)
    # t2 = threading.Thread(target=start)
    # threads.append(t2)
    t2=threading.Thread(target=touch)
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
