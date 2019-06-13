#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from contextlib import closing
import os

def download_file(url, path):
    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print '下载开始'
        with open(path, "wb") as f:
            n = 1
            for chunk in r.iter_content(chunk_size=chunk_size):
                loaded = n*1024.0/content_size
                f.write(chunk)
                print '已下载{0:%}'.format(loaded)
                n += 1

if __name__ == '__main__':
    url = 'https://vip2.pp63.org/e928c44b-b500-4ad6-96a3-61764991b126'
    path = './001.mp4'
    download_file(url, path)