#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/31
import sys
sys.path.append("..")
import requests, json
import globalvar as gl
import global_variables


# 接口获得
class Standby_api(object):
    def __init__(self):
        self.host = str(gl.get_value('api_ip'))

    def standby_get(self):
        self.url = 'http://' + self.host + '/api/robot/' + gl.get_value('pepper_id') + '/detail/'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.get(url=self.url, headers=self.headers)
        if resp.status_code == 200:
            return json.loads(resp.content)['data']
        else:
            return []


if __name__ == '__main__':
    result = Standby_api().standby_get()
    print(result)
