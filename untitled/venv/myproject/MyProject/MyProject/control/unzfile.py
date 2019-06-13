#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"sidalin"


import os
import os.path
import zipfile

# Zip文件处理类
class ZFile(object):
    def __init__(self, filename, mode='r', basedir=''):
        try:
            self.filename = filename
            self.mode = mode
            if self.mode in ('w', 'a'):
                self.zfile = zipfile.ZipFile(filename, self.mode, compression=zipfile.ZIP_DEFLATED)
            else:
                self.zfile = zipfile.ZipFile(filename, self.mode)
            self.basedir = basedir
            if not self.basedir:
                self.basedir = os.path.dirname(filename)
        except Exception as e:
            pass

    def addfile(self, path, arcname=None):
        path = path.replace('//', '/')
        if not arcname:
            if path.startswith(self.basedir):
                arcname = path[len(self.basedir):]
            else:
                arcname = ''
        self.zfile.write(path, arcname)

    def addfiles(self, paths):
        for path in paths:
            if isinstance(path, tuple):
                self.addfile(*path)
            else:
                self.addfile(path)

    def close(self):
        try:
            self.zfile.close()
        except Exception as e:
            pass

    def extract_to(self, path):
        try:
            for p in self.zfile.namelist():
                self.extract(p, path)
            return 'success'
        except Exception as e:
            return e.message

    def extract(self, filename, path):
        if not filename.endswith('/'):
            f = os.path.join(path, filename)
            dir = os.path.dirname(f)
            if not os.path.exists(dir):
                os.makedirs(dir)
            file(f, 'wb').write(self.zfile.read(filename))


# 创建Zip文件
# def createZip(zfile, files):
#     z = ZFile(zfile, 'w')
#     z.addfiles(files)
#     z.close()



# 解压缩Zip到指定文件夹
def extractZip(zfile, path):
    z = ZFile(zfile)
    z.extract_to(path)
    z.close()


# 获得文件名和后缀
# def GetFileNameAndExt(filename):
#     (filepath, tempfilename) = os.path.split(filename);
#     (shotname, extension) = os.path.splitext(tempfilename);
#     return shotname, extension
if __name__ == '__main__':
    # extractZip(r'D:\zfile\tornado_new.zip',r'D:\zfile')
    z = ZFile(r'D:\zfile\tornado_new.zip')
    result=z.extract_to(r'D:\zfile')
    print(result)
    z.close()

