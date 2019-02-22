#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import time
import json
import requests
import base64

def get_gateway_heart():
    SENDERIP = "192.168.3.21"
    MYPORT = 9898
    MYGROUP = '224.0.0.50'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    #allow multiple sockets to use the same PORT number   允许多个套接字使用相同的端口号
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    #Bind to the port that we know will receive multicast data   绑定到我们知道将接收多播数据的端口
    sock.bind((SENDERIP,MYPORT))
    #tell the kernel that we are a multicast socket   告诉内核我们是多播套接字
    #sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
    #Tell the kernel that we want to add ourselves to a multicast group 告诉内核我们要将自己添加到多播组中
    #The address for the multicast group is the third param   多播组的地址是第三个参数
    status = sock.setsockopt(socket.IPPROTO_IP,
        socket.IP_ADD_MEMBERSHIP,
        socket.inet_aton(MYGROUP) + socket.inet_aton(SENDERIP))

    #sock.setblocking(0)
    #ts = time.time()
    data, addr = sock.recvfrom(1024)
    data_str=str(data)   #,encoding='utf-8'
#    sock.close()

    return data_str


if __name__=='__main__':
    SENDERIP = "192.168.3.21"
    MYPORT = 9898
    MYGROUP = '224.0.0.50'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # allow multiple sockets to use the same PORT number   允许多个套接字使用相同的端口号
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind to the port that we know will receive multicast data   绑定到我们知道将接收多播数据的端口
    sock.bind((SENDERIP, MYPORT))
    # tell the kernel that we are a multicast socket   告诉内核我们是多播套接字
    # sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
    # Tell the kernel that we want to add ourselves to a multicast group 告诉内核我们要将自己添加到多播组中
    # The address for the multicast group is the third param   多播组的地址是第三个参数
    status = sock.setsockopt(socket.IPPROTO_IP,
                             socket.IP_ADD_MEMBERSHIP,
                             socket.inet_aton(MYGROUP) + socket.inet_aton(SENDERIP))

    # sock.setblocking(0)
    # ts = time.time()
    temperature,humidity = 0,0

    while 1:
        # data = '{"cmd":"read","sid":"158d0002b53b55"}'
        # sock.sendto(data, ("192.168.3.23", 9898))

        data = '{"cmd":"whois"}'
        sock.sendto(data, ("224.0.0.50", 4321))

        data, addr = sock.recvfrom(1024)
        data_str = str(data)  # ,encoding='utf-8'
        #    sock.close()

        data_zd = json.loads(data_str)
        print data_zd


        if 'token' in data_zd:
            token = data_zd["token"]
            print token



        # data_TH = json.loads(data_zd["data"])
        # if "temperature" in data_TH:
        #     temperature = float(data_TH["temperature"])
        #     temperature /= 100
        #     humidity /= 100
        # print "温度：" + str(temperature) + "℃"
        # print "湿度：" + str(humidity) + "%"
        # sT = "温度：" + str(temperature) + "℃"
        # sH = "湿度：" + str(humidity) + "%"
        # # s2TH = base64.b64encode(sTH)
        # filedata = {"Tdata": sT,
        #             "Hdata": sH,}
        # # requests.post(url="http://192.168.3.21:11111/THdata", data=filedata)
        # # resp=requests.get(url="http://192.168.3.21:11111/THdata", params=filedata)
        # # print resp.content
        
        time.sleep(3)

'''
    data = '{"cmd":"write","model":"gateway","sid":"04cf8c8fab20","short_id":0,"data":"{\"rgb\":4278255360,\"illumination\":500}" }'
    sock.sendto(data, ("192.168.3.23", 9898))
    # sock.sendto(data, ("224.0.0.50", 4321))
    data, addr = sock.recvfrom(1024)
    data_str = str(data)  # ,encoding='utf-8'
    #    sock.close()

    data_zd = json.loads(data_str)
    print data_zd
'''