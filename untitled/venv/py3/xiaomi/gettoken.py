#-*-coding:utf8-*-

import codecs

import socket

# from protocol import Message

helobytes=bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff')

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(helobytes,('192.168.3.36',54321))#插座ip，端口54321

data,addr=s.recvfrom(1024)

# m=Message.parse(data)

# tok=codecs.encode(m.checksum,'hex')

print(codecs.encode(data,'hex'))

# print(tok)


#bda249e4ff60873e77c3b2e49569ecd9
#bda249e4ff60873e77c3b2e49569ecd9
#f26ac8a464e02783563759055b6cd67f
# 213100200000000007dc3bf20023c2d300000000000000000000000000000000