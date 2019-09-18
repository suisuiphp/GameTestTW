#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

import json,time
from utils.isAssert import IsAssert
from base.user import User
from utils.public import *
from base.variables import *
import unittest
from utils.proportionExcel.opertionProportionExcel import OpertionProportionExcel

#TODO 每次执行需更新环境变量中的user_mark
#TODO 新增彩种后，需要更新代码中新增用户接口（user）、更新requestData中新增会员的接口（彩种id、占成details）

class TestProportion(IsAssert):
	@classmethod
	def setUpClass(cls):
		cls.req = User(user_type=1)
		cls.pro = OpertionProportionExcel()
	
	def create_users(self, filename, mark):
		'''
		创建用户
		:param filename: 文件名称user_info_case1.txt
		:param mark: 组织账号防重复标志p1
		:return: proxys，members
		[['zy-gs12p5', 'zy-fgs12p5', 'zy-dzj12p5', 'zy-zj12p5'], [566, 567, 568, 569]]
		[['zy566-1', 'zy567-1', 'zy568-1', 'zy569-1'], [180, 181, 182, 183]]
		'''
		# 新增组织
		proxys = self.req.create_proxy_all(
			user_mark=getAdminMark() + mark,
			file=data_dir("data/proportionData/user_info", filename))
		print(proxys)
		# proxys = [['zy-gs11p1', 'zy-fgs11p1', 'zy-dzj11p1', 'zy-zj11p1'], [544, 545, 546, 547]]
		
		# 新增会员
		members = [[], []]
		for id in proxys[1]:
			temp_members = self.req.create_members(id)
			members[0].extend(temp_members[0])
			members[1].extend(temp_members[1])
		self.assertNotNull(members[1], u"为每个组织新增会员失败")
		print(members)
		
		return proxys, members
	
	def assertProportion(self,members,case):
		'''
		对比所有会员的占成
		:param members: [['zy582-1', 'zy583-1', 'zy584-1', 'zy585-1'], [196, 197, 198, 199]]
		:param case: "case1",获取占成期望数据的关键字
		:return:
		'''
		hy = ""
		for i in range(0, len(members[1])):
			if i == 0:
				hy = "hy_gs"
			elif i == 1:
				hy = "hy_fgs"
			elif i == 2:
				hy = "hy_dzj"
			elif i == 3:
				hy = "hy_zj"
			else:
				pass
			member_id = members[1][i]
			
			# 获取会员占成
			r = self.req.get("admin_member_proportions_001", True, member_id=member_id)
			self.assertStatusCode(r, u"获取会员占成接口状态码错误%d" % r.status_code)
			self.assertNotNull(r.text, u"获取会员占成数据为空")
			self.assertHasStr(r.text, '"organization_id":1', u"获取会员占成接口未获取到总公司占成信息")
			
			actual = r.json()
			expect = self.pro.getProxyProportions(case=case, hy=hy)
			for j in range(0, len(actual)):
				proportion_expect = float(expect[j + 1])
				for k in range(0, len(actual[j]["details"])):
					proportion_actual = float(actual[j]["details"][k]["proportion_ratio"])
					self.assertEqual(proportion_expect, proportion_actual, u"线路：%s，%s占成错误" % (hy, actual[j]["level_name"]))
	
	def assertProportionConfig(self, proxys, case):
		'''
		比较组织线上每个组织的占成配置信息是否正确
		:param proxys: [['zy-gs12p1', 'zy-fgs12p1', 'zy-dzj12p1', 'zy-zj12p1'], [550, 551, 552, 553]]
		:param case: "case1",获取占成配置期望数据的关键字
		:return:
		'''
		proxy = ""
		for i in range(0, len(proxys[1])):
			if i == 0:
				proxy = "gs"
			elif i == 1:
				proxy = "fgs"
			elif i == 2:
				proxy = "dzj"
			elif i == 3:
				proxy = "zj"
			else:
				pass
			proxy_id = proxys[1][i]
			
			# 获取组织占成配置信息
			r = self.req.get(
				interface_name="admin_update_company_sources_001",
				url_change=True,
				organization_id=proxy_id)
			self.assertStatusCode(r, u"修改页面获取组织资源信息接口状态码错误%d" % r.status_code)
			self.assertHasStr(r.text, 'details', u"修改页面获取组织资源信息接口未返回占成配置'details'")
			self.assertNotNull(r.json()["details"],u"修改页面获取组织资源信息接口未返回占成配置详细信息")
			
			# 获取占成配置期望数据
			expect = self.pro.getProxyConfig(case,proxy)
			
			# 断言占成配置信息
			expect_self_highest = float(expect[0])
			expect_down_lowest = float(expect[1])
			expect_down_highest = float(expect[2])
			for j in range(0, len(r.json()["details"])):
				actual_self_highest = float(r.json()["details"][j]["self_highest_proportion"])
				actual_down_lowest = float(r.json()["details"][j]["down_lowest_proportion"])
				actual_down_highest = float(r.json()["details"][j]["down_highest_proportion"])
				
				self.assertEqual(
					expect_self_highest,
					actual_self_highest,
					u"组织：%s 上级自身占成最高错误，期望：%f,实际：%f" % (proxy,expect_self_highest,actual_self_highest))
				self.assertEqual(
					expect_down_lowest,
					actual_down_lowest,
					u"组织：%s 下级占成最低错误，期望：%f,实际：%f" % (proxy, expect_down_lowest, actual_down_lowest))
				self.assertEqual(
					expect_down_highest,
					actual_down_highest,
					u"组织：%s 下级占成最高错误，期望：%f,实际：%f" % (proxy, expect_down_highest, actual_down_highest))
	
	@unittest.skip("case6、case7、case8、case9、case10中包含了对case1的测试")
	def test_new_case1(self):
		'''proportion-new-case1'''
		proxys,members = self.create_users(filename="user_info_case1.txt",mark="p1")
		self.assertProportionConfig(proxys, "case1")
		self.assertProportion(members,"case1")
	
	def test_new_case2(self):
		'''proportion-new-case2'''
		proxys, members = self.create_users(filename="user_info_case2.txt", mark="p2")
		self.assertProportionConfig(proxys, "case2")
		self.assertProportion(members, "case2")
	
	def test_new_case3(self):
		'''proportion-new-case3'''
		proxys, members = self.create_users(filename="user_info_case3.txt", mark="p3")
		self.assertProportionConfig(proxys, "case3")
		self.assertProportion(members, "case3")
	
	def test_new_case4(self):
		'''proportion-new-case4'''
		proxys, members = self.create_users(filename="user_info_case4.txt", mark="p4")
		# proxys = [['zy-gs19p4', 'zy-fgs19p4', 'zy-dzj19p4', 'zy-zj19p4'], [826, 827, 828, 829]]
		# members = [['zy826-1', 'zy827-1', 'zy828-1', 'zy829-1'], [327, 328, 329, 330]]
		self.assertProportionConfig(proxys,"case4")
		self.assertProportion(members, "case4")
		
	
	def test_new_case5(self):
		'''proportion-new-case5'''
		proxys, members = self.create_users(filename="user_info_case5.txt", mark="p5")
		self.assertProportionConfig(proxys, "case5")
		self.assertProportion(members, "case5")
		
	@unittest.skip("case7中包含了对case6的测试")
	def test_change_case6(self):
		'''proportion-change-case6：在case1的基础上修改分公司，将公司占成改为20-立即生效'''
		proxys, members = self.create_users(filename="user_info_case1.txt", mark="p6")
		# proxys = [['zy-gs12p1', 'zy-fgs12p1', 'zy-dzj12p1', 'zy-zj12p1'], [550, 551, 552, 553]]
		# members = [['zy550-1', 'zy551-1', 'zy552-1', 'zy553-1'], [164, 165, 166, 167]]
		self.assertProportionConfig(proxys, "case1")
		self.assertProportion(members, "case1")
		
		# 修改分公司，将公司占成改为20
		proportion_details = [{"lottery_id": 6,"self_highest_proportion": 0.2,"down_lowest_proportion": 0,"down_highest_proportion": 1}]
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][1],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r,u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":false}',r.text,u"修改占成失败")
		self.assertProportion(members,"case6")
	
	def test_change_case7(self):
		'''proportion-change-case7：在case1的基础上修改分公司，将公司占成改为20,修改大总监，将分公司占成改为20-立即生效'''
		#按case1用例新增用户并断言新增占成
		proxys, members = self.create_users(filename="user_info_case1.txt", mark="p7")
		self.assertProportionConfig(proxys, "case1")
		self.assertProportion(members, "case1")
		# proxys = [['zy-gs12p1', 'zy-fgs12p1', 'zy-dzj12p1', 'zy-zj12p1'], [550, 551, 552, 553]]
		# members = [['zy550-1', 'zy551-1', 'zy552-1', 'zy553-1'], [164, 165, 166, 167]]
		
		# 修改分公司，将公司占成改为20
		proportion_details = [{"lottery_id": 6, "self_highest_proportion": 0.2, "down_lowest_proportion": 0,"down_highest_proportion": 1}]
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][1],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r, u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":false}', r.text, u"修改占成失败")
		self.assertProportion(members, "case6")
		
		# 修改大总监，将分公司占成改为20
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][2],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r, u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":false}', r.text, u"修改占成失败")
		self.assertProportion(members, "case7")
	
	@unittest.skip("case9、case10中包含了对case8的测试")
	def test_change_case8(self):
		'''proportion-change-case8：在case1的基础上修改公司，将下级最高改为90-立即生效'''
		#按case1用例新增用户并断言新增占成
		proxys, members = self.create_users(filename="user_info_case1.txt", mark="p8")
		self.assertProportionConfig(proxys, "case1")
		self.assertProportion(members, "case1")
		# proxys = [['zy-gs13p1', 'zy-fgs13p1', 'zy-dzj13p1', 'zy-zj13p1'], [570, 571, 572, 573]]
		# members = [['zy570-1', 'zy571-1', 'zy572-1', 'zy573-1'], [184, 185, 186, 187]]
		
		# 修改公司，将下级最高改为90
		proportion_details = [{"lottery_id": 6, "self_highest_proportion": 1, "down_lowest_proportion": 0,"down_highest_proportion": 0.9}]
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][0],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r, u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":false}', r.text, u"修改占成失败")
		
		# 断言修改后的实际占成和配置信息
		self.assertProportion(members, "case8")
		self.assertProportionConfig(proxys,"case8")
	
	@unittest.skip("case10中包含了对case8、case9的测试")
	def test_change_case9(self):
		'''proportion-change-case9：在case1、case8的基础上修改公司，将下级最高改为40-立即生效'''
		# 按case1用例新增用户并断言新增占成
		proxys, members = self.create_users(filename="user_info_case1.txt", mark="p9")
		self.assertProportionConfig(proxys, "case1")
		self.assertProportion(members, "case1")
		# proxys = [['zy-gs13p1', 'zy-fgs13p1', 'zy-dzj13p1', 'zy-zj13p1'], [570, 571, 572, 573]]
		# members = [['zy570-1', 'zy571-1', 'zy572-1', 'zy573-1'], [184, 185, 186, 187]]
		
		# 修改公司，将下级最高改为90
		proportion_details = [{"lottery_id": 6, "self_highest_proportion": 1, "down_lowest_proportion": 0, "down_highest_proportion": 0.9}]
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][0],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r, u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":false}', r.text, u"修改占成失败")

		# 断言修改后的实际占成和配置信息case8
		self.assertProportion(members, "case8")
		self.assertProportionConfig(proxys, "case8")
		
		# 修改公司，将下级最高改为40-case9
		proportion_details = [{"lottery_id": 6, "self_highest_proportion": 1, "down_lowest_proportion": 0,"down_highest_proportion": 0.4}]
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][0],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r, u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":false}', r.text, u"修改占成失败")

		# 断言修改后的实际占成和配置信息
		self.assertProportion(members, "case9")
		self.assertProportionConfig(proxys, "case9")
	
	def test_change_case10(self):
		'''proportion-change-case9：在case1、case8、casse9基础上，修改公司，将下级最低改为50，最高改为60-立即生效'''
		# 按case1用例新增用户并断言新增占成
		proxys, members = self.create_users(filename="user_info_case1.txt", mark="p10")
		self.assertProportionConfig(proxys, "case1")
		self.assertProportion(members, "case1")
		# proxys = [['zy-gs13p1', 'zy-fgs13p1', 'zy-dzj13p1', 'zy-zj13p1'], [570, 571, 572, 573]]
		# members = [['zy570-1', 'zy571-1', 'zy572-1', 'zy573-1'], [184, 185, 186, 187]]
		
		# 修改公司，将下级最高改为90-case8
		proportion_details = [{"lottery_id": 6, "self_highest_proportion": 1, "down_lowest_proportion": 0,"down_highest_proportion": 0.9}]
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][0],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r, u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":false}', r.text, u"修改占成失败")

		# 断言修改后的实际占成和配置信息
		self.assertProportion(members, "case8")
		self.assertProportionConfig(proxys, "case8")
		
		# 修改公司，将下级最高改为40-case9
		proportion_details = [{"lottery_id": 6, "self_highest_proportion": 1, "down_lowest_proportion": 0,
		                       "down_highest_proportion": 0.4}]
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][0],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r, u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":false}', r.text, u"修改占成失败")

		# 断言修改后的实际占成和配置信息
		self.assertProportion(members, "case9")
		self.assertProportionConfig(proxys, "case9")
		
		# 修改公司，将下级最低改为50，最高改为60-case10
		proportion_details = [{"lottery_id": 6, "self_highest_proportion": 1, "down_lowest_proportion": 0.5, "down_highest_proportion": 0.6}]
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][0],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r, u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":false}', r.text, u"修改占成失败")
		
		# 断言修改后的实际占成和配置信息
		self.assertProportion(members, "case10")
		self.assertProportionConfig(proxys, "case10")
	
	def test_change_case11(self):
		'''proportion-change-case8：在case1的基础上修改公司，将下级最高改为90-延迟生效'''
		print("------------------按case1用例新增用户-----------------------------")
		proxys, members = self.create_users(filename="user_info_case1.txt", mark="p11")
		self.assertProportionConfig(proxys, "case1")
		self.assertProportion(members, "case1")
		# proxys = [['zy-gs16p11', 'zy-fgs16p11', 'zy-dzj16p11', 'zy-zj16p11'], [631, 632, 633, 634]]
		# members = [['zy631-1', 'zy632-1', 'zy633-1', 'zy634-1'], [238, 239, 240, 241]]

		print("------------------总监会员登录并修改密码-----------------------------")
		hy = User(user_type=2,username=members[0][-1],password="6yhn6tfc")

		print("------------------总监会员下注极速赛车-冠军大-----------------------------")
		flag, msg = hy.bet()
		self.assertEqual(True, flag, msg)

		print("-----------------case8-修改公司，将下级最高改为90-----------------------------")
		proportion_details = [{"lottery_id": 6, "self_highest_proportion": 1, "down_lowest_proportion": 0,
		                       "down_highest_proportion": 0.9}]
		r = self.req.post(
			interface_name="admin_update_proportion_001",
			data_change=True,
			organization_id=proxys[1][0],
			proportion_details=proportion_details,
			proportion_mode=1)
		self.assertStatusCode(r, u"修改占成接口请求状态码错误%d" % r.status_code)
		self.assertEqual('{"is_next_valid":true}', r.text, u"修改占成失败")

		print("-----------------断言修改配置后的实际占成（不变）和配置信息（变化）-----------------------------")
		self.assertProportion(members, "case1")
		self.assertProportionConfig(proxys, "case8")

		# 触发配置占成生效
		print("-----------------触发配置占成生效，断言修改后大占成是否正确-----------------------------")
		self.req.get("admin_cal_proportion_001")
		time.sleep(2)
		self.assertProportion(members, "case8")
		self.assertProportionConfig(proxys, "case8")
		

if __name__ == '__main__':
	suite = unittest.TestSuite(unittest.makeSuite(TestProportion))
	unittest.TextTestRunner(verbosity=2).run(suite)