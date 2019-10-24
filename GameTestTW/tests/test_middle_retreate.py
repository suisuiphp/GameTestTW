#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

import unittest
from page.Retreat import Retreat


class TestMiddleRetreat(unittest.TestCase):
	'''
	修改用户管理退水：line1、line2为非独立调配组织线，line3为独立调配组织线
	test_middle_retreate
	'''
	def setUp(self):
		# #本地测试环境
		# self.url_admin = "https://admin.game.cn-su.net"
		# self.db = "mysql,root/123456@192.168.1.10:30827/game_api_stage_tw"
		
		# 修改公司
		
		self.r = Retreat(user_type=1, id_mark="m")
		self.obj_id = self.r.ids["line1"][0]
		self.channel = 2
		self._type_equality_funcs = {}

		
	def test_d01(self):
		'''修改line1退水：不影响、等量增加'''
		flag, msg = self.r.reset_retreat_data(condition="1/1",normal_case=True,independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="1/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_001 1/1 fail")

	def test_d02(self):
		'''修改line1退水：不影响、不等量增加'''
		flag, msg = self.r.reset_retreat_data(condition="1/2",normal_case=True,independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="1/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_002 1/2 fail")

	def test_d03(self):
		'''修改line1退水：影响该层级、等量增加'''
		flag, msg = self.r.reset_retreat_data(condition="2/1",normal_case=True,independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="2/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_003 2/1 fail")

	def test_d04(self):
		'''修改line1退水：影响该层级、不等量增加'''
		flag, msg = self.r.reset_retreat_data(condition="2/2",normal_case=True,independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="2/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_004 2/2 fail")

	def test_d05(self):
		'''修改line1退水：影响组织线、等量增加'''
		flag, msg = self.r.reset_retreat_data(condition="3/1",normal_case=True,independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="3/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_005 3/1 fail")

	def test_d06(self):
		'''修改line1退水：影响该组织线、不等量增加'''
		flag, msg = self.r.reset_retreat_data(condition="3/2",normal_case=True,independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="3/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_006 3/2 fail")

	def test_d07(self):
		'''修改line1退水：影响全部层级、等量增加'''
		flag, msg = self.r.reset_retreat_data(condition="4/1",normal_case=True,independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="4/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_007 4/1 fail")

	def test_d08(self):
		'''修改line1退水：影响全部层级、不等量增加'''
		flag, msg = self.r.reset_retreat_data(condition="4/2",normal_case=True,independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="4/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_008 4/2 fail")

	def test_d09(self):
		'''修改line1退水：全部影响、等量增加'''
		flag,msg = self.r.reset_retreat_data(condition="5/1",normal_case=True,independent=False)
		# self.assertEqual(True,flag,msg)
		rs = self.r.case(condition="5/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_009 5/1 fail")

	def test_d10(self):
		'''修改line1退水：全部影响、不等量增加'''
		flag, msg = self.r.reset_retreat_data(condition="5/2",normal_case=True,independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="5/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_010 5/2 fail")

	def test_d11(self):
		'''修改line1退水：影响该层级，等量增加，被影响人等量增加后若大于上级，修改为等于上级'''
		flag, msg = self.r.reset_retreat_data(condition="2/1", normal_case=False, independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="2/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_011 2/1 fail")

	def test_d12(self):
		'''修改line1退水：影响该层级，不等量增加成功，并且影响下级'''
		flag, msg = self.r.reset_retreat_data(condition="2/2", normal_case=False, independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="2/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_012 2/2 fail")

	def test_d13(self):
		'''修改line1退水：影响全部层级，等量增加，被影响人等量增加后若大于上级，修改为等于上级'''
		flag, msg = self.r.reset_retreat_data(condition="4/1", normal_case=False, independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="4/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_013 4/1 fail")

	def test_d14(self):
		'''修改line1退水：影响全部层级，不等量增加成功，并且影响下级'''
		flag, msg = self.r.reset_retreat_data(condition="4/2", normal_case=False, independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="4/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_014 4/2 fail")

	def test_d15(self):
		'''修改line1退水：影响全部，等量增加，被影响人等量增加后若大于上级，修改为等于上级'''
		flag, msg = self.r.reset_retreat_data(condition="5/1", normal_case=False, independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="5/1", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_015 5/1 fail")

	def test_d16(self):
		'''修改line1退水：影响全部层级，不等量增加成功，并且影响下级'''
		flag, msg = self.r.reset_retreat_data(condition="5/2", normal_case=False, independent=False)
		# self.assertEqual(True, flag, msg)
		rs = self.r.case(condition="5/2", channel=self.channel, obj_id=self.obj_id)
		self.assertEqual(rs, True, "*ERROR* test_016 2/2 fail")



			
if __name__ == '__main__':
	suite = unittest.TestSuite(unittest.makeSuite(TestMiddleRetreat))
	unittest.TextTestRunner(verbosity=2).run(suite)
