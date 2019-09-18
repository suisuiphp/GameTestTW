#!/usr/bin/env python
#coding:utf-8

#Author:TiFity
from utils.operationExcel import OperationExcel
from utils.public import *
from utils.proportionExcel.proportionExcel_data import *

class OpertionProportionExcel(OperationExcel):
	def __init__(self):
		self.sh = self.getExcelSheet(data_dir("data/proportionData", "proportionData.xls"))
	def getProxyProportions(self,case="case1",hy="hy_gs"):
		'''根据会员获取这条组织线各个组织的实际占成'''
		col = get_col_id_by_hy(hy)
		row = get_case_row_id(case)
		return self.sh.col_values(col,row,row+6)
	def getProxyConfig(self,case="case1",proxy="zgs"):
		'''
		查询一个组织的占成配置信息
		:param case: case编号
		:param proxy: 组织代号
		:return:
		'''
		base_row = get_case_row_id(case)
		row = base_row
		if proxy == "zgs":
			row = base_row + 1
		elif proxy == "gs":
			row = base_row + 2
		elif proxy == "fgs":
			row = base_row + 3
		elif proxy == "dzj":
			row = base_row + 4
		elif proxy == "zj":
			row = base_row + 5
		else:
			print("Wrong proxy name")
			
		col = get_col_self_highest()
		return self.sh.row_values(row,col,col+4)
	
		
if __name__ == '__main__':
	obj = OpertionProportionExcel()# print(obj.getProxyProportions(hy="hy_zj"))
	print(obj.getProxyConfig(case="case9",proxy="zgs"))
