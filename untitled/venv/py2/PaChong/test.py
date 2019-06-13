#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import cookielib
import urllib2
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.66s.cc/e/DownSys/play/?classid=14&id=10651&pathid1=0&bf=0"
response1 = urllib2.urlopen(url)

html_doc = response1.read()

# 创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")
# 获取所有的链接
links = soup.find_all('a')
print "所有的链接"
for link in links:
    print link.name, link['href']  #, link.get_text()

# print "获取特定的URL地址"
# link_node = soup.find('a', href="http://example.com/elsie")
# print link_node.name, link_node['href'], link_node['class'], link_node.get_text()
#
# print "正则表达式匹配"
# link_node = soup.find('a', href=re.compile(r"ti"))
# print link_node.name, link_node['href'], link_node['class'], link_node.get_text()
#
# print "获取P段落的文字"
# p_node = soup.find('p', class_='story')
# print p_node.name, p_node['class'], p_node.get_text()