#!/usr/bin/env python
#coding:utf-8

#Author:TiFity
"""
需求：
1、对请求参数的进行ascill排序
2、排序后，对请求参数进行md5加密
"""
def sortKey(**kwargs):
    return dict(sorted(kwargs.items(),key=lambda item:item[0]))

def add_amount(amount=10):
    return lambda x : x+amount

def big(x):
    return x>11

def log(func):
    
    def wrapper(*args,**kwargs):
        print("-----start------")
        return func(*args,**kwargs)
    return wrapper

def log2(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print("%s,%s start" % (text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator
    
@log2("20190808")
def login(username,password):
    if username=="zhuoyan" and password=="123456":
        print("login success")
    else:
        print("wrong username or password")

if __name__ == '__main__':
    # print(""==None)
    # str1 = "\xe8\xb4\xa6\xe5\x8f\xb7\xe5\xb7\xb2\xe5\xad\x98\xe5\x9c\xa8"
    # print(str1.decode("utf-8"))
    #
    # list1 = [1,2]
    # list2 = [3,4]
    # list1.extend(list2)
    # print(list1)
    #
    #
    # dict3 = {"name": "wuya", "age": 18, "address": "xian"}
    # print(dict3.items())
    # print(sortKey(**dict3))
    # list3 = map(add_amount(amount=100),list1)
    # print(list3)
    #
    #
    # he = [x for x in range(3,20)]
    # print(he)
    # print(list(filter(lambda x:x>11,he)))
    #
    # login("zhuoyan","123456")

    print('\n'.join([''.join([('Love'[(x - y) % len('Love')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
                x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-50, 50)]) for y in range(50, -50, -1)]))
    
    
    

    