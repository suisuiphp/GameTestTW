#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

import os,time

def data_dir(dirname=None,filename=None):
	'''
	查找文件路径
	:param dirname:工程下面的文件夹名称
	:param filename:文件名称
	:return:返回文件名称的绝对路径
	'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),dirname,filename)

print(data_dir("data","requestData.json"))

def getDate():
	return time.strftime("%Y-%m-%d", time.localtime(time.time()))

def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))