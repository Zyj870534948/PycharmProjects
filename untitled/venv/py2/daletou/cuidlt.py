#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import random

def fz():
    Front = []
    After = []

    t = 3   #开数1/3/6对应1/2/3
    y1 = 20 #年前两位
    y2 = 19 #年后两位
    m = 5   #月
    d = 30  #日

    gy1 = 19    #出生年前两位
    gy2 = 97    #出生年后两位
    gm =8   #出生月
    gd =15  #出生日
    gxz = 11  # 星座
    gx = 6  #姓
    gm = 17 #名
    gss = 8 #属生肖
    gzg = 0 #中宫

    while 1:
        F = random.randint(1,32)
        if len(Front) == 5:
            break
        else :
            if F in Front:
                pass
            else :
                Front.append(F)
    Front.sort()

    while 1:
        A = random.randint(1, 12)
        if len(After) == 2:
            break
        else :
            if A in After:
                pass
            else :
                After.append(A)
    After.sort()


    if t == 1:
        b = Front[0] - (y1+m)
        if b < 0:
            b *= -1
        while b > 32:
            b -= 32
        if b in Front:
            pass
        else :
            Front[0] = b

        b = Front[4] - (y2 + d)
        if b < 0:
            b *= -1
        while b > 32:
            b -= 32
        if b in Front:
            pass
        else:
            Front[4] = b

        b = After[0] - y1 + y2 - m + d
        if b < 0:
            b *= -1
        while b > 12:
            b -= 12
        if b in After:
            pass
        else:
            After[0] = b

    elif t == 2:
        b = Front[1] - (y1 + m)
        if b < 0:
            b *= -1
        while b > 32:
            b -= 32
        if b in Front:
            pass
        else:
            Front[1] = b

        b = Front[3] - (y2 + d)
        if b < 0:
            b *= -1
        while b > 32:
            b -= 32
        if b in Front:
            pass
        else:
            Front[3] = b

        b = After[1] + y1 - y2 + m - d
        if b < 0:
            b *= -1
        while b > 12:
            b -= 12
        if b in After:
            pass
        else:
            After[1] = b

    else :
        b = Front[2] - (y1 + m + y2 +d)
        if b < 0:
            b *= -1
        while b > 32:
            b -= 32
        if b in Front:
            pass
        else:
            Front[2] = b

        b = After[0] + y1 + y2 - m - d
        if b < 0:
            b *= -1
        while b > 12:
            b -= 12
        if b in After:
            pass
        else:
            After[0] = b

        b = After[1] - y1 - y2 + m + d
        if b < 0:
            b *= -1
        while b > 12:
            b -= 12
        if b in After:
            pass
        else:
            After[1] = b

    ps = 0
    for i in [8,8,2,1,2,8,6,6,7]:
        if random.randint(1,9) == i:
            ps += 10
        else :
            ps -= 6
    Front.sort()
    After.sort()
    if 0 in Front:
        Front[0] = 32
    if 0 in After:
        After[0] = 2
    Front.sort()
    After.sort()

    return [Front,After,ps]

g = 0
k = 0
bw = 0
sy = 0
wy = 0
kwy = 0


for i in range(10):
    while 1:
        a = fz()
        g += 1
        if a[2] > 70:
            print a[0],a[1],"比率：",a[2],"%"
            print "次数：", str(kwy).zfill(3), str(wy).zfill(3), str(sy).zfill(3), str(bw).zfill(3), str(k).zfill(3), str(
                g).zfill(3)
            break
        if g == 1000:
            g = 0
            k += 1
        if k == 1000:
            k = 0
            bw += 1
            print "次数：", str(kwy).zfill(3), str(wy).zfill(3), str(sy).zfill(3), str(bw).zfill(3), str(k).zfill(3), str(
                g).zfill(3)
        if bw == 1000:
            bw = 0
            sy += 1
            print "次数：", str(kwy).zfill(3), str(wy).zfill(3), str(sy).zfill(3), str(bw).zfill(3), str(k).zfill(3), str(
                g).zfill(3)
        if sy == 1000:
            sy = 0
            wy += 1
            print "次数：", str(kwy).zfill(3), str(wy).zfill(3), str(sy).zfill(3), str(bw).zfill(3), str(k).zfill(3), str(
                g).zfill(3)
        if wy == 1000:
            qy = 0
            kwy += 1
            print "次数：", str(kwy).zfill(3), str(wy).zfill(3), str(sy).zfill(3), str(bw).zfill(3), str(k).zfill(3), str(
                g).zfill(3)
    print("第",i,"个")


'''
[3, 8, 17, 18, 29] [2, 9] 比率： 74 %
[1, 2, 3, 13, 31] [5, 6] 比率： 74 %
[3, 11, 17, 26, 32] [1, 5] 比率： 74 %
[2, 18, 24, 27, 29] [4, 8] 比率： 74 %
[7, 15, 17, 22, 25] [3, 10] 比率： 74 %





[2, 3, 7, 22, 25] [4, 9]
[4, 18, 20, 22, 23] [1, 6]
[6, 17, 19, 28, 30] [8, 12]
[9, 11, 20, 26, 27] [2, 8]
[10, 15, 18, 27, 30] [1, 7]




'''