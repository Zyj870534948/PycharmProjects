#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/29
# !/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/23

import requests, json
import sys
sys.path.append('../')
from filter import SQLFilter
import manger.config.globalvar as gl
import manger.config.global_variables
import logging

# 接口获得
class Problem_api(object):
    def __init__(self):
        self.host = str(gl.get_value('api_ip'))

    def problem_api_get(self,id):
        filter = [
            {
                "name": 'categoryId',
                "value": id,
            },
        ]
        filter_str = SQLFilter(filter)
        params = {'filter': filter_str}
        self.url = 'http://' + self.host + '/api/robot/' + gl.get_value('pepper_id') + '/rolematerial/CLASSROOM'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.get(url=self.url,headers=self.headers,params=params)
        if resp.status_code == 200:
            return json.loads(resp.content)['data']
        else:
            result={'data':[]}
            return result


if __name__ == '__main__':
    m = Problem_api()
    print m.problem_api_get(21)
