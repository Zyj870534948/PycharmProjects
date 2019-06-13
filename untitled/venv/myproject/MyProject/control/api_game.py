#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import requests,json
import manger.config.globalvar as gl
import manger.config.global_variables
from filter import SQLFilter


# 接口获得
class Game_api(object):
    def __init__(self):
        self.host = str(gl.get_value('api_ip'))
        print(self.host)

    def main(self,operationId):
        self.url = 'http://' + self.host + '/api/funtion/operationgame/' + operationId+'/'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.get(url=self.url, headers=self.headers)
        if resp.status_code == 200:
            return json.loads(resp.content)['data']
        else:
            return False


if __name__ == '__main__':
    ga = Game_api()
    result = ga.main()
    print(result['data'])
    # for d in result['data']:
    #     print(d['functionName'])