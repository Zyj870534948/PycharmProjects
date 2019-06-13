#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import tornado.web
import json
from logtiming import log1

# 用于记录页面时间的长短
class RecordFileHandler(tornado.web.RequestHandler):
    def get(self):
        result={}
        recordInfo=self.get_argument('data')
        recordInfo=json.loads(recordInfo)
        #将接受到的消息{u'pageName': u'FUNCTION', u'endTime': 1552630485161L, u'startTime': 1552630121287L}
        #转成{'pageName': 'FUNCTION', 'endTime': 1552630485161L, 'startTime': 1552630121287L}，方便后台处理
        for key in recordInfo:
            if key==u'pageName':
                result[key.encode('utf-8')]=recordInfo[key].encode('utf-8')
            else:
                result[key.encode('utf-8')] = recordInfo[key]
        result = str(result)
        log1.addLog('log.txt', result)
        print(recordInfo)
        self.write('success')