#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__:"MrZhu"
'''
__introduce__

'''

import time
import os

# i = 10
# while i:
#     time.sleep(1)
#     f = open("/data/home/nao/nplus/MrZhu/test.wav","rb")
#     a = f.read()
#     f.close()
#     f = open("/data/home/nao/nplus/MrZhu/test.wav", "wb")
#     f.write("")
#     f.close()
#     d = open("/data/home/nao/nplus/MrZhu/a" + str(i) + ".wav","wb")
#     d.write(a)
#     d.close()
#     i -=1
#
# os.system('scriptreplay timing.log output.session')


# i = 10
# f = open("/data/home/nao/nplus/MrZhu/test2.wav", "wb+")
# while i:
#     d = open("/data/home/nao/nplus/MrZhu/a" + str(i) + ".wav","rb")
#     f.write(d.read())
#     d.close()
#     i -=1
#
# f.close()



import os
import numpy as np
f = open("C:/Users/N-pod/Desktop/test.wav")
f.seek(0)
f.read(44)
data = np.fromfile(f, dtype=np.int16)
data.tofile("test.pcm")