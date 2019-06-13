#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"
# 接口
import requests,json
import manger.config.globalvar as gl
import manger.config.global_variables

class PersonalCenter_api(object):
    def __init__(self):
        self.host = str(gl.get_value('api_ip'))

    def main(self):
        self.url='http://' + self.host +'/api/robotintroduce/'+gl.get_value('pepper_id')
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.get(url=self.url,headers=self.headers)
        if resp.status_code == 200:
            return json.loads(resp.content)['data']
        else:
            return False


if __name__ == '__main__':
    pc = PersonalCenter_api()
    print(pc.main())