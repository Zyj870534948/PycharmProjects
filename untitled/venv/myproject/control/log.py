#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"
class Log:
    def addLog(self,fileName,content):
        with open(fileName, 'a+') as file:
            # 最后根据json的dump将上面的列表写入文件，得到最终的json文件
            file.write(content+'\n')


log1=Log()

if __name__ == '__main__':
    l=Log()
    l.addLog('log.txt','{"pageNmae": "standby", "startTime": "1552535297.36"}')