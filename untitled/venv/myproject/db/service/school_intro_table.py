#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/24
from creat_database import *


class School_intro(BaseModel):
    id = PrimaryKeyField()
    title = CharField(null=False)
    content = CharField(null=False)

    class Meta:
        order_by = ('title',)
        db_table = 'school_intro'
