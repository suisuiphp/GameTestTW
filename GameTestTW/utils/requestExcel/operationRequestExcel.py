#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
from utils.public import *
from requestExcel_data import *
from base.variables import *
import json

class OperationRequestExcel(OperationExcel):
	
	def __init__(self):
		self.operJson = OperationJson()
		self.sh = self.getExcelSheet(data_dir("data","requestData.xls"))
	def get_interface(self,interfaceName):
		'''
		获取请求接口
		:return:
		'''
		row = self.getRowIdByStr(self.sh,get_col_InterfaceName(),interfaceName)[0]
		return self.sh.cell_value(row,get_col_Interface())
	
	def get_requestdata(self,interfaceName):
		"""
		获取请求参数
		:param interfaceName:
		:return:
		"""
		row = self.getRowIdByStr(self.sh, get_col_InterfaceName(), interfaceName)[0]
		requestdata = self.sh.cell_value(row, get_col_RequestData())
		requestdata = self.operJson.getJsonDataByKey(data_dir("data","requestData.json"),requestdata)
	
		return json.dumps(requestdata)

	
	
		
	

if __name__ == '__main__':
    obj = OperationRequestExcel()
    # print(obj.get_member_interface("member_login_001"))
    print(obj.get_member_requestdata("member_login_001"))
    