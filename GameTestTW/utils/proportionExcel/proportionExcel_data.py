#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

class ProportionExcleVariable:
	col_hy_gs = 1
	col_hy_fgs = 2
	col_hy_dzj = 3
	col_hy_zj = 4
	col_self_highest_proportion = 6
	col_down_lowest_proportion = 7
	col_down_highest_proportion = 8
	
	row_case1 = 0
	row_case2 = 8
	row_case3 = 17
	row_case4 = 25
	row_case5 = 33
	row_case6 = 42
	row_case7 = 51
	row_case8 = 60
	row_case9 = 70
	row_case10 = 80
	
def get_col_hy_gs():
	return ProportionExcleVariable.col_hy_gs

def get_col_hy_fgs():
	return ProportionExcleVariable.col_hy_fgs

def get_col_hy_dzj():
	return ProportionExcleVariable.col_hy_dzj

def get_col_hy_zj():
	return ProportionExcleVariable.col_hy_zj

def get_col_self_highest():
	return ProportionExcleVariable.col_self_highest_proportion


def get_case_row_id(case="case1"):
	if case == "case1":
		return ProportionExcleVariable.row_case1
	elif case == "case2":
		return ProportionExcleVariable.row_case2
	elif case == "case3":
		return ProportionExcleVariable.row_case3
	elif case == "case4":
		return ProportionExcleVariable.row_case4
	elif case == "case5":
		return ProportionExcleVariable.row_case5
	elif case == "case6":
		return ProportionExcleVariable.row_case6
	elif case == "case7":
		return ProportionExcleVariable.row_case7
	elif case == "case8":
		return ProportionExcleVariable.row_case8
	elif case == "case9":
		return ProportionExcleVariable.row_case9
	elif case == "case10":
		return ProportionExcleVariable.row_case10
	else:
		print("Case:%s not exsit!" % case)
		
def get_col_id_by_hy(hy="hy_gs"):
	if hy == "hy_gs":
		return get_col_hy_gs()
	elif hy == "hy_fgs":
		return get_col_hy_fgs()
	elif hy == "hy_dzj":
		return get_col_hy_dzj()
	elif hy == "hy_zj":
		return get_col_hy_zj()
	else:
		print("hy:%s not exsit" % hy)
