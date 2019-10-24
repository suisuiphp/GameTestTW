#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

import unittest
from page.Retreat import Retreat



class TestSystemRetreateA(unittest.TestCase):
	'''
	总公司：修改总公司初始限额
	'''
	def setUp(self):
		self.zgs = Retreat(user_type=1,id_mark="a")
		
	# def test_a01(self):
	# 	'''总公司-修改总公司初始限额：不影响、等量增加'''
	# 	rs = self.zgs.case(condition="1/1", channel=1, obj_id=1)
	# 	self.assertEqual(rs, True, "*ERROR* test_001 1/1 fail")
	#
	# def test_a02(self):
	# 	"""总公司-修改总公司初始限额：不影响、不等量增加"""
	# 	rs = self.zgs.case(condition="1/2", channel=1, obj_id=1)
	# 	self.assertEqual(rs, True, "*ERROR* test_002 1/2 fail")
	#
	# def test_a03(self):#20190801-fail
	# 	"""总公司-修改总公司初始限额：影响该层级、等量增加"""
	# 	rs = self.zgs.case(condition="2/1", channel=1, obj_id=1)
	# 	self.assertEqual(rs, True, "*ERROR* test_003 2/1 fail")
	#
	# def test_a04(self):#20190801-fail
	# 	"""总公司-修改总公司初始限额：影响该层级、不等量增加"""
	# 	rs = self.zgs.case(condition="2/2", channel=1, obj_id=1)
	# 	self.assertEqual(rs, True, "*ERROR* test_004 2/2 fail")

	def test_a05(self):  # ----------20191009 失败，独立调配的公司下的会员被影响了了
		"""总公司-修改总公司初始限额：影响该组织线、等量增加"""
		self.zgs.reset_retreat_data(condition="3/1",normal_case=True,independent=False)
		rs = self.zgs.case(condition="3/1", channel=1, obj_id=1)
		self.assertEqual(rs, True, "*ERROR* 3/1 fail")

	def test_a06(self): # ----------20191009 失败，独立调配的公司下的会员被影响了了
		"""总公司-修改总公司初始限额：影响该组织线、不等量增加"""
		self.zgs.reset_retreat_data(condition="3/2",normal_case=True,independent=False)
		rs = self.zgs.case(condition="3/2", channel=1, obj_id=1)
		self.assertEqual(rs, True, "*ERROR* 3/2 fail")

	def test_a07(self):# ----------20191009 失败 下级管理层级未被影响
		"""总公司-修改总公司初始限额：影响全部层级、等量增加"""
		self.zgs.reset_retreat_data(condition="3/1",normal_case=True,independent=False) #总公司这里的初始化用"3/1"就可以了
		rs = self.zgs.case(condition="4/1", channel=1, obj_id=1)
		self.assertEqual(rs, True, "*ERROR* 4/1 fail")

	def test_a08(self):# ----------20191009 失败 下级管理层级未被影响
		"""总公司-修改总公司初始限额：影响全部层级、不等量增加"""
		self.zgs.reset_retreat_data(condition="3/1",normal_case=True,independent=False)  # 总公司这里的初始化用"3/1"就可以了
		rs = self.zgs.case(condition="4/2", channel=1, obj_id=1)
		self.assertEqual(rs, True, "*ERROR* 4/2 fail")

	def test_a09(self): # ----------20191009 失败 下级会员未被影响
		"""总公司-修改总公司初始限额：全部影响、等量增加"""
		self.zgs.reset_retreat_data(condition="3/1",normal_case=True,independent=False)  # 总公司这里的初始化用"3/1"就可以了
		rs = self.zgs.case(condition="5/1", channel=1, obj_id=1)
		self.assertEqual(rs, True, "*ERROR* 4/1 fail")

	def test_a10(self):# ----------20191009 失败 下级会员未被影响
		"""总公司-修改总公司初始限额：全部影响、不等量增加"""
		self.zgs.reset_retreat_data(condition="3/1",normal_case=True,independent=False)  # 总公司这里的初始化用"3/1"就可以了
		rs = self.zgs.case(condition="5/2", channel=1, obj_id=1)
		self.assertEqual(rs, True, "*ERROR* 5/2 fail")



if __name__ == '__main__':
	suite = unittest.TestSuite(unittest.makeSuite(TestSystemRetreateA))
	unittest.TextTestRunner(verbosity=2).run(suite)
