#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import requests
import json
class UpFile:
    def upfile(self,url,filePath):
        url = 'http://192.168.1.151:8080/api/record'
        headers = {'Accept': 'application/json'}
        filePath = r'/data/home/nao/nplus/MyProject/manger/log.txt'
        with open('log.txt', 'r') as f:
            f = f.read()
            f = json.loads(f)
            # d = json.dumps(f.read())
        body = {'data': f}
        resp = requests.post(url=url, params=body, headers=headers)
uf=UpFile()

if __name__ == '__main__':
    uf=UpFile()
    uf.upfile('http://yapi.nplusgroup.net/project/249/interface/api/32712/','log.txt')
    # url = "http://192.168.1.151:8080/api/photo/record"
    # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # headers = {'Accept': 'application/json'}

