#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

import unittest
from page.Retreat import Retreat

class TestSystemRetreateC(unittest.TestCase):
	'''
	独立调配公司：修改自己的初始限额
	'''
	
	def setUp(self):
		self.zgs = Retreat(user_type=1, id_mark="c")
		self.gs = Retreat(user_type=1, id_mark="c", username="zy-gs01", password="6yhn6tfc")
		self.obj_id = self.zgs.ids["line1"][0]
		self.channel = 1
		print(self.gs.account)


	def test_c01(self):
		'''独立公司-修改独立调配line1退水：不影响、等量增加'''
		rs = self.gs.case(condition="1/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_201 1/1 fail")
		

	def test_c02(self):
		'''独立公司-修改独立调配line1退水：不影响、不等量增加'''
		rs = self.gs.case(condition="1/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_202 1/2 fail")

	def test_c03(self):
		'''独立公司-修改独立调配line1退水：影响该层级、等量增加'''
		rs = self.gs.case(condition="2/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_203 2/1 fail")

	def test_c04(self):#test------------------------------------0704其他独立调配公司和下级值更新为了与总公司相同
		'''独立公司-修改独立调配line1退水：影响该层级、不等量增加'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="2/2",normal_case=True,independent=True)
		rs = self.gs.case(condition="2/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_204 2/2 fail")

	def test_c05(self):
		'''独立公司-修改独立调配line1退水：影响组织线、等量增加'''
		self.zgs.reset_retreat_data(condition="3/1", normal_case=True, independent=True)
		rs = self.gs.case(condition="3/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_205 3/1 fail")

	def test_c06(self):
		'''独立公司-修改独立调配line1退水：影响该组织线、不等量增加'''
		self.zgs.reset_retreat_data(condition="3/2", normal_case=True, independent=True)
		rs = self.gs.case(condition="3/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_206 3/2 fail")

	def test_c07(self):#test------------------------------------0704其他独立调配公司和下级值更新为了与总公司相同
		'''独立公司-修改独立调配line1退水：影响全部层级、等量增加'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="4/1", normal_case=True, independent=True)
		rs = self.gs.case(condition="4/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_207 4/1 fail")

	def test_c08(self):
		'''独立公司-修改独立调配line1退水：影响全部层级、不等量增加'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="4/2", normal_case=True, independent=True)
		rs = self.gs.case(condition="4/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_208 4/2 fail")

	def test_c09(self):
		'''独立公司-修改独立调配line1退水：全部影响、等量增加'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="5/1", normal_case=True, independent=True)
		rs = self.gs.case(condition="5/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_209 5/1 fail")

	def test_c10(self):
		'''独立公司-修改独立调配line1退水：全部影响、不等量增加'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="5/2", normal_case=True, independent=True)
		rs = self.gs.case(condition="5/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_210 5/2 fail")

	def test_c11(self):
		'''独立公司-修改独立调配line1退水：影响该层级，等量增加，被影响人等量增加后若大于上级，修改为等于上级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="2/1", normal_case=False, independent=True)
		rs = self.gs.case(condition="2/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_211 2/1 fail")

	def test_c12(self):
		'''独立公司-修改独立调配line1退水：影响该层级，不等量增加成功，并且影响下级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="2/2", normal_case=False, independent=True)
		rs = self.gs.case(condition="2/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_212 2/2 fail")

	def test_c13(self):
		'''独立公司-修改独立调配line1退水：影响全部层级，等量增加，被影响人等量增加后若大于上级，修改为等于上级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="4/1", normal_case=False, independent=True)
		rs = self.gs.case(condition="4/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_213 4/1 fail")

	def test_c14(self):
		'''独立公司-修改独立调配line1退水：影响全部层级，不等量增加成功，并且影响下级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="4/2", normal_case=False, independent=True)
		rs = self.gs.case(condition="4/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_214 4/2 fail")

	def test_c15(self):
		'''独立公司-修改独立调配line1退水：影响全部，等量增加，被影响人等量增加后若大于上级，修改为等于上级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="5/1", normal_case=False, independent=True)
		rs = self.gs.case(condition="5/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_215 5/1 fail")

	def test_c16(self):
		'''独立公司-独立调配修改line1退水：影响全部层级，不等量增加成功，并且影响下级'''
		self.zgs.reset_independent_retreat_data(self.obj_id)
		self.zgs.reset_retreat_data(condition="5/2", normal_case=False, independent=True)
		rs = self.gs.case(condition="5/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_216 2/2 fail")



if __name__ == '__main__':
	suite = unittest.TestSuite(unittest.makeSuite(TestSystemRetreateC))
	unittest.TextTestRunner(verbosity=2).run(suite)
