#!/usr/bin/env python
# -*- coding:utf-8 -*-

#_author:"sidalin"
import config.globalvar as gl
import config.global_variables
class Changeip:
    def changeIp(self,file,ip):
        file_data = ""
        for count, line in enumerate(open(file, 'r')):
            if count == 0:
                line = 'myself_ip = \'' + str(ip) + '\'' + '\n'
                file_data += line
            else:
                file_data += line
        with open(file, "w") as f:
            f.write(file_data)
        print 'success'


if __name__ == '__main__':
    c = Changeip()
    # c.chang_ip('../static/js/alluse.js',gl.get_value('robot_ip'))
    c.chang_ip('../static/js/alluse.js', '192.168.3.2')
