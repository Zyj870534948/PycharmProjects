#!/usr/bin/env python
#-*- coding:utf-8 -*-

#_author:"xiaolin"
#date:2018/8/24
from school_intro_table import School_intro

class School_intro_opreate:
    # 新增数据
    def sch_insert(self, id, title,content):
        School_intro.create_table()
        School_intro.create(id=id, title=title,content=content)

    # 查询数据：根据title查询id
    def sch_select_pagename(self, title):
        record = School_intro.get(School_intro.title == title)
        return record.id

    # 查询数据：根据id查询,返回字符串
    def sch_select_id(self, id):
        record = School_intro.get(School_intro.id == id)
        s={'id':record.id,'title':record.title,'content':record.content}
        return s

    # 修改数据
    def sch_update(self, id,title,content ):
        record = School_intro.get(School_intro.id == id)
        record.id = id
        record.title = title
        record.content = content
        record.save()

    def display(self,record):
        for s in record:
            print("id:{}title:{},content:{}".format(s.id, s.pagename, s.pageaddress))


if __name__ == '__main__':
    s=School_intro_opreate()
    # s.sch_insert('1','introduce','是个好学校')
    print s.sch_select_id(s.sch_select_pagename('introduce'))
    # print s.sch_select_pagename('introduce')
    # print p.page_select_id('1')['pageaddress']