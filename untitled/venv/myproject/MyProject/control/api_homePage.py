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
class HomePage_api(object):
    def __init__(self):
        self.host = str(gl.get_value('api_ip'))
        print(self.host)

    def main(self):
        filter = [
            {
                "name": 'status',
                "value": 'ON',
            },
        ]
        filter_str = SQLFilter(filter)
        params = {'filter': filter_str}
        self.url = 'http://' + self.host + '/api/robot/menu/' + gl.get_value('pepper_id')
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.get(url=self.url, headers=self.headers, params=params)
        if resp.status_code == 200:
            return json.loads(resp.content)['data']
        else:
            return False


if __name__ == '__main__':
    hp = HomePage_api()
    result = hp.main()
    print(result['data'])
    # for d in result['data']:
    #     print(d['functionName'])
