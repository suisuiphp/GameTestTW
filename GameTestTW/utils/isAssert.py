#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

import unittest


class IsAssert(unittest.TestCase):
	
	def assertStatusCode(self, r, msg=None):
		flag = False
		if r.status_code in (200, 201, 304):
			flag = True
		self.assertEqual(True, flag, msg)
	
	def assertHasStr(self, full_str, sub_str, msg=None):
		'''
		验证sub_str是否在full_str中
		:param full_str:
		:param sub_str:
		:return:
		'''
		flag = False
		if sub_str in full_str:
			flag = True
		self.assertEqual(flag, True, msg)
	
	def assertNotNullStr(self, obj_str, msg=None):
		'''
		断言obj_str不是空字符串
		:param obj_str:
		:return:
		'''
		flag = True
		if obj_str == "":
			flag = False
		self.assertEqual(True, flag,msg)
	
	def assertNotNull(self, obj, msg=None):
		'''
		断言obj不是空字符串、空列表
		:param obj:
		:return:
		'''
		flag = True
		if not obj:
			flag = False
			self.assertEqual(True, flag, msg)
