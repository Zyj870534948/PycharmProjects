#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/9/11

# 用于判断相似度

import difflib


class Compare:
    def conmpare(self, str1, str2):
        seq = difflib.SequenceMatcher(None, str1, str2)
        ratio = seq.ratio()
        return ratio


if __name__ == '__main__':
    print Compare().conmpare(u'返回首页', u'返回')
