#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import requests
import json

re = requests.get("http://sandbox.api.simsimi.com/request.p?key=c4c118f2-a89b-4cfe-9563-359c39046bb2&lc=en&ft=1.0&text=")
tb = json.loads(re.text.encode("utf-8"))
print type(tb),tb["response"]