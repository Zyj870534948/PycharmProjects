#!/usr/bin/env python
#-*- coding:utf-8 -*-

#_author:"xiaolin"
#date:2018/8/22

from page_table import Page

#存放待机页面的信息和主页面的信息
#格式:id,pagename,pageaddreww(1,'standby', 'http://10.1.1.106:8888/xxxxx')
class Page_opreate:
    # 新增数据
    def page_insert(self, id, pagename, pageaddress):
        Page.create_table()
        Page.create(id=id, pagename=pagename, pageaddress=pageaddress)

    # 查询数据：根据title查询id
    def page_select_pagename(self, pagename):
        record = Page.get(Page.pagename == pagename)
        return record.id

    # 查询数据：根据id查询,返回字符串
    def page_select_id(self, id):
        record = Page.get(Page.id == id)
        s={'id':record.id,'pagename':record.pagename,'pageaddress':record.pageaddress}
        return s

    # 修改数据
    def page_update(self, id,pagename,pageaddress ):
        record = Page.get(Page.id == id)
        record.id = id
        record.pagename = pagename
        record.pageaddress = pageaddress
        record.save()

    def display(self,record):
        for s in record:
            print("id:{}名称:{},地址:{}".format(s.id, s.pagename, s.pageaddress))

if __name__ == '__main__':
    p=Page_opreate()
    # p.page_insert('2','standby2','standby_hor.html')
    print p.page_select_pagename('standby')
    # print p.page_select_id('1')['pageaddress']