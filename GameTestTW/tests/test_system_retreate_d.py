#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

import unittest
from page.Retreat import Retreat

class TestSystemRetreateD(unittest.TestCase):
	'''
	test_system_retreate_d
	总公司：修改非独立调配公司初始限额
	'''
	
	def setUp(self):
		self.zgs = Retreat(user_type=1, id_mark="d")
		self.obj_id = self.zgs.ids["line1"][0]
		self.channel = 1

	def test_d01(self):
		'''总公司-修改非独立调配line1退水：不影响、等量增加'''
		rs = self.zgs.case(condition="1/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_101 1/1 fail")
	
	def test_d02(self):
		'''总公司-修改非独立调配line1退水：不影响、不等量增加'''
		rs = self.zgs.case(condition="1/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_102 1/2 fail")

	def test_d03(self):
		'''总公司-修改非独立调配line1退水：影响该层级、等量增加'''
		rs = self.zgs.case(condition="2/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_103 2/1 fail")

	def test_d04(self):
		'''总公司-修改非独立调配line1退水：影响该层级、不等量增加'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="2/2",normal_case=True,independent=True)
		rs = self.zgs.case(condition="2/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_104 2/2 fail")

	def test_d05(self):
		'''总公司-修改非独立调配line1退水：影响组织线、等量增加'''
		self.zgs.reset_retreat_data(condition="3/1", normal_case=True, independent=True)
		rs = self.zgs.case(condition="3/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_105 3/1 fail")

	def test_d06(self):
		'''总公司-修改非独立调配line1退水：影响该组织线、不等量增加'''
		self.zgs.reset_retreat_data(condition="3/2", normal_case=True, independent=True)
		rs = self.zgs.case(condition="3/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_106 3/2 fail")

	def test_d07(self):
		'''总公司-修改非独立调配line1退水：影响全部层级、等量增加'''
		print("------test_d07")
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="4/1", normal_case=True, independent=True)
		rs = self.zgs.case(condition="4/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_107 4/1 fail")

	def test_d08(self):
		'''总公司-修改非独立调配line1退水：影响全部层级、不等量增加'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="4/2", normal_case=True, independent=True)
		rs = self.zgs.case(condition="4/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_108 4/2 fail")

	def test_d09(self):
		'''总公司-修改非独立调配line1退水：全部影响、等量增加'''
		print("------test_d09")
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="5/1", normal_case=True, independent=True)
		rs = self.zgs.case(condition="5/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_109 5/1 fail")

	def test_d10(self):
		'''总公司-修改非独立调配line1退水：全部影响、不等量增加'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="5/2", normal_case=True, independent=True)
		rs = self.zgs.case(condition="5/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_110 5/2 fail")

	def test_d11(self):
		'''总公司-修改非独立调配line1退水：影响该层级，等量增加，被影响人等量增加后若大于上级，修改为等于上级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="2/1", normal_case=False, independent=True)
		rs = self.zgs.case(condition="2/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_111 2/1 fail")

	def test_d12(self):
		'''总公司-修改非独立调配line1退水：影响该层级，不等量增加成功，并且影响下级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="2/2", normal_case=False, independent=True)
		rs = self.zgs.case(condition="2/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_112 2/2 fail")

	def test_d13(self):
		'''总公司-修改非独立调配line1退水：影响全部层级，等量增加，被影响人等量增加后若大于上级，修改为等于上级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="4/1", normal_case=False, independent=True)
		rs = self.zgs.case(condition="4/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_113 4/1 fail")

	def test_d14(self):
		'''总公司-修改非独立调配line1退水：影响全部层级，不等量增加成功，并且影响下级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="4/2", normal_case=False, independent=True)
		rs = self.zgs.case(condition="4/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_114 4/2 fail")

	def test_d15(self):
		'''总公司-修改非独立调配line1退水：影响全部，等量增加，被影响人等量增加后若大于上级，修改为等于上级'''
		print("------test_d15")
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="5/1", normal_case=False, independent=True)
		rs = self.zgs.case(condition="5/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_115 5/1 fail")

	def test_d16(self):
		'''总公司-修改非独立调配line1退水：影响全部层级，不等量增加成功，并且影响下级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="5/2", normal_case=False, independent=True)
		rs = self.zgs.case(condition="5/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_116 2/2 fail")
		
if __name__ == '__main__':
	suite = unittest.TestSuite(unittest.makeSuite(TestSystemRetreateD))
	unittest.TextTestRunner(verbosity=2).run(suite)
