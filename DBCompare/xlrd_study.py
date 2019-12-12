#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

import xlrd,xlwt
from copy import deepcopy
import time,functools



# xlsx = xlrd.open_workbook("/Users/yan/Desktop/test.xlsx")
# # table = xlsx.sheet_by_name(r"初始限额")
# table = xlsx.sheet_by_index(0)
# for row in range(0,table.nrows):
# 	print(table.row_values(row))

# print(table.col_values(1,0))
# print(dir(table))
# print(table.cell(0,0))

# for row in range(0,table.nrows):
# 	if table.cell_value(row,0) == "case2":
# 		print("find case in row %d" % row)
#
# print(table.cell_xf_index(0,0))


# def find_cell_index(str,sheet):
# 	for row in range(0,sheet.nrows):
# 		for col in range(0,sheet.ncols):
# 			if sheet.cell_value(row,col) == str:
# 				return row,col
# 	return
#
# row,col = find_cell_index("case2",table)
# print(row,col)





# def assert_value():
# 	pass
#
# print(table.col_values(1))
# table.cell_xf_index()


# print(table.cell_value(1,4))
#
#
# print(table.row(1)[4].value)
#
# new_book = xlwt.Workbook()
# worksheet = new_book.add_sheet("new_test")
# worksheet.write(0,0,"test")
# new_book.save("/Users/yan/Desktop/test1.xlsx")

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		print("excite：%s %s" % (func.__name__,time.localtime()))
		return func(*args,**kwargs)
		
	return wrapper

@log
def login(username,password):
	if username == "zhuoyan" and password=="123456":
		print("welcome,zhuoyan")
	else:
		print("用户名或密码错误")
		
login("zhuoyan","123456")



