#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _author:"sidalin"
import socket
import struct

class Thing:

    def __init__(self, MAC=[0, 0, 0, 0, 0, 0, 0, 0], LRAddress=("0.0.0.0", 0)):  # 传 MAC地址 和 （IP地址，端口号）
        self.MAC = MAC
        self.LRAddress = LRAddress

    def TTSt(self, a):  # 十进制转十六进制
        return (0x00 + a) & 0xff

    def MLC2(self, dir, i, a):  # 0x00移位
        if dir == 0:
            a <<= i
        else:
            a >>= i
        return a & 0xff

    def MLC4(self, dir, i, a):  # 0x0000移位
        if dir == 0:
            a <<= i
        else:
            a >>= i
        return a & 0xffff

    def StTS(self, a):  # 十六进制转字符
        return struct.pack("%dB" % (len(a)), *a)

    def CRC16_XMODEM(self, a):  # CRC_16_XMODEM校验
        c = treat = bcrc = 0x00
        wcrc = 0x0000
        for i in a:
            c = i & 0xff
            for j in range(8):
                treat = c & 0x80
                c = self.MLC2(0, 1, c)
                bcrc = (wcrc >> 8) & 0x80
                wcrc = self.MLC4(0, 1, wcrc)
                if treat != bcrc:
                    wcrc ^= 0x1021
        return wcrc

    def DecF(self, wcrc):  # 分解0x0000获取前两位0x00
        return (wcrc >> 8) & 0xff

    def DecA(self, wcrc):  # 分解0x0000获取后两位0x00
        return wcrc & 0xff

    def StSep(self, wcrc):  # 拼接两个0x00为0x0000
        return [self.DecF(wcrc), self.DecA(wcrc)]

    def Control(self, str):  # 控制发送帧包（帧内容）
        ctr = [0xa5, ]
        FP = []
        date = ""
        FP += ([0, len(str) + 13] + self.MAC + [00])
        for i in range(len(str)):
            FP += [str[i]]
        FP += self.StSep(self.CRC16_XMODEM(FP))
        ctr += (FP + [0x5a])
        date = self.StTS(ctr)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(date, self.LRAddress)
        print(ctr)
        s.close()

    def BFPacket(self, t):  # 亮度的帧内容
        str = [0x02, ]
        return str + [t]

    def RGBWFPacket(self, tR, tG, tB, tW):  # 变色的帧内容
        str = [0x03, ]
        str += [00, 01, 00, 00]
        return str + [tR, tG, tB, tW]

    def CTFPackage(self, t):  # 色温的帧内容
        str = [0x04, ]
        return str + self.StSep(t) + [0, 0]




brig = 0
isagain = 1
LRHOST = '192.168.3.46'  # IP地址
LRPORT = 13434  # 端口号
LRAddress = (LRHOST, LRPORT)
MAC = [0x62, 0x01, 0x94, 0x02, 0x2D, 0X6D, 0X00, 0x00]
ctr=Thing(MAC,LRAddress)

str1 = ctr.BFPacket(brig)
str2 = ctr.RGBWFPacket(255,255,255,255)
ctr.Control(str2)
ctr.Control(str1)
