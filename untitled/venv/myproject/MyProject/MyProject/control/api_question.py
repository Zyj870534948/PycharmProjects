#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"sidalin"

import requests, json
import sys
sys.path.append('../')
import manger.config.globalvar as gl
import manger.config.global_variables
from filter import SQLFilter


# 接口获得
class Question_api(object):
    def __init__(self):
        self.host = str(gl.get_value('api_ip'))

    def main_get(self,operationId):
        filter = [
            {
                "name": 'status',
                "value": 'ON',
            },
        ]
        filter_str = SQLFilter(filter)
        params = {'filter': filter_str}
        # self.url = 'http://' + self.host + '/api/robot/customMaterial/' + gl.get_value('pepper_id')
        self.url = 'http://' + self.host + '/api/funtion/operationCustomMaterial/' + operationId+'/'
        print(self.url)
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.get(url=self.url, headers=self.headers,params=params)
        if resp.status_code == 200:
            return json.loads(resp.content)['data']['data']
        else:
            result = [{
                'sort': None,
                'status': 'ON',
                'question': '今天天气怎么样？',
                'answer': '非常好',
                'id': 9
            }]
            return result


if __name__ == '__main__':
    q = Question_api()
    result = q.main_get()
    print(result)
