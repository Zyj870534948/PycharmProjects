#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''
import json
import requests

def Tuling(text_input):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    req = {
        "perception":
            {
                "inputText":
                    {
                        "text": text_input
                    },
                "selfInfo":
                    {
                        "location":
                            {
                                "city": "无锡"
                            }
                    }
            },
        "userInfo":
            {
                "apiKey": "66f396239d6948f5b267f1ec5c234731",
                "userId": "demo"
            }
    }
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    response = requests.post(api_url, data=req, headers={'content-type': 'application/json'})
    data = (response.text).encode("utf-8")
    data = json.loads(data)
    return data["results"][0]["values"]["text"]


if __name__=='__main__':
    print (Tuling(""))
