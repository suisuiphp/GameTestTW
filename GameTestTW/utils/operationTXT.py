#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

class OperationTxt():

	def __init__(self):
		pass
	
	def open(self, file, format):
		try:
			fp = open(file, format)
		except Exception as e:
			print("*ERROR* ", repr(e))
		return fp
	
	def close(self, file):
		try:
			file.close()
		except Exception as e:
			print("*ERROR* ", repr(e))
	
	def fileRead(self, file, format):
		'''
		按行读取TXT文件中所以数据
		:param file:
		:param format:
		:return: 返回行数数据列表
		'''
		# 打开文件
		fp = self.open(file, format)
		# 读文件到列表
		list_file = []
		if fp != None:
			list_file = fp.readlines()
		# 关闭文件
		self.close(fp)
		return list_file
	
	def fileWrite(self, file, format, str):
		fp = self.open(file, format)
		if fp != None:
			try:
				fp.write(str)
			except Exception as e:
				print("*ERROR*", repr(e))
			finally:
				self.close(fp)
