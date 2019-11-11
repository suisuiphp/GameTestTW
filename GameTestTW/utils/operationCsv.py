#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

import csv
from public import *


class OperationCsv(object):
	
	def __init__(self):
		pass
	
	def readCsvList(self, file):
		'''
		按行读取数据，，一行为一个列表，返回数据列表
		:param file: csv文件
		:return: 按行读取数据的列表
		'''
		try:
			if file[-4:] != ".csv":
				print("*ERROR* File Type can only be csv")
		except Exception as e:
			print("*ERROR* params file error")
			
		with open(file,"r") as f:
			reader = csv.reader(f)
			return [data for data in reader]
	
	def readCsvDict(self, file):
		'''
		按字典的形式读取数据,一行数据一个字典，返回字典列表
		:param file: csv文件
		:return: 字典列表
		'''
		try:
			if file[-4:] != ".csv":
				print("*ERROR* File Type can only be csv")
		except Exception as e:
			print("*ERROR* params file error")
		
		with open(file, "r") as f:
			reader = csv.DictReader(f)
			return [data for data in reader]
		
	def writeCsvDict(self,file,format,headers,data):
		'''
		已字典的形式写入数据
		:param file: 文件名
		:param format: "w"：覆盖；"a"：追加
		:param headers: 表头headers = {"InterfaceName", "Title", "Module", "RequestData", "Expect", "Interface", "Result"}
		:param data: [{},{}]
		:return:
		'''
		try:
			if file[-4:] != ".csv":
				print("*ERROR* File Type can only be csv")
		except Exception as e:
			print("*ERROR* params file error")
			
		with open(file, format) as f:
			write = csv.DictWriter(f,headers)
			write.writeheader()
			write.writerows(data)
			
	def writeCsvList(self,file,format,data):
		'''
		以列表的形式写入csv
		:param file: 文件名
		:param format: format: "w"：覆盖；"a"：追加
		:param data: [[],[]]
		:return:
		'''
		try:
			if file[-4:] != ".csv":
				print("*ERROR* File Type can only be csv")
		except Exception as e:
			print("*ERROR* params file error")
			
		with open(file, format) as f:
			write = csv.writer(f)
			write.writerows(data)
		
		
if __name__ == '__main__':
    file = data_dir("data","requestData.csv")
    obj = OperationCsv()
    data = obj.readCsvList(file)
    
    lagou = data_dir("data","lagou.csv")
    obj.writeCsvList(lagou,"w",data)
    

