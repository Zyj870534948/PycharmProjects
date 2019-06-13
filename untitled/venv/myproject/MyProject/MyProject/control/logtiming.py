#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"
import datetime
import json
from datetime import date, time, datetime, timedelta

class Log:
    def changeTime(self,fileName):

        now = datetime.now()
        strnow = now.strftime('%Y-%m-%d %H:%M')
        # 开机时间
        strnow1 = str(strnow)
        fileDi = {}
        with open(fileName, 'r') as f:
            fileContent = json.load(f)
            fileDi=fileContent
        fileDi["time"]=strnow1
        print fileDi["time"]
        with open(fileName, 'w+') as file:
            # 最后根据json的dump将上面的列表写入文件，得到最终的json文件
            json.dump(fileDi, file, ensure_ascii=False)

    def addLog(self,fileName,content):

        fileDi={}
        with open(fileName, 'r') as f:
            fileContent = json.load(f)
            fileDi=fileContent

        # print(fileDi["time"])
        # print(type(fileDi))

        if fileDi.has_key('page'):
            fileDi['page'].append(content)
        else:
            pass

        with open(fileName, 'w') as file:
            # 最后根据json的dump将上面的列表写入文件，得到最终的json文件
            json.dump(fileDi, file, ensure_ascii=False)

log1=Log()

if __name__ == '__main__':
    l=Log()
    l.changeTime('a.json')
    l.addLog('a.json',{'page':'bbb','end':'aaa'})
