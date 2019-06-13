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
        # strnow1 = str(strnow)
        # fileDi = {}
        with open(fileName, 'r') as f:
            fileContent = json.load(f)
            fileDi=fileContent
        fileDi["time"]=strnow
        # print fileDi["time"]
        with open(fileName, 'w+') as file:
            # 最后根据json的dump将上面的列表写入文件，得到最终的json文件
            json.dump(fileDi, file, ensure_ascii=False)

    def addLog(self,fileName,content):

        fileDi={}
        with open(fileName, 'r') as f:
            fileContent = json.load(f)
            fileDi=fileContent

        print(fileDi['page'])
        print(type(fileDi))

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
    mes = {'pageName': 'MENU', 'endTime': 1553564847.058205, 'startTime': 1553564844.275291}
    print type(mes)
    a = {"page": [{"pageName": "STANDBY", "endTime": 1553564844.175825, "startTime": 1553564832.222233}],
     "time": "2019-03-26 01:47"}
    runMsg = {'pageName': 'MENU', 'endTime': 1553564847.058205, 'startTime': 1553564844.275291}
    {'pageName': 'MENU', 'endTime': 1553564847.058205, 'startTime': 1553564844.275291}
    {'pageName': 'MENU', 'endTime': 1553564848648L, 'startTime': 1553564848504L}
    {'pageName': 'FUNCTION', 'endTime': 1553564850551L, 'startTime': 1553564849292L}
    {'pageName': 'MENU', 'endTime': 1553564851994L, 'startTime': 1553564850970L}
    {'pageName': 'FUNCTION', 'endTime': 1553564853372L, 'startTime': 1553564852594L}
    {'pageName': 'FUNCTION', 'endTime': 1553564853689L, 'startTime': 1553564852594L}
    {'pageName': 'MENU', 'endTime': 1553564855081L, 'startTime': 1553564854182L}
    {'pageName': 'FUNCTION', 'endTime': 1553564856247L, 'startTime': 1553564855435L}

    l.addLog('log.txt', mes)
    l.changeTime('./log.txt')
    # l.addLog('log.txt',{'page':'bbb','end':'aaa'})
    # l.addLog('log.txt', {'page': 'bbb', 'end': '111'})
    l.addLog('log.txt', mes)