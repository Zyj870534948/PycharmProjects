#!/usr/bin/env python
# coding=utf-8
# 爬取m3u8地址的所有ts文件并下载到"D:/video2/"，一般会有几千个文件耐心等待

# 下载阿丽塔
# https://sohu.zuida-163sina.com/20190223/TnSFbZPj/800kb/hls/jQQWmUN39911775.ts 其中一个ts文件地址

#https://vip2.pp63.org/201902/24/yaFQDHbf/600kb/hls/ciAnq6870234.ts
#https://vip2.pp63.org/share/V35jtLDkXZ4vRL71

# 第一步通过查看源代码可看到Referer地址如下，其中下载地址:https://sohu.zuida-163sina.com/20190223/TnSFbZPj/index.m3u8
# https://newplayers.pe62.com/mdparse/m3u8.php?id=https://sohu.zuida-163sina.com/20190223/TnSFbZPj/index.m3u8
# 第二步以上下载的文件中有个地址：/ppvod/FA7CC7B31F271DBD6F1A181E8429770D.m3u8
# 组合成地址："https://sohu.zuida-163sina.com/ppvod/FA7CC7B31F271DBD6F1A181E8429770D.m3u8"就可以下载了
import requests
import os, re
import time
import urllib.request

# https://sohu.zuida-163sina.com/20190223/TnSFbZPj/800kb/hls/jQQWmUN39911775.ts 通过这个可以确定url开头部分
# 将来需要拼接的每一个ts视频文件地址的开头
begin_url = "https://sohu.zuida-163sina.com"
length = len(begin_url)
# m3u8地址,下载下来会看到很多个ts文件名字组成
url = "https://sohu.zuida-163sina.com/ppvod/FA7CC7B31F271DBD6F1A181E8429770D.m3u8"

response = requests.get(url)
all_content = response.text
# 按照结尾的换行符进行切片操作
file_line = all_content.split("\n")
# 存储将来拼接的所有ts链接地址
url_list = []
header = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);'
}
for index, line in enumerate(file_line):
    if "EXTINF" in line:
        pd_url = begin_url + file_line[index + 1]  # 拼出ts片段的URL
        # print(pd_url)
        url_list.append(pd_url)
        # file_name = file_line[index+1][-10:-3]

url_length = len(url_list)
for i in range(url_length):
    add_url = url_list[i]
    # 正则取出数字文件名字
    patt = re.compile(r'\d+')
    file_name = add_url.split("/")[-1]
    request = urllib.request.Request(add_url, headers=header)
    response = urllib.request.urlopen(request)
    html = response.read()
    # result_file_name= url_list[i][length:][-10:-3]
    result_file_name = patt.findall(file_name)[0]
    print("正在处理%s" % result_file_name + ".ts", "共%s/%s项" % (i + 1, url_length))
    time.sleep(1)
    path = "D:/video2/"
    if (not os.path.exists(path)):
        os.makedirs(path)
    with open(path + result_file_name + '.ts', "wb")as f:
        f.write(html)