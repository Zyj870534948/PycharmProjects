#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"
import requests
from requests import get
from requests import post
url = 'http://192.168.3.5:8123/api/services/camera/snapshot'  # http://localhost:8123/api/services/switch/turn_on
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmNmJkNmEyOWM4ZjY0ZjI1OWY4ZDBlOWI4YWU2MTNiZSIsImlhdCI6MTU0ODIyMzg2MiwiZXhwIjoxODYzNTgzODYyfQ.-q8mDUy48ifCGaxXU7uo6xXy-4O1pQTpurRNgJ3aPJk',
    'content-type': 'application/json',
}
# data = '{"entity_id": "remote.xiaomi_rm","command":"' + air_tmp["close"] + '"}'
data = '{"entity_id":"camera.cam1","filename":"C:/pyfun/file/picture/test.jpg"}'
response = post(url, data=data, headers=headers)