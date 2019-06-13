#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import os

f = open(r"C:\Users\N-pod\Desktop\color.txt","r")

str = f.read()
print str[3],ord(str[4]),str[5],str[6],str[7],ord(str[60])

colordic = {}
colorname = ""
colorR = 0
colorG = 0
colorB = 0
i = 0
while i < len(str):
    print ord(str[i]),colorname,str[i],
    if (ord(str[i])>=65 and ord(str[i])<=122) or ((ord(str[i])>=48 and ord(str[i])<=57) and ord(str[i+1])==9) :
        print 1
        colorname += str[i]
        i += 1
    elif (ord(str[i])>=48 and ord(str[i])<=57) and ord(str[i-1])==9:
        print 2
        if ord(str[i+1])==32:
            colorR = int(str[i])
            if ord(str[i + 3]) == 32:
                colorG = int(str[i + 2])
                if ord(str[i + 5]) == 9:
                    colorB = int(str[i + 4])
                    k=6
                elif ord(str[i + 6]) == 9:
                    colorB = int(str[i + 4] + str[i + 5])
                    k =7
                elif ord(str[i + 7]) == 9:
                    colorB = int(str[i + 4] + str[i + 5] + str[i + 6])
                    k =8

            elif ord(str[i + 4]) == 32:
                colorG = int(str[i + 2] + str[i + 3])
                if ord(str[i + 6]) == 9:
                    colorB = int(str[i + 5])
                    k =7
                elif ord(str[i + 7]) == 9:
                    colorB = int(str[i + 5] + str[i + 6])
                    k =8
                elif ord(str[i + 8]) == 9:
                    colorB = int(str[i + 5] + str[i + 6] + str[i + 7])
                    k =9

            elif ord(str[i + 5]) == 32:
                colorG = int(str[i + 2] + str[i + 3] + str[i + 4])
                if ord(str[i + 7]) == 9:
                    colorB = int(str[i + 6])
                    k =8
                elif ord(str[i + 8]) == 9:
                    colorB = int(str[i + 6] + str[i + 7])
                    k =9
                elif ord(str[i + 9]) == 9:
                    colorB = int(str[i + 6] + str[i + 7] + str[i + 8])
                    k =10

        elif ord(str[i+2])==32:
            colorR = int(str[i] + str[i + 1])
            if ord(str[i + 4]) == 32:
                colorG = int(str[i + 3])
                if ord(str[i + 6]) == 9:
                    colorB = int(str[i + 5])
                    k =7
                elif ord(str[i + 7]) == 9:
                    colorB = int(str[i + 5] + str[i + 6])
                    k =8
                elif ord(str[i + 8]) == 9:
                    colorB = int(str[i + 5] + str[i + 6] + str[i + 7])
                    k =9

            elif ord(str[i + 5]) == 32:
                colorG = int(str[i + 3] + str[i + 4])
                if ord(str[i + 7]) == 9:
                    colorB = int(str[i + 6])
                    k =8
                elif ord(str[i + 8]) == 9:
                    colorB = int(str[i + 6] + str[i + 7])
                    k =9
                elif ord(str[i + 9]) == 9:
                    colorB = int(str[i + 6] + str[i + 7] + str[i + 8])
                    k =10

            elif ord(str[i + 6]) == 32:
                colorG = int(str[i + 3] + str[i + 4] + str[i + 5])
                if ord(str[i + 8]) == 9:
                    colorB = int(str[i + 7])
                    k =9
                elif ord(str[i + 9]) == 9:
                    colorB = int(str[i + 7] + str[i + 8])
                    k =10
                elif ord(str[i + 10]) == 9:
                    colorB = int(str[i + 7] + str[i + 8] + str[i + 9])
                    k =11

        elif ord(str[i+3])==32:
            colorR = int(str[i] + str[i + 1] + str[i + 2])
            if ord(str[i + 5]) == 32:
                colorG = int(str[i + 4])
                if ord(str[i + 7]) == 9:
                    colorB = int(str[i + 6])
                    k =8
                elif ord(str[i + 8]) == 9:
                    colorB = int(str[i + 6] + str[i + 7])
                    k =9
                elif ord(str[i + 9]) == 9:
                    colorB = int(str[i + 6] + str[i + 7] + str[i + 8])
                    k =10

            elif ord(str[i + 6]) == 32:
                colorG = int(str[i + 4] + str[i + 5])
                if ord(str[i + 8]) == 9:
                    colorB = int(str[i + 7])
                    k =9
                elif ord(str[i + 9]) == 9:
                    colorB = int(str[i + 7] + str[i + 8])
                    k =10
                elif ord(str[i + 10]) == 9:
                    colorB = int(str[i + 7] + str[i + 8] + str[i + 9])
                    k =11

            elif ord(str[i + 7]) == 32:
                colorG = int(str[i + 4] + str[i + 5] + str[i + 6])
                if ord(str[i + 9]) == 9:
                    colorB = int(str[i + 8])
                    k =10
                elif ord(str[i + 10]) == 9:
                    colorB = int(str[i + 8] + str[i + 9])
                    k =11
                elif ord(str[i + 11]) == 9:
                    colorB = int(str[i + 8] + str[i + 9] + str[i + 10])
                    k =12

        i+=k
    elif ord(str[i]) == 35:
        print 3
        colordic[colorname] = (colorR,colorG,colorB)
        colorname = ""
        i+=8
    else:
        print 4
        i += 1

print colordic,len(colordic)