#!/usr/bin/env python
# coding:utf-8

# Author:TiFity
"""
需求：
1、对请求参数的进行ascill排序
2、排序后，对请求参数进行md5加密
"""


def sortKey(**kwargs):
	return dict(sorted(kwargs.items(), key=lambda item: item[0]))


def add_amount(amount=10):
	return lambda x: x + amount


def big(x):
	return x > 11


def log(func):
	def wrapper(*args, **kwargs):
		print("-----start------")
		return func(*args, **kwargs)
	
	return wrapper


def log2(text):
	def decorator(func):
		def wrapper(*args, **kwargs):
			print("%s,%s start" % (text, func.__name__))
			return func(*args, **kwargs)
		
		return wrapper
	
	return decorator


class Fruit():
	def __init__(self,name):
		self.name = name
		self.age = 18
		
class Apple(Fruit):
	def __init__(self,name,color):
		Fruit.__init__(self,name)
		self.color = color


@log2("20190808")
def login(username, password):
	if username == "zhuoyan" and password == "123456":
		print("login success")
	else:
		print("wrong username or password")


if __name__ == '__main__':
	ob = Apple("苹果","红色")
	print ob.name
	print ob.age
	
	
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
	#
	# '''对请求参数进行assci排序'''
	# info = {"name": "zhuoyan", "age": 18, "city": "xian", "work": "tester"}
	# info = dict(sorted(info.items(), key=lambda item: item[0]))
	#
	# '''做urlencode编码 name=zhuoyan&age=18&city=xian&work=tester'''
	# # 用python2：urllib.urlencode(dict)
	# import urllib
	#
	# url_data = urllib.urlencode(info)  # info 是字典
	# print(url_data)  # city=xian&age=18&work=tester&name=zhuoyan
	#
	# # #  用python3：urllib.parse.urlencode(dict)
	# # from urllib import parse
	# # url_data = parse.urlencode(info)  # info 是字典
	# # print(url_data)  # city=xian&age=18&work=tester&name=zhuoyan
	#
	# '''md5加密'''
	# import hashlib
	#
	# md5 = hashlib.md5()  # 创建一个md5实例
	# md5.update(url_data.encode("utf-8"))  # 用md5实例update函数对数据进行加密，参数必须是unicode类型
	# print(md5.hexdigest())  # 57bb75530f6a588cd53fc16a22688c0a
	# info["sign"] = md5.hexdigest()  #用md5加密后的结果填入字典的sign里面

	url1 = "http://admin.win2019.cc/server/api/tw_manage/system_manage/limit_quota"
	url2 = "http://admin.win2019.cc/server/api/tw_manage/system_manage/limit_quota"
	
	headers1 = {'token': u'83bb2803ab2df1f68fcca9b1e8b3854182aaf77356598bed44e9d4b188212c40', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36', 'Content-Type': 'application/json', 'cache-control': 'no-cache'}
	headers2 = {'token': u'5f3bf5b2bf3c9a0a6846d68d59727c6637554b4d3eea4be1cf8640d480b60916', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36', 'Content-Type': 'application/json', 'cache-control': 'no-cache'}
	
	data1 = {"link_item": "1", "equal_add": "1", "organization_id": 1, "setting_group_ids": [220], "data": [{"in_data": [{"single_highest_quota": 30090.0, "origin_a_proportion": 480.0, "group": 1, "origin_b_proportion": 490.0, "origin_single_highest_quota": 30080.0, "origin_f_proportion": 530.0, "b_proportion": 500.0, "d_proportion": 520.0, "f_proportion": 540.0, "c_proportion": 510.0, "setting_group_id": 220, "origin_c_proportion": 500.0, "single_lowest_quota": 490.0, "origin_e_proportion": 520.0, "a_proportion": 490.0, "single_period_quota": 300090.0, "e_proportion": 530.0, "origin_d_proportion": 510.0, "origin_single_period_quota": 300080.0, "origin_single_lowest_quota": 480.0}], "lottery_id": 6}], "channel": 1}
	data2 = {"link_item": "1", "equal_add": "1", "organization_id": 1, "setting_group_ids": [220], "data": [{"in_data": [{"single_highest_quota": 30100.0, "origin_a_proportion": 490.0, "group": 1, "origin_b_proportion": 500.0, "origin_single_highest_quota": 30090.0, "origin_f_proportion": 540.0, "b_proportion": 510.0, "d_proportion": 530.0, "f_proportion": 550.0, "c_proportion": 520.0, "setting_group_id": 220, "origin_c_proportion": 510.0, "single_lowest_quota": 500.0, "origin_e_proportion": 530.0, "a_proportion": 500.0, "single_period_quota": 300100.0, "e_proportion": 540.0, "origin_d_proportion": 520.0, "origin_single_period_quota": 300090.0, "origin_single_lowest_quota": 490.0}], "lottery_id": 6}], "channel": 1}