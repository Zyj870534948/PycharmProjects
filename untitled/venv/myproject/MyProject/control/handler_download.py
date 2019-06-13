#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import tornado.web
import os,time,requests
from unzfile import ZFile
from api_downloadurl import Downloadurl_api
from runsh import Runsh

class DownloadHandler(tornado.web.RequestHandler):
    def get(self):
        state=self.get_argument('state')
        if state=='on':
            downapi=Downloadurl_api()
            result=downapi.main_get()
            if result.has_key('loadUrl'):
                # url = 'https://pepper-test.oss-cn-hangzhou.aliyuncs.com/admin/versionFile/2019/01/02/1/1_20190102182112.zip'
                url = result['loadUrl']
                local = os.path.join(r'/data/home/nao/nplus/download', 'MyProject.zip')
                local_path=r'/data/home/nao/nplus/download'
                state_down=self.downloader(url,local,local_path)
                if state_down==True:
                    z = ZFile(r'/data/home/nao/nplus/download/MyProject.zip')
                    result = z.extract_to(r'/data/home/nao/nplus/download')
                    z.close()
                    self.write(result)
                    time.sleep(5)
                    if result=='success':
                        rs=Runsh()
                        rs.main()
                else:
                    self.write(state_down)
            else:
                self.write(result['errorMsg'])


    def downloader(self,url, path,local_path):
        if not os.path.exists(local_path):
            os.mkdir(local_path)
        # 开始时间
        start = time.time()
        size = 0
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.get(url=url,headers=headers,stream=True,verify=False)
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
            except Exception as e:
                print(e.message)
                print('下载失败，找不到本地下载路径')
                return 'find local path failed'
        else:
            print('下载失败，下载路径出错')
            return 'find service path failed'