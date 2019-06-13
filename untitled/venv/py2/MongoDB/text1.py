#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/python3

import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# mylist = [
#     {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
#     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
#     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
#     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
#     {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
# ]
#
# x = mycol.insert_many(mylist)
#
# # 输出插入的所有文档对应的 _id 值
# print(x.inserted_ids)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1,"url": 1}):
#     print(x)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
#
# myquery = {"name": "Taobao"}
#
# mycol.delete_one(myquery)

# 删除后输出
for x in mycol.find():
    print(x)