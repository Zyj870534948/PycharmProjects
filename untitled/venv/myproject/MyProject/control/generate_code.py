#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/31
# 生成连接二维码，二维码的地址在static/images

import os
import sys


#生成二维码图片并保存
class GenerateCode:
    def save_code(self, url,imageName):
        sys.path.append(os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../")), "mylib"))
        import qrcode
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=8, border=8, )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image()
        address = os.path.join(
            os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../")), "static/images/"+imageName+r'.png'))
        print(address)
        img.save(address)


if __name__ == '__main__':
    g = GenerateCode()
    #参数一是网页地址比如www:baidu.com，参数二是图片名称
    g.save_code('http://zhida.nplusgroup.com/phone/results/index.htm','code')
