#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import tornado.web
import urllib
import os,time,requests
from unzfile import ZFile

class DownloadHandler(tornado.web.RequestHandler):
    def get(self):
        state=self.get_argument('state')
        if state=='on':
            url = 'https://pepper-test.oss-cn-hangzhou.aliyuncs.com/admin/versionFile/2018/12/27/1/1_20181227144722.zip'
            local = os.path.join(r'/data/home/nao/nplus/download', 'tornado_new.zip')
            local_path=r'/data/home/nao/nplus/download'
            state_down=self.downloader(url,local,local_path)
            if state_down==True:
                z = ZFile(r'/data/home/nao/nplus/download/tornado_new.zip')
                result = z.extract_to(r'/data/home/nao/nplus/download')
                print(result)
                z.close()
                self.write(result)
            else:
                self.write(state_down)


    def downloader(self,url, path,local_path):
        if not os.path.exists(local_path):
            os.mkdir(local_path)
        # 开始时间
        start = time.time()
        size = 0
        response = requests.get(url, stream=True)
        chunk_size = 1024
        content_size = int(response.headers['content-length'])
        if response.status_code == 200:
            try:
                print('[文件大小]：%0.2f MB' % (content_size / chunk_size / 1024))
                with open(path, 'wb') as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        print('\r' + '[下载进度]:%s%.2f%%' % (
                        '>' * int(size * 50 / content_size), float(size*100 / content_size))),
                end = time.time()
                print('全部下载完成！用时%.2f秒' % (end - start))
                return True
            except Exception, e:
                print(e.message)
                print('下载失败，找不到本地下载路径')
                return 'find local path failed'
        else:
            print('下载失败，下载路径出错')
            return 'find service path failed'