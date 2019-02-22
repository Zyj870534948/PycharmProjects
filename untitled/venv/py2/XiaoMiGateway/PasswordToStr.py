#!/usr/bin/env python
# -*- coding:utf-8 -*-

from binascii import b2a_hex, a2b_hex
import sys

s='8B941730EEC04B09'    #初始向量
m=a2b_hex(s)
print m,repr(m)

#转换后的初始向量
#b'\x17\x99m\t=(\xdd\xb3\xbaiZ.oXV.'