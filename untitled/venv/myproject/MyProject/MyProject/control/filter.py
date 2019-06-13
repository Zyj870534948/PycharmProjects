#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"sidalin"

import json

import requests
import logging


class initFilter:
    def __init__(self):
        self.orderList = []
        self.sesl = []

    def addOrder(self, order):
        self.orderList.append(order)

    def addSQLExpressionSet(self, ses):
        self.sesl.append(ses)

    def buildBySe(self, se=[], lop='and', order=[]):
        se_new = []
        if isinstance(order, (int, str, float)):
            self.orderList.extend(order)
        else:
            self.orderList.append(order)

        if isinstance(se, (int, str, float)):
            se_new.append(se)
        else:
            se_new = se
        ses = SQLExpressionSet(lop, se_new)
        self.sesl.append(ses)

    def getFilter(self):
        return {"orderList": self.orderList, "sesl": self.sesl}


class SQLExpressionSet:
    def __init__(self, lop, selist):
        self.logicalOp = lop
        self.sel = selist

    def display(self):
        return {
            'logicalOp': self.logicalOp,
            'sel': self.sel
        }


class SQLOrder:
    def __init__(self, name, oType):
        self.property = name
        self.direction = oType

    def display(self):
        return {
            'property': self.property,
            'direction': self.direction
        }


class SQLException:
    def __init__(self, lop, name, mathM, exp, ignoreC=False):
        # 表达式逻辑关系符， and ， or ，not
        # 连接该表达式时的逻辑关系符号
        self.logicalOp = lop
        # 属性名String类型
        self.property = name
        # 匹配方式String类型
        self.matchMode = mathM
        # 匹配的值Object[]对象数组对于matchMode为between和in需要多个值
        exp_new = []
        if isinstance(exp, (int, str, float)):
            exp_new.append(exp)
        else:
            exp_new = exp
        self.value = exp_new
        self.ignoreCase = ignoreC

    def display(self):
        return {
            'logicalOp': self.logicalOp,
            'property': self.property,
            'matchMode': self.matchMode,
            'value': self.value,
            'ignoreCase': self.ignoreCase
        }


#   arr参数
#       Object[] 对象数组
#       数组中是对象，对象包含两个属性name，value
#       name参数名称，value参数的值，mathM匹配的值
#       mathM常用有3个值：'='全匹配（默认），'like'模糊匹配，'between'范围直接（value是数组[1,10]）
#  例:[{name:'username',value:'admin',mathM:'like'},{name:'password',value:'123456'}]

def SQLFilter(arr):
    if isinstance(arr, list) == False:
        return False
    filter = initFilter()
    sel = []
    for a in arr:
        if a['value']:
            mathM = '='
            val = a['value']
            if a.has_key('mathM'):
                mathM = a['mathM']
            if mathM == 'like':
                val = '%25' + val + '%25'
            se = SQLException('and', a['name'], mathM, val, True)
            se = se.display()
            sel.append(se)
            ses = SQLExpressionSet('and', sel)
            ses = ses.display()
            filter.addSQLExpressionSet(ses)
    f = filter.getFilter()
    return json.dumps(f)


#   arr参数
#        Object[] 对象数组
#        数组中是对象，对象包含两个属性name，value
#        name参数名称，value参数的值
#        value的值有desc(降序)、asc(升序)
#   例:[{name:'id',value:'desc'}]
def SQLOrder(arr):
    if isinstance(arr, list) == False:
        return False
    sort = []

    for a in arr:
        if a['value'] != '':
            obj = {"property": a['name'], "direction": a['value']}
            sort.append(obj)
    return json.dumps(sort)


if __name__ == '__main__':
    sort = [
        {
            'name': 'createTime',
            'value': 'desc'
        }
    ]
    # # params={'filter':'{"sesl":[{"logicalOp":"and","sel":[{"logicalOp":"and","property":"status","matchMode":"=","value":["OFF"],"ignoreCase":true}]}]}'}
    # filter_str = SQLOrder(sort)
    # print(filter_str)
    filter = [
        {
            "name": 'status',
            "value": 'ON',
        },
    ]

    filter_str = SQLFilter(filter)
    print(filter_str)
    filter = [
        {
            "name": 'categoryId',
            "value": 21,
        },
    ]
    filter_str = SQLFilter(filter)
    print(filter_str)
