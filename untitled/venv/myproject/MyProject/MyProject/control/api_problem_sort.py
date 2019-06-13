#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"sidalin"

# 分类接口，获得分类数据，如机器人中物理，化学，科学
import requests, json
import sys
#
sys.path.append('../')
reload(sys)
sys.setdefaultencoding("utf-8")
import manger.config.globalvar as gl
import manger.config.global_variables


# 接口获得
class ProblemSort_api(object):
    def __init__(self):
        self.host = str(gl.get_value('api_ip'))

    def main_get(self):
        self.url = 'http://' + self.host + '/api/robot/CLASSROOM/category/'+gl.get_value('pepper_id')
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        resp = requests.get(url=self.url, headers=self.headers)
        if json.loads(resp.content).has_key('success'):
            return json.loads(resp.content)['data']
        else:
            print(str(json.loads(resp.content)['errorMsg']))
            data = [{
                "id": 18,
                "fcode": "CLASSROOM",
                "categoryName": "获取不到信息",
                "status": "ON",
            }]
            return data


if __name__ == '__main__':
    p = ProblemSort_api()
    print(p.main_get())
