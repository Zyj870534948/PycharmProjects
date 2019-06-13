#!/usr/bin/env python
# -*- coding:utf-8 -*-

# _author:"xiaolin"
# date:2018/8/7
# !/usr/bin/env python
# encoding: utf-8
# description: get local ip address

# import socket
# import fcntl
# import struct


# def get_ip_address(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(
#         s.fileno(),
#         0x8915,  # SIOCGIFADDR
#         struct.pack('256s', ifname[:15])
#     )[20:24])
#
# print get_ip_address('lo')
# print get_ip_address('eth0')
# import socket
# import config.globalvar as gl
# import config.global_variables

# def get_webview_url():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(('8.8.8.8', 80))
#     ip = s.getsockname()[0]
#     port = '8888'
#     webview_ip = 'http://' + str(ip) + ':' + port + '/'
#     print webview_ip

# get_webview_url()
# gl.get_value('homepage_rul')
# print gl.get_value('homepage_rul')
# import os
# TEMPLATE_PATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)), "template")
# STATIC_PATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)), "static")
# print TEMPLATE_PATH
# print STATIC_PATH

