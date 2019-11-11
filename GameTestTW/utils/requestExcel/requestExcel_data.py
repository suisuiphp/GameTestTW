#!/usr/bin/env python
#coding:utf-8

#Author:TiFity


class ExcleVariable:
	col_InterfaceName = 1  # 接口名称列id
	col_Interface = 3  # 接口地址列id
	col_RequestData = 4  # 请求数据列id
	
def get_col_InterfaceName():
	'''
	获取接口名称列id
	:return: 接口名称列id
	'''
	return ExcleVariable.col_InterfaceName

def get_col_Interface():
	'''
	获取接口地址列id
	:return: 接口地址列id
	'''
	return ExcleVariable.col_Interface

def get_col_RequestData():
	'''
	获取请求数据列id
	:return: 请求数据列id
	'''
	return ExcleVariable.col_RequestData
