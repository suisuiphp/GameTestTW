#!/usr/bin/env python
# coding:utf-8

# Author:TiFity


import json, time
from utils.isAssert import IsAssert
from base.user import User
from utils.public import *
import unittest


class TestMember(IsAssert):
	@classmethod
	def setUpClass(cls):
		cls.req = User(user_type=2)
	
	# ******************测试当前期数获取*****************************************************************************
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
	
	# ******************测试上期开奖********************************************************************************
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
		r_before = self.req.get("member_recently_number_001") #上期开奖
		self.assertStatusCode(r_before, u"上期开奖接口状态码错误%d" % r_before.status_code)
		self.assertHasStr(r_before.text, "before_period_number", u"上期开奖接口结果未包含before_period_number")
		self.assertNotNull(r_before.json()["before_period_number"], u"上期开奖期数为空")
		self.assertNotNull(r_before.json()["before_lottery_numbers"], u"上期开奖号码为空")
		
		r_current = self.req.get("member_period_infos_001") #当前期数
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
	
	# ******************获取即时赔率********************************************************************************
	def test_execution_odds_001(self):
		'''获取即时赔率-极速赛车'''
		r = self.req.get("member_execution_odds_001")
		self.assertStatusCode(r, u"获取即时赔率接口状态码错误%d" % r.status_code)
		
		odds = json.loads(r.content)
		self.assertEqual(171, len(odds))  # 极速赛车的玩法个数
		
		msg = ""
		for i in range(0, len(odds)):
			flag = True
			self.assertNotNull(odds[i]["execution_odds"])
			if float(odds[i]["execution_odds"]) < 1:
				flag = False
				msg = "game_id:{0}即时赔率错误,execution_odds：{1}".format(odds[i]["game_id"], odds[i]["execution_odds"])
			self.assertEqual(True, flag, msg.decode("utf-8"))
	
	def test_execution_odds_002(self):
		'''获取即时赔率-幸运飞艇'''
		r = self.req.get(interface_name="member_execution_odds_001", url_change=True, lottery_id=2)
		self.assertStatusCode(r, u"获取即时赔率接口状态码错误%d" % r.status_code)
		
		odds = json.loads(r.content)
		self.assertEqual(171, len(odds))  # 幸运飞艇的玩法个数
		
		msg = ""
		for i in range(0, len(odds)):
			flag = True
			self.assertNotNull(odds[i]["execution_odds"])
			if float(odds[i]["execution_odds"]) < 1:
				flag = False
				msg = "game_id:{0}即时赔率错误,execution_odds：{1}".format(odds[i]["game_id"], odds[i]["execution_odds"])
			self.assertEqual(True, flag, msg.decode("utf-8"))
	
	# ******************获取账户信息：账户、盘口、信用额度、可用余额等***************************************************
	def test_personal_info_001(self):
		'''获取账户信息：账户、盘口、信用额度、可用余额等'''
		r = self.req.get("member_personal_info_001")
		self.assertStatusCode(r, u"获取账户信息接口状态码错误%d" % r.status_code)
		self.assertEqual(self.req.account, r.json()["account"], u"获取账户信息，账号错误")
		self.assertNotNull(r.json()["name"], u"获取账户信息-未获取到用户名称")
		self.assertNotNull(r.json()["handicap_name"], u"获取账户信息-未获取到盘口")
	
	# ******************下注**************************************************************************************
	@unittest.skip("test_current_orders_001最新订单会测试到下注")
	def test_bet_001(self):
		'''下注-冠军大-极速赛车'''
		flag,msg=self.req.bet(interface="member_bet_001",lottery_id=6)
		self.assertEqual(True,flag,msg)
	
	def test_bet_002(self):
		'''批量下注-两面盘-极速赛车'''
		flag, msg = self.req.bet(interface="member_bet_002", lottery_id=6)
		self.assertEqual(True, flag, msg)
	
	@unittest.skip("test_current_orders_002最新订单会测试到下注")
	def test_bet_003(self):
		'''下注-冠军大-幸运飞艇'''
		flag, msg = self.req.bet(interface="member_bet_003", lottery_id=2)
		self.assertEqual(True, flag, msg)
		
	def test_bet_004(self):
		'''批量下注-两面盘-幸运飞艇'''
		flag, msg = self.req.bet(interface="member_bet_004", lottery_id=2)
		self.assertEqual(True, flag, msg)
	
	# ******************最新订单***********************************************************************************
	def test_current_orders_001(self):
		'''最新订单-极速赛车'''
		
		'''下注-冠军大-极速赛车'''
		flag, msg = self.req.bet()
		self.assertEqual(True, flag, msg)
		
		# 获取当前期数号码
		r = self.req.get("member_period_infos_001")
		self.assertStatusCode(r, u"当前期数获取接口状态码错误%d" % r.status_code)
		self.assertHasStr(r.text, "current_period_number", u"当前期数接口结果未包含current_period_number")
		self.assertNotNull(r.json()["current_period_number"], u"当前期数获取失败")
		current_period_number = r.json()["current_period_number"]
		
		# 获取最新订单
		r = self.req.get("member_orders_001")
		self.assertEqual(current_period_number, r.json()["period_number"], u"期数不一致")
		mark = False
		if r.json()["bet_count"] > 0:
			mark = True
		self.assertEqual(True, mark, "获取{0}条订单".format(r.json()["bet_count"]))
	
	def test_current_orders_002(self):
		'''最新订单-幸运飞艇'''
		flag, msg = self.req.bet(interface="member_bet_003", lottery_id=2)
		self.assertEqual(True, flag, msg)
		
		# 获取当前期数号码
		r = self.req.get(interface_name="member_period_infos_001", url_change=True, lottery_id=2)
		self.assertStatusCode(r, u"当前期数获取接口状态码错误%d" % r.status_code)
		self.assertHasStr(r.text, "current_period_number", u"当前期数接口结果未包含current_period_number")
		self.assertNotNull(r.json()["current_period_number"], u"当前期数获取失败")
		current_period_number = r.json()["current_period_number"]
		
		# 获取最新订单
		r = self.req.get(interface_name="member_orders_001", url_change=True, lottery_id=2)
		self.assertEqual(current_period_number, r.json()["period_number"], u"期数不一致")
		mark = False
		if r.json()["bet_count"] > 0:
			mark = True
		self.assertEqual(True, mark, u"获取{0}条订单".format(r.json()["bet_count"]))
	
	# ******************两面长龙***********************************************************************************
	def test_statistic_infos_001(self):
		"两面长龙-极速赛车"
		r = self.req.get("member_statistic_infos_001")
		self.assertStatusCode(r, u"两面长龙接口状态码错误%d" % r.status_code)
		self.assertHasStr(r.text, "single_lottery_statistic_details")
		mark = False
		if len(r.json()["side_lottery_statistic_details"]) > 0 \
				and r.json()["side_lottery_statistic_details"][0]["continuous_period_count"] >= 2:
			mark = True
		self.assertEqual(True, mark, u"两面长龙数据获取失败或错误")
		
	def test_statistic_infos_002(self):
		"两面长龙-幸运飞艇"
		r = self.req.get(interface_name="member_statistic_infos_001",url_change=True, lottery_id=2)
		self.assertStatusCode(r, u"两面长龙接口状态码错误%d" % r.status_code)
		self.assertHasStr(r.text, "single_lottery_statistic_details")
		mark = False
		if len(r.json()["side_lottery_statistic_details"]) > 0 \
				and r.json()["side_lottery_statistic_details"][0]["continuous_period_count"] >= 2:
			mark = True
		self.assertEqual(True, mark, u"两面长龙数据获取失败或错误")
	
	# ******************冠亚和历史***********************************************************************************
	def test_show_group_history_001(self):
		'''冠亚和历史-极速赛车'''
		r = self.req.get("member_show_group_history_001")
		self.assertStatusCode(r, u"冠亚和历史-极速赛车状态码错误%d" % r.status_code)
		self.assertHasStr(r.content, r"冠、亚军和")
		self.assertHasStr(r.content, r"冠、亚军和大小")
		self.assertHasStr(r.content, r"冠、亚军和单双")
		mark = True
		for record in r.json():
			if record["name"] == u"冠、亚军和":
				if len(record["details"]) == 0:
					mark = False
			if record["name"] == u"冠、亚军和大小":
				self.assertHasStr(record["details"], u"大", u"冠亚军和历史中没有字符串'大'")
				self.assertHasStr(record["details"], u"小", u"冠亚军和历史中没有字符串'小'")
			if record["name"] == u"冠、亚军和单双":
				self.assertHasStr(record["details"], u"单", u"冠亚军和历史中没有字符串'单'")
				self.assertHasStr(record["details"], u"双", u"冠亚军和历史中没有字符串'双'")
		self.assertEqual(True, mark, u"冠亚和历史数据为空或者不正确")
		
	def test_show_group_history_002(self):
		'''冠亚和历史-幸运飞艇'''
		r = self.req.get(interface_name="member_show_group_history_001", url_change=True, lottery_id=2)
		self.assertStatusCode(r, u"冠亚和历史-极速赛车状态码错误%d" % r.status_code)
		self.assertHasStr(r.content, r"冠、亚军和")
		self.assertHasStr(r.content, r"冠、亚军和大小")
		self.assertHasStr(r.content, r"冠、亚军和单双")
		mark = True
		for record in r.json():
			if record["name"] == u"冠、亚军和":
				if len(record["details"]) == 0:
					mark = False
			if record["name"] == u"冠、亚军和大小":
				self.assertHasStr(record["details"], u"大", u"冠亚军和历史中没有字符串'大'")
				self.assertHasStr(record["details"], u"小", u"冠亚军和历史中没有字符串'小'")
			if record["name"] == u"冠、亚军和单双":
				self.assertHasStr(record["details"], u"单", u"冠亚军和历史中没有字符串'单'")
				self.assertHasStr(record["details"], u"双", u"冠亚军和历史中没有字符串'双'")
		self.assertEqual(True, mark, u"冠亚和历史数据为空或者不正确")
	
	# ******************今日已结*************************************************************************************
	def test_settled_today_001(self):
		'''今日已结'''
		r = self.req.get("member_settled_today_001")
		self.assertStatusCode(r, u"今日已结获取接口状态码错误%d" % r.status_code)
	
	# ******************未结明细*************************************************************************************
	def test_no_settle_001(self):
		'''未结明细'''
		r = self.req.get("member_no_settle_001")
		self.assertStatusCode(r, u"未结明细获取接口状态码错误%d" % r.status_code)
	
	# ******************两周报表-全部*************************************************************************************
	def test_reports_001(self):
		'''两周报表-全部'''
		r = self.req.get("member_reports_001")
		self.assertStatusCode(r, u"两周报表-全部获取接口状态码错误%d" % r.status_code)
	
	def test_reports_002(self):
		'''两周报表-极速赛车'''
		r = self.req.get(interface_name="member_reports_001", url_change=True, lottery_id=6)
		self.assertStatusCode(r, u"两周报表-获取接口状态码错误%d" % r.status_code)
	
	# ******************报表注单明细-全部**********************************************************************************
	def test_reports_retreating_001(self):
		'''报表注单明细-全部'''
		r = self.req.get(interface_name="member_reports_retreating_001", url_change=True, lottery_id=None,
		                 date=getDate())
		self.assertStatusCode(r, u"报表注单明细-全部接口状态码错误%d" % r.status_code)
	
	def test_reports_retreating_002(self):
		'''报表注单明细-极速赛车'''
		r = self.req.get(interface_name="member_reports_retreating_001", url_change=True, lottery_id=6, date=getDate())
		self.assertStatusCode(r, u"报表注单明细接口状态码错误%d" % r.status_code)
	
	# ******************历史总帐*****************************************************************************************
	def test_history_001(self):
		'''历史总帐'''
		r = self.req.get(interface_name="member_history_001", url_change=True, start_time=getDate(), end_time=getDate())
		self.assertStatusCode(r, u"历史总帐接口状态码错误%d" % r.status_code)
	
	# ******************历史开奖*****************************************************************************************
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


	# ******************自动下单-新增方案
	



if __name__ == '__main__':
	suite = unittest.TestSuite(unittest.makeSuite(TestMember))
	unittest.TextTestRunner(verbosity=2).run(suite)
