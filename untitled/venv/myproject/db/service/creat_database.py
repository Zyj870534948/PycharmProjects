#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/3

# 外部导入python库
import sys
import os

sys.path.append(r'/MyProject/mylib')
# from test_api import test1

from peewee import *

db = SqliteDatabase('../control/test1.db')
# db = SqliteDatabase(r'/MyProject1/db/control/test2.db')


class BaseModel(Model):
    class Meta:
        database = db
