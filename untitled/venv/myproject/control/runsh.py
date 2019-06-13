#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"

import os
class Runsh:
    def main(self):
        os.chdir('/data/home/nao/nplus/download/MyProject/')
        cmd="chmod a+x a.sh"
        os.popen(cmd)
        os.popen("./a.sh")

if __name__ == '__main__':
    rs=Runsh()
    rs.main()