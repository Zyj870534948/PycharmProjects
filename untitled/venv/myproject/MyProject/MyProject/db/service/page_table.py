#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/22


from creat_database import *
from creat_database import BaseModel


class Page(BaseModel):
    id = PrimaryKeyField()
    pagename = CharField(null=False, unique=True)
    pageaddress = CharField(null=False)

    class Meta:
        order_by = ('title',)
        db_table = 'page'


if __name__ == '__main__':
    p = Page()
