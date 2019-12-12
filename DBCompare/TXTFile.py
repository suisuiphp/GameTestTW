# _*_ coding: utf-8 _*_
# from robot.api import logger
class TXTFile():
	# ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	# ROBOT_LIBRARY_VERSION = 0.1
	# ROBOT_LIBRARY_DOC_FORMAT = 'reST'
	def __init__(self):
		...
	
	def open(self, file, format):
		try:
			File = open(file, format)
		except Exception as e:
			print("*ERROR* ", repr(e))
		return File
	
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
		File = self.open(file, format)
		# 读文件到列表
		list_file = []
		if File != None:
			list_file = File.readlines()
		# 关闭文件
		self.close(File)
		return list_file
	
	def fileWrite(self, file, format, str):
		File = self.open(file, format)
		if File != None:
			try:
				File.write(str)
			except Exception as e:
				print("*ERROR*", repr(e))
			finally:
				self.close(File)
