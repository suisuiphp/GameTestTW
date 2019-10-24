#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

import xlrd,xlwt
from xlutils.copy import copy

class OperationExcel(object):
	def getExcelSheet(self,filename,sheet_id=0):
		'''
		打开Excel文件，并返回id对应的sheet
		:param filename:
		:param sheet_id:
		:return:
		'''
		wb = xlrd.open_workbook(filename)
		ws = wb.sheet_by_index(sheet_id)
		return ws
	def getIdByStr(self,filename,sheet_id=0,str=None):
		'''
		查询字符串在excel中的ID
		:param filename:
		:param sheet_id:
		:param str:
		:return:
		'''
		rs = []
		ws = self.getExcelSheet(filename,sheet_id)
		for row in range(0,ws.nrows):
			for col in range(0,ws.ncols):
				if ws.cell_value(row,col) == str:
					rs.append((row,col))
		return rs
	
	def getRowIdByStr(self,sheet,col_id,str):
		'''
		查询一个字符串在某一列中的行号
		:param sheet:
		:param col_id:
		:param str:
		:return:
		'''
		rs = []
		for row in range(0,sheet.nrows):
			if sheet.cell_value(row,col_id) == str:
				rs.append(row)
		return rs
	
	def getColIdByStr(self,sheet,row_id,str):
		'''
		查询一个字符串在某一行中的列号
		:param sheet:
		:param row_id:
		:param str:
		:return:
		'''
		rs = []
		for col in range(0,sheet.ncols):
			if sheet.cell_value(row_id,col) == str:
				rs.append(col)
		return rs
	