#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

import json, time
from utils.isAssert import IsAssert
from base.user import User
from utils.public import *
import unittest


# TODO: 修改环境变量base/variables,组织mark等

class TestAdmin(IsAssert):
	@classmethod
	def setUpClass(cls):
		cls.req = User(user_type=1)
	
	@unittest.skip("test_admin_password_001:新增用户修改密码已验证新增用户功能")
	def test_new_new_company_001(self):
		'''新增完整组织线，并给每个组织创建会员'''
		proxys = self.req.create_proxy_all()
		print(proxys)

		#为每个组织新增一个会员
		members = [[], []]
		for id in proxys[1]:
			temp_members = self.req.create_members(id)
			members[0].extend(temp_members[0])
			members[1].extend(temp_members[1])
		self.assertNotNull(members[1], u"为每个组织新增会员失败")
		print(members)
		#
		# proxys = [
		# 	['zy-gs15', 'zy-fgs15', 'zy-dzj15', 'zy-zj15', 'zy-dgd15', 'zy-gd15', 'zy-zdl15', 'zy-yjdl15', 'zy-ejdl15',
		# 	 'zy-sjdl15'], [610, 611, 612, 613, 614, 615, 616, 617, 618, 619]]
		# members = [['zy610-1', 'zy611-1', 'zy612-1', 'zy613-1', 'zy614-1', 'zy615-1', 'zy616-1', 'zy617-1', 'zy618-1',
		#             'zy619-1'], [218, 219, 220, 221, 222, 223, 224, 225, 226, 227]]
		# proxys = [['zy-gs16', 'zy-fgs16', 'zy-dzj16', 'zy-zj16', 'zy-dgd16', 'zy-gd16', 'zy-zdl16', 'zy-yjdl16', 'zy-ejdl16', 'zy-sjdl16'], [620, 621, 622, 623, 624, 625, 626, 627, 628, 629]]
		# members = [['zy620-1', 'zy621-1', 'zy622-1', 'zy623-1', 'zy624-1', 'zy625-1', 'zy626-1', 'zy627-1', 'zy628-1', 'zy629-1'], [228, 229, 230, 231, 232, 233, 234, 235, 236, 237]]

		#修改密码
		for i in range(0, len(proxys[1])):
			User(user_type=1, username=proxys[0][i], password="6tfc6yhn")
		
		# for j in range(0, len(members[1])):
		# 	User(user_type=2, username=members[0][j], password="6tfc6yhn")
			
	# 新增用户修改密码
	def test_admin_password_001(self):
		'''新增用户修改密码'''
		#新增组织线
		proxys = self.req.create_proxy_all()
		print(proxys)
		
		# 为每个组织新增一个会员
		members = [[], []]
		for id in proxys[1]:
			temp_members = self.req.create_members(id)
			members[0].extend(temp_members[0])
			members[1].extend(temp_members[1])
		self.assertNotNull(members[1], u"为每个组织新增会员失败")
		print(members)
		
		# 修改密码
		for i in range(0, len(proxys[1])):
			User(user_type=1, username=proxys[0][i], password="6tfc6yhn")
		
		for j in range(0, len(members[1])):
			User(user_type=2, username=members[0][j], password="6tfc6yhn")
		
	# ******************测试当前期数获取***********************************************************************************
	@unittest.skip("test_period_number_001:测试是否掉奖-极速赛车已经包含")
	def test_period_infos_001(self):
		'''测试当前期数获取-极速赛车'''
		r = self.req.get("member_period_infos_001")
		self.assertStatusCode(r, u"当前期数获取接口状态码错误%d" % r.status_code)
		self.assertHasStr(r.text, "current_period_number", u"当前期数接口结果未包含current_period_number")
		self.assertNotNull(r.json()["current_period_number"], u"当前期数获取失败")
	
	@unittest.skip("test_period_number_002:测试是否掉奖-幸运飞艇已经包含")
	def test_period_infos_002(self):
		'''测试当前期数获取-幸运飞艇'''
		r = self.req.get(interface_name="member_period_infos_001", url_change=True, lottery_id=2)
		self.assertStatusCode(r, u"当前期数获取接口状态码错误%d" % r.status_code)
		self.assertHasStr(r.text, "current_period_number", u"当前期数接口结果未包含current_period_number")
		self.assertNotNull(r.json()["current_period_number"], u"当前期数获取失败")
	
	# ******************测试上期开奖**************************************************************************************
	@unittest.skip("test_period_number_001:测试是否掉奖-极速赛车已经包含")
	def test_recently_number_001(self):
		'''测试上期开奖获取-极速赛车'''
		r = self.req.get("member_recently_number_001")
		self.assertStatusCode(r, u"上期开奖接口状态码错误%d" % r.status_code)
		self.assertHasStr(r.text, "before_period_number", u"上期开奖接口结果未包含before_period_number")
		self.assertNotNull(r.json()["before_period_number"], u"上期开奖期数为空")
		self.assertNotNull(r.json()["before_lottery_numbers"], u"上期开奖号码为空")
	
	@unittest.skip("test_period_number_002:测试是否掉奖-幸运飞艇已经包含")
	def test_recently_number_002(self):
		'''测试上期开奖获取-幸运飞艇'''
		r = self.req.get(interface_name="member_recently_number_001", url_change=True, lottery_id=2)
		self.assertStatusCode(r, u"上期开奖接口状态码错误%d" % r.status_code)
		self.assertHasStr(r.text, "before_period_number", u"上期开奖接口结果未包含before_period_number")
		self.assertNotNull(r.json()["before_period_number"], u"上期开奖期数为空")
		self.assertNotNull(r.json()["before_lottery_numbers"], u"上期开奖号码为空")
	
	# ******************测试是否掉奖********************************************************************************
	def test_period_number_001(self):
		'''测试是否掉奖-极速赛车'''
		r_before = self.req.get("member_recently_number_001")  # 上期开奖
		self.assertStatusCode(r_before, u"上期开奖接口状态码错误%d" % r_before.status_code)
		self.assertHasStr(r_before.text, "before_period_number", u"上期开奖接口结果未包含before_period_number")
		self.assertNotNull(r_before.json()["before_period_number"], u"上期开奖期数为空")
		self.assertNotNull(r_before.json()["before_lottery_numbers"], u"上期开奖号码为空")
		
		r_current = self.req.get("member_period_infos_001")  # 当前期数
		self.assertStatusCode(r_current, u"当前期数获取接口状态码错误%d" % r_current.status_code)
		self.assertHasStr(r_current.text, "current_period_number", u"当前期数接口结果未包含current_period_number")
		self.assertNotNull(r_current.json()["current_period_number"], u"当前期数获取失败")
		
		flag = True
		interval = int(r_current.json()["current_period_number"]) - int(r_before.json()["before_period_number"])
		if interval > 2:
			flag = False
		self.assertEqual(True, flag, u"开奖延迟{0}期".format(interval - 1))
	
	def test_period_number_002(self):
		'''测试是否掉奖-幸运飞艇'''
		r_before = self.req.get(interface_name="member_recently_number_001", url_change=True, lottery_id=2)  # 上期开奖
		self.assertStatusCode(r_before, u"上期开奖接口状态码错误%d" % r_before.status_code)
		self.assertHasStr(r_before.text, "before_period_number", u"上期开奖接口结果未包含before_period_number")
		self.assertNotNull(r_before.json()["before_period_number"], u"上期开奖期数为空")
		self.assertNotNull(r_before.json()["before_lottery_numbers"], u"上期开奖号码为空")
		
		r_current = self.req.get(interface_name="member_period_infos_001", url_change=True, lottery_id=2)  # 当前期数
		self.assertStatusCode(r_current, u"当前期数获取接口状态码错误%d" % r_current.status_code)
		self.assertHasStr(r_current.text, "current_period_number", u"当前期数接口结果未包含current_period_number")
		self.assertNotNull(r_current.json()["current_period_number"], u"当前期数获取失败")
		
		flag = True
		interval = int(r_current.json()["current_period_number"]) - int(r_before.json()["before_period_number"])
		if interval > 2:
			flag = False
		self.assertEqual(True, flag, u"开奖延迟{0}期".format(interval - 1))
		
	# 历史开奖 - 极速赛车
	def test_lottery_infos_001(self):
		'''历史开奖-极速赛车'''
		r = self.req.get(interface_name="member_lottery_infos_001", url_change=True, created_at=getDate())
		print(r.text)
		self.assertStatusCode(r, u"历史开奖接口状态码错误%d" % r.status_code)
		self.assertHasStr(r.text, "results", u"历史开奖接口未返回结果results")
		self.assertNotNull(r.json()["results"], u"历史开奖返回开奖结果为空")
		self.assertNotNull(r.json()["results"][0]["lottery_numbers"], u"历史开奖返回开奖结果号码为空")
		self.assertNotNull(r.json()["results"][0]["details"][0]["lottery_result"], u"冠亚军和或者1~5龙虎为空")
		self.assertNotNull(r.json()["results"][0]["details"][1]["lottery_result"], u"冠亚军和或者1~5龙虎为空")
		
	# TODO：获取即时赔率，断言玩法个数，赔率有值
		
if __name__ == '__main__':
	suite = unittest.TestSuite(unittest.makeSuite(TestAdmin))
	unittest.TextTestRunner(verbosity=2).run(suite)