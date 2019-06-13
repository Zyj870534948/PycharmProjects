#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/9/4

import httplib
import md5
import urllib
import random
import json


class Transfer:
    def __init__(self):
        self.appid = '20180903000202134'  # 你的appid
        self.secretKey = 'p6jPvVqWUinlaDAMX1Vf'  # 你的密钥
        self.httpClient = None
        self.myurl = '/api/trans/vip/translate'
        self.fromLang = 'auto'
        self.toLang = 'auto'
        self.salt = random.randint(32768, 65536)

    def transfer(self, q):
        sign = self.appid + q + str(self.salt) + self.secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = self.myurl + '?appid=' + self.appid + '&q=' + urllib.quote(
            q) + '&from=' + self.fromLang + '&to=' + self.toLang + '&salt=' + str(
            self.salt) + '&sign=' + sign
        try:
            httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            resp = json.loads(response.read())

            if resp.has_key('error_code'):
                return resp[u'error_msg']
            else:
                return resp['trans_result'][0]
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()


if __name__ == '__main__':
    t = Transfer()
    result = t.transfer('你好')
    if isinstance(result, dict):
        print result['src']+' '+result['dst']
    else:
        print result
