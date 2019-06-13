#!/usr/bin/env python
# -*- coding:utf-8 -*-


# _author:"xiaolin"
# date:2018/9/10

import requests, json
import sys
sys.path.append('../')
import manger.config.globalvar as gl
import manger.config.global_variables
from filter import SQLFilter


# 接口获得
class Func_api(object):
    def __init__(self):
        self.host = str(gl.get_value('api_ip'))
        print(self.host)

    def main_get(self):
        filter = [
            {
                "name": 'status',
                "value": 'ON',
            },
        ]
        filter_str = SQLFilter(filter)
        params = {'filter': filter_str}
        self.url = 'http://' + self.host + '/api/robot/' + gl.get_value('pepper_id') + '/function/'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.get(url=self.url, headers=self.headers,params=params)
        if resp.status_code == 200:
            return json.loads(resp.content)['data']
        else:
            return False


if __name__ == '__main__':
    f = Func_api()
    result = f.main_get()
    print(result['data'])
    # for d in result['data']:
    #     print(d['functionName'])
