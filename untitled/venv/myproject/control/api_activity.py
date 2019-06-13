#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"


import requests, json
import manger.config.globalvar as gl
import manger.config.global_variables


# 接口获得介绍中的内容
class Activity_api(object):
    def __init__(self):
        self.host = str(gl.get_value('api_ip'))

    def main(self,activityId):
        self.url='http://' + self.host +'/api/activity/'+activityId
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.get(url=self.url,headers=self.headers)
        if resp.status_code == 200:
            return json.loads(resp.content)['data']
        else:
            return False


if __name__ == '__main__':
    a = Activity_api()
    print(a.main())