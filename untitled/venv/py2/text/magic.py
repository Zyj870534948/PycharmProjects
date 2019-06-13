#!/usr/bin/env python
# -*- coding:utf-8 -*-

args=('one',32,2)
argss={"arg3":"3","arg1":1,"arg2":"two"}
dicts ={ "name":"瑾",
"sex":"男",
"age":20
}
arg = [1,2,3,4,5,6,7,8,9]

# 魔法变量放入我们调用参数
def fun(arg1,arg2,arg3):
    print("agr1", arg1)
    print("agr2", arg2)
    print("agr3", arg3)

# 魔法变量放入函数参数
def funs(arg,*args):
    print("第一个参数是",arg)
    print(args)
    for a in args:
        print("*arg中的参数是：",a)

# 正常顺序
def funss(arg,*args, **kwargs):
    print(arg)
    print(args)
    for k,v in kwargs.items():
        print("**argss中的参数是：{0}:{1}".format(k,v))

# 只放入 **kwargs
def funkwargs(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print("**argss中的参数是：{0}=={1}".format(k,v))


funss(1,args,dicts)