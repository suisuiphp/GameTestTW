#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

import xlrdtest

xlsx = xlrdtest.open_workbook("/Users/yan/Desktop/test.xlsx")
tabel = xlsx.sheet_by_name("初始限额")

print(tabel.cell_value(1,4))