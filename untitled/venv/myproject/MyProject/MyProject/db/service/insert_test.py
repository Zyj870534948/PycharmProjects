#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/3

import sys

reload(sys)
sys.setdefaultencoding('utf8')

# from creat_table_test import *
from creat_table_test import Course


class Course_opreate:
    # 新增数据
    def course_insert(self, id, title, period, description):
        Course.create_table()
        Course.create(id=id, title=title, period=period, description=description)

    # 删除数据
    def course_delect(self, id):
        # 获取1行数据，再删除,如果不存在，则会报错
        record = Course.get(Course.id == id)
        record.delete_instance()
        print('删除成功')

    # 修改数据
    def course_update(self, id, title, period, description):
        record = Course.get(Course.id == id)
        record.title = title
        record.period = period
        record.description = description
        record.save()

    # 查询数据:查询所有
    def course_select_all(self):
        record = Course.select()
        self.display(record)

    # 查询数据：根据id查询
    def course_select_id(self, id):
        record = Course.get(Course.id == id)
        print("id:{}课程:{},学时:{},文科必修:{}".format(record.id, record.title, record.period, record.description))

    # 查询数据：根据title查询
    def course_select_title(self, title):
        record = Course.select().where(Course.title == title)
        self.display(record)

    def display(self,record):
        for s in record:
            print("id:{}课程:{},学时:{},文科必修:{}".format(s.id, s.title, s.period, s.description))

if __name__ == '__main__':
    co=Course_opreate()
    co.course_insert('10','语文','12','必修')


