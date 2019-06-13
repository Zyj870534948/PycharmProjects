#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"

import sys
import time
import numpy
import os
import json

try:
    f_element = open('./element.txt')
except:
    f_element = open('./element.txt','w')
    f_element.close()
    f_element = open('./element.txt')


element = f_element.read()[:-1]
element = '{' +  element + '}'

element = json.loads(element)


print type(element),element