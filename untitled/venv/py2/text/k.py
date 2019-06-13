from requests import get
from requests import post
import time
import json
import numpy as np
from PIL import Image


# import matplotlib.pyplot as plt

''''''

air_tmp = {"close":"Z6VJACYCAACXBgAAUxEAAKwiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjEAAAAAAAEAAAAAAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "22coldld": "Z6VJACgCAACKBgAAUREAALAiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjEAAAEBAQAAAAEBAAAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "23coldld": "Z6VJACgCAACJBgAAUREAALAiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjEAAAEBAQAAAQEBAAAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "24coldld": "Z6VJACcCAACPBgAAUBEAAK8iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjEAAAEBAQAAAAAAAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "25coldld": "Z6VJACYCAACTBgAANhEAAMoiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjEAAAEBAQAAAQAAAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "26coldld": "Z6VJACcCAACPBgAAUhEAAK0iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjEAAAEBAQAAAAEAAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "27coldld": "Z6VJACYCAACSBgAAUREAAK0iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjEAAAEBAQAAAQEAAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "28coldld": "Z6VJACcCAACQBgAAUREAAK4iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjEAAAEBAQAAAAABAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "22hotld": "Z6VJACcCAACSBgAAUhEAAK4iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjAAAQEBAQAAAAEBAAAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "23hotld": "Z6VJACcCAACSBgAAUREAAK8iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjAAAQEBAQAAAAABAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "24hotld": "Z6VJACcCAACSBgAAUBEAAK8iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjAAAQEBAQAAAAAAAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "25hotld": "Z6VJACcCAACRBgAAUREAAK4iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjAAAQEBAQAAAQAAAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "26hotld": "Z6VJACcCAACSBgAAUREAAK8iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjAAAQEBAQAAAAEAAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "27hotld": "Z6VJACYCAACSBgAAUREAAK4iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjAAAQEBAQAAAQEAAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           "28hotld": "Z6VJACcCAACSBgAAUREAAK8iAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjAAAQEBAQAAAAABAQAAAAAAAAAAAAAAAAAAAAABAAEAAAEAAA",
           }


'''
url = 'http://192.168.3.5:8123/api/states/sensor.temperature_158d0002e26e39'
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmNmJkNmEyOWM4ZjY0ZjI1OWY4ZDBlOWI4YWU2MTNiZSIsImlhdCI6MTU0ODIyMzg2MiwiZXhwIjoxODYzNTgzODYyfQ.-q8mDUy48ifCGaxXU7uo6xXy-4O1pQTpurRNgJ3aPJk',
    'content-type': 'application/json',
}

response = get(url, headers=headers)
data = str = unicode.encode(response.text)
# print data
data = json.loads(data)

print data["state"]
time.sleep(1)
'''


'''
url = 'http://192.168.3.5:8123/api/services/media_player/play_media'      #http://localhost:8123/api/services/switch/turn_on
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmNmJkNmEyOWM4ZjY0ZjI1OWY4ZDBlOWI4YWU2MTNiZSIsImlhdCI6MTU0ODIyMzg2MiwiZXhwIjoxODYzNTgzODYyfQ.-q8mDUy48ifCGaxXU7uo6xXy-4O1pQTpurRNgJ3aPJk',
    'content-type': 'application/json',
}
# data = '{"entity_id": "remote.xiaomi_rm","command":"' + air_tmp["close"] + '"}'
# data = '{"entity_id": "image_processing.ms_face_feature"}'
data = '{"entity_id": "media_player.vlc","media_content_id":"C:/Users/N-pod/Desktop/music.mp3","media_content_type":"music"}'
response = post(url,data=data, headers=headers)
print(response.text)
'''
# url = 'http://192.168.3.5:8123/api/states/image_processing.ms_face_feature'
# headers = {
#     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmNmJkNmEyOWM4ZjY0ZjI1OWY4ZDBlOWI4YWU2MTNiZSIsImlhdCI6MTU0ODIyMzg2MiwiZXhwIjoxODYzNTgzODYyfQ.-q8mDUy48ifCGaxXU7uo6xXy-4O1pQTpurRNgJ3aPJk',
#     'content-type': 'application/json',
# }
# response = get(url, headers=headers)
# data = unicode.encode(response.text)
# data = json.loads(data)
# data1 = unicode.encode(data["state"])
# print type(data1),data["attributes"]["faces"]

# if int(data["state"]) >= 1:
#     data1 = (data["attributes"])
#     print data1["faces"][0]["gender"], data1["faces"][0]["age"], data1["faces"][0]["glasses"]
#     print type(data1["faces"][0]["gender"]),data1["faces"][0]
#     # print type(data),data

# url = "https://realme-holi.oss-ap-south-1.aliyuncs.com/holi/1/1552706779743.jpeg"
# request = get(url)
# f = open("./123.jpg",'wb')
# for chunk in request.iter_content(chunk_size=1024):
#     if chunk:
#         f.write(chunk)
#
# img = Image.open('./123.jpg')
# img = img.resize((900, 500),Image.ANTIALIAS)
# plt.imshow(img)
# print request.text


# f = open('D:/video3/003.ts', "wb")
# for chunk in request.iter_content(chunk_size=1024):
#     if chunk:
#         f.write(chunk)

# if request.text[0]=="<" and request.text[1] == "h":
#     print(request.text)
# else:
#     print("OK")
'''
headers = {
    'Accept': 'application/json',
    'content-type': 'application/json',
}

response = get(url="http://api.robot.nplus5.com/api//third/book/user/101/personal/male",headers=headers)
#http://api.robot.nplus5.com/api/third/recommend/user/101/personal/male
#http://api.robot.nplus5.com/api//third/book/user/101/personal/male
# print type(response.text),response.text

content = json.loads(response.text)
print content#["data"]["title"],content["data"]["textContent"]
# print type(content["data"][0]["returnBooksTime"]),type(content["data"][0]["bookName"]),content["data"][0]["bookName"]#,(content["data"][0]["flag"]),type(content["data"][0]["isRenew"])

# if content["data"][0]["bookName"] == None:
#     print "OK"

# print s["data"]["textContent"]
s = {u'errorMsg': u'\u670d\u52a1\u9519\u8bef\uff1anull', u'errorNum': -65535, u'errorArgs': [], u'detail': None}
print s["errorMsg"]
'''

# response = post(url="http://192.168.8.103:11697/welcome")


from requests import post
url = 'http://192.168.8.141:8123/api/services/light/turn_off'      #http://localhost:8123/api/services/switch/turn_on
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmNmJkNmEyOWM4ZjY0ZjI1OWY4ZDBlOWI4YWU2MTNiZSIsImlhdCI6MTU0ODIyMzg2MiwiZXhwIjoxODYzNTgzODYyfQ.-q8mDUy48ifCGaxXU7uo6xXy-4O1pQTpurRNgJ3aPJk',
    'content-type': 'application/json',
}
data = '{"entity_id": "light.xiaomi_philips_smart_led_ball"}'
response = post(url,data=data, headers=headers)