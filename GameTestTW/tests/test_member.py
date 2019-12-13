#!/usr/bin/env python
# coding:utf-8

# Author:TiFity


import json, time
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.isAssert import IsAssert
from base.user import User
from utils.public import *
import unittest
from base.variables import *
import ddt


@ddt.ddt
class TestMember(IsAssert):
	@classmethod
	def setUpClass(cls):
		cls.req = User(user_type=2)
	
	def msg_decode(self, msg):
		return msg.decode("utf-8")
	#
	# # ******************测试当前期数获取***********************************************************************************
	# # @unittest.skip("test_period_number_001 测试是否掉奖包含当前期数")
	# @ddt.data(*LOTTERIES.keys())
	# def test_period_infos_001(self, lottery_id):
	# 	'''获取当前期数'''
	# 	r = self.req.get(interface_name="member_period_infos_001", url_change=True, lottery_id=lottery_id)
	# 	self.assertStatusCode(r, self.msg_decode(LOTTERIES[lottery_id] + ":状态码错误"))
	# 	self.assertNotEqual(str({}), r.content, self.msg_decode(LOTTERIES[lottery_id] + ":接口返回结果为空"))
	# 	self.assertNotEqual(0, len(r.json()["current_period_number"]), self.msg_decode(LOTTERIES[lottery_id] + ":获取当前期数失败"))
	
	# def test_period_infos_001(self):
	# 	'''获取当前期数'''
	# 	lottery_id = 5
	# 	r = self.req.get(interface_name="member_period_infos_001", url_change=True, lottery_id=lottery_id)
	# 	self.assertStatusCode(r, self.msg_decode(LOTTERIES[lottery_id] + ":状态码错误"))
	# 	self.assertNotEqual(str({}), r.content, self.msg_decode(LOTTERIES[lottery_id] + ":接口返回结果为空"))
	# 	self.assertNotEqual(0, len(r.json()["current_period_number"]), self.msg_decode(LOTTERIES[lottery_id] + ":获取当前期数失败"))

	# # ******************测试上期开奖**************************************************************************************
	# @unittest.skip("test_period_number_001 测试是否掉奖包含上期开奖")
	# @ddt.data(*LOTTERIES.keys())
	# def test_recently_number_001(self, lottery_id):
	# 	'''获取上期开奖号码'''
	# 	r = self.req.get(interface_name="member_recently_number_001", url_change=True, lottery_id=lottery_id)
	# 	self.assertStatusCode(r, self.msg_decode(LOTTERIES[lottery_id] + ":状态码错误"))
	# 	self.assertNotEqual(0, len(r.json()["before_period_number"]), self.msg_decode(LOTTERIES[lottery_id] + ":上期开奖期数为空"))
	# 	self.assertNotEqual(0, len(r.json()["before_lottery_numbers"]), self.msg_decode(LOTTERIES[lottery_id] + ":上期开奖号码为空"))

	# ******************测试是否掉奖********************************************************************************
	# @unittest.skip("skip test")
	@ddt.data(*LOTTERIES.keys())
	def test_period_number_001(self, lottery_id):
		'''测试是否掉奖-极速赛车'''
		# 获取上期开奖
		r_before = self.req.get(interface_name="member_recently_number_001", url_change=True, lottery_id=lottery_id)
		self.assertStatusCode(r_before, self.msg_decode(LOTTERIES[lottery_id] + ":状态码错误"))

		# 当前期数
		r_current = self.req.get(interface_name="member_period_infos_001", url_change=True, lottery_id=lottery_id)
		self.assertStatusCode(r_current, self.msg_decode(LOTTERIES[lottery_id] + ":状态码错误"))

		flag = True
		interval = int(r_current.json()["current_period_number"]) - int(r_before.json()["before_period_number"])
		if interval > 2:
			flag = False
		self.assertEqual(True, flag, u"开奖延迟{0}期".format(interval - 1))
		self.assertTrue(flag, self.msg_decode(LOTTERIES[lottery_id]+"开奖延迟{0}期".format(interval - 1)))

	# # ******************获取即时赔率********************************************************************************
	# @unittest.skip("skip test")
	# @ddt.data([JSSC, 171], [XYFT, 171], [JSSSC, 92], [JSFT, 171], [BJSC, 171], [CQHLSS, 92])
	# @ddt.unpack
	# def test_execution_odds_002(self,lottery_id,numbers):
	# 	'''获取即时赔率'''
	# 	r = self.req.get(interface_name="member_execution_odds_001", url_change=True, lottery_id=lottery_id)
	# 	self.assertStatusCode(r, self.msg_decode(LOTTERIES[lottery_id] + ":状态码错误"))
	#
	# 	odds = json.loads(r.content)
	# 	self.assertEqual(numbers, len(odds), self.msg_decode(LOTTERIES[lottery_id] + ":玩法个数错误"))  # 玩法个数
	#
	# 	msg = ""
	# 	for i in range(0, len(odds)):
	# 		flag = True
	# 		if float(odds[i]["execution_odds"]) < 1:
	# 			flag = False
	# 			msg = "game_id:{0}即时赔率错误,execution_odds：{1}".format(odds[i]["game_id"], odds[i]["execution_odds"])
	# 		self.assertTrue(flag,self.msg_decode(LOTTERIES[lottery_id]+msg))
	#
	# # ******************获取账户信息：账户、盘口、信用额度、可用余额等***************************************************
	# @unittest.skip("skip test")
	# def test_personal_info_001(self):
	# 	'''获取账户信息：账户、盘口、信用额度、可用余额等'''
	# 	r = self.req.get("member_personal_info_001")
	# 	self.assertStatusCode(r, u"获取账户信息接口状态码错误%d" % r.status_code)
	# 	self.assertEqual(self.req.account, r.json()["account"], u"账号错误")
	# 	self.assertNotEqual(0, len(r.json()["name"]), u"未获取到用户名称" )
	# 	self.assertNotEqual(0, len(r.json()["handicap_name"]), u"未获取到所属盘口")
	# #
	# # ******************下注**************************************************************************************
	# @unittest.skip("test_current_orders_001最新订单会测试到下注")
	# def test_bet_001(self):
	# 	'''下注-冠军大-极速赛车'''
	# 	flag, msg = self.req.bet(interface="member_bet_001", lottery_id=6)
	# 	self.assertTrue(flag, msg)
	#
	# def test_bet_002(self):
	# 	'''批量下注-两面盘-极速赛车'''
	# 	flag, msg = self.req.bet(interface="member_bet_002", lottery_id=6)
	# 	self.assertTrue(flag, msg)
	#
	# # @unittest.skip("test_current_orders_002最新订单会测试到下注")
	# def test_bet_003(self):
	# 	'''下注-冠军大-幸运飞艇'''
	# 	flag, msg = self.req.bet(interface="member_bet_003", lottery_id=2)
	# 	self.assertTrue(flag, msg)
	#
	# def test_bet_004(self):
	# 	'''批量下注-两面盘-幸运飞艇'''
	# 	flag, msg = self.req.bet(interface="member_bet_004", lottery_id=2)
	# 	self.assertTrue(flag, msg)
	#
	# # ******************最新订单***********************************************************************************
	# def test_current_orders_001(self):
	# 	'''最新订单-极速赛车'''
	#
	# 	'''下注-冠军大-极速赛车'''
	# 	flag, msg = self.req.bet()
	# 	self.assertTrue(flag, msg)
	#
	# 	# 获取当前期数号码
	# 	r = self.req.get("member_period_infos_001")
	# 	self.assertStatusCode(r, u"当前期数获取接口状态码错误%d" % r.status_code)
	# 	self.assertHasStr(r.text, "current_period_number", u"当前期数接口结果未包含current_period_number")
	# 	self.assertNotNull(r.json()["current_period_number"], u"当前期数获取失败")
	# 	current_period_number = r.json()["current_period_number"]
	#
	# 	# 获取最新订单
	# 	r = self.req.get("member_orders_001")
	# 	self.assertEqual(current_period_number, r.json()["period_number"], u"期数不一致")
	# 	mark = False
	# 	if r.json()["bet_count"] > 0:
	# 		mark = True
	# 	self.assertEqual(True, mark, "获取{0}条订单".format(r.json()["bet_count"]))
	#
	# def test_current_orders_002(self):
	# 	'''最新订单-幸运飞艇'''
	# 	flag, msg = self.req.bet(interface="member_bet_003", lottery_id=2)
	# 	self.assertTrue(flag, msg)
	#
	# 	# 获取当前期数号码
	# 	r = self.req.get(interface_name="member_period_infos_001", url_change=True, lottery_id=2)
	# 	self.assertStatusCode(r, u"当前期数获取接口状态码错误%d" % r.status_code)
	# 	self.assertHasStr(r.text, "current_period_number", u"当前期数接口结果未包含current_period_number")
	# 	self.assertNotNull(r.json()["current_period_number"], u"当前期数获取失败")
	# 	current_period_number = r.json()["current_period_number"]
	#
	# 	# 获取最新订单
	# 	r = self.req.get(interface_name="member_orders_001", url_change=True, lottery_id=2)
	# 	self.assertEqual(current_period_number, r.json()["period_number"], u"期数不一致")
	# 	mark = False
	# 	if r.json()["bet_count"] > 0:
	# 		mark = True
	# 	self.assertEqual(True, mark, u"获取{0}条订单".format(r.json()["bet_count"]))
	#
	# # ******************两面长龙***********************************************************************************
	# def test_statistic_infos_001(self):
	# 	"两面长龙-极速赛车"
	# 	r = self.req.get("member_statistic_infos_001")
	# 	self.assertStatusCode(r, u"两面长龙接口状态码错误%d" % r.status_code)
	# 	self.assertHasStr(r.text, "single_lottery_statistic_details")
	# 	mark = False
	# 	if len(r.json()["side_lottery_statistic_details"]) > 0 \
	# 			and r.json()["side_lottery_statistic_details"][0]["continuous_period_count"] >= 2:
	# 		mark = True
	# 	self.assertEqual(True, mark, u"两面长龙数据获取失败或错误")
	#
	# def test_statistic_infos_002(self):
	# 	"两面长龙-幸运飞艇"
	# 	r = self.req.get(interface_name="member_statistic_infos_001", url_change=True, lottery_id=2)
	# 	self.assertStatusCode(r, u"两面长龙接口状态码错误%d" % r.status_code)
	# 	self.assertHasStr(r.text, "single_lottery_statistic_details")
	# 	mark = False
	# 	if len(r.json()["side_lottery_statistic_details"]) > 0 \
	# 			and r.json()["side_lottery_statistic_details"][0]["continuous_period_count"] >= 2:
	# 		mark = True
	# 	self.assertEqual(True, mark, u"两面长龙数据获取失败或错误")
	#
	# # ******************冠亚和历史***********************************************************************************
	# def test_show_group_history_001(self):
	# 	'''冠亚和历史-极速赛车'''
	# 	r = self.req.get("member_show_group_history_001")
	# 	self.assertStatusCode(r, u"冠亚和历史-极速赛车状态码错误%d" % r.status_code)
	# 	self.assertHasStr(r.content, r"冠、亚军和")
	# 	self.assertHasStr(r.content, r"冠、亚军和大小")
	# 	self.assertHasStr(r.content, r"冠、亚军和单双")
	# 	mark = True
	# 	for record in r.json():
	# 		if record["name"] == u"冠、亚军和":
	# 			if len(record["details"]) == 0:
	# 				mark = False
	# 		if record["name"] == u"冠、亚军和大小":
	# 			self.assertHasStr(record["details"], u"大", u"冠亚军和历史中没有字符串'大'")
	# 			self.assertHasStr(record["details"], u"小", u"冠亚军和历史中没有字符串'小'")
	# 		if record["name"] == u"冠、亚军和单双":
	# 			self.assertHasStr(record["details"], u"单", u"冠亚军和历史中没有字符串'单'")
	# 			self.assertHasStr(record["details"], u"双", u"冠亚军和历史中没有字符串'双'")
	# 	self.assertEqual(True, mark, u"冠亚和历史数据为空或者不正确")
	#
	# def test_show_group_history_002(self):
	# 	'''冠亚和历史-幸运飞艇'''
	# 	r = self.req.get(interface_name="member_show_group_history_001", url_change=True, lottery_id=2)
	# 	self.assertStatusCode(r, u"冠亚和历史-极速赛车状态码错误%d" % r.status_code)
	# 	self.assertHasStr(r.content, r"冠、亚军和")
	# 	self.assertHasStr(r.content, r"冠、亚军和大小")
	# 	self.assertHasStr(r.content, r"冠、亚军和单双")
	# 	mark = True
	# 	for record in r.json():
	# 		if record["name"] == u"冠、亚军和":
	# 			if len(record["details"]) == 0:
	# 				mark = False
	# 		if record["name"] == u"冠、亚军和大小":
	# 			self.assertHasStr(record["details"], u"大", u"冠亚军和历史中没有字符串'大'")
	# 			self.assertHasStr(record["details"], u"小", u"冠亚军和历史中没有字符串'小'")
	# 		if record["name"] == u"冠、亚军和单双":
	# 			self.assertHasStr(record["details"], u"单", u"冠亚军和历史中没有字符串'单'")
	# 			self.assertHasStr(record["details"], u"双", u"冠亚军和历史中没有字符串'双'")
	# 	self.assertEqual(True, mark, u"冠亚和历史数据为空或者不正确")
	#
	# # ******************今日已结*************************************************************************************
	# def test_settled_today_001(self):
	# 	'''今日已结'''
	# 	r = self.req.get("member_settled_today_001")
	# 	self.assertStatusCode(r, u"今日已结获取接口状态码错误%d" % r.status_code)
	#
	# # ******************未结明细*************************************************************************************
	# def test_no_settle_001(self):
	# 	'''未结明细'''
	# 	r = self.req.get("member_no_settle_001")
	# 	self.assertStatusCode(r, u"未结明细获取接口状态码错误%d" % r.status_code)
	#
	# # ******************两周报表-全部*************************************************************************************
	# def test_reports_001(self):
	# 	'''两周报表-全部'''
	# 	r = self.req.get("member_reports_001")
	# 	self.assertStatusCode(r, u"两周报表-全部获取接口状态码错误%d" % r.status_code)
	#
	# def test_reports_002(self):
	# 	'''两周报表-极速赛车'''
	# 	r = self.req.get(interface_name="member_reports_001", url_change=True, lottery_id=6)
	# 	self.assertStatusCode(r, u"两周报表-获取接口状态码错误%d" % r.status_code)
	#
	# def test_reports_003(self):
	# 	'''两周报表-幸运飞艇'''
	# 	r = self.req.get(interface_name="member_reports_001", url_change=True, lottery_id=2)
	# 	self.assertStatusCode(r, u"两周报表-获取接口状态码错误%d" % r.status_code)
	#
	# # ******************报表注单明细-全部**********************************************************************************
	# def test_reports_retreating_001(self):
	# 	'''报表注单明细-全部'''
	# 	r = self.req.get(interface_name="member_reports_retreating_001", url_change=True, lottery_id=None,
	# 	                 date=getDate())
	# 	self.assertStatusCode(r, u"报表注单明细-全部接口状态码错误%d" % r.status_code)
	#
	# def test_reports_retreating_002(self):
	# 	'''报表注单明细-极速赛车'''
	# 	r = self.req.get(interface_name="member_reports_retreating_001", url_change=True, lottery_id=6, date=getDate())
	# 	self.assertStatusCode(r, u"报表注单明细接口状态码错误%d" % r.status_code)
	#
	# def test_reports_retreating_003(self):
	# 	'''报表注单明细-极速赛车'''
	# 	r = self.req.get(interface_name="member_reports_retreating_001", url_change=True, lottery_id=2, date=getDate())
	# 	self.assertStatusCode(r, u"报表注单明细接口状态码错误%d" % r.status_code)
	#
	# # ******************历史总帐*****************************************************************************************
	# def test_history_001(self):
	# 	'''历史总帐'''
	# 	r = self.req.get(interface_name="member_history_001", url_change=True, start_time=getDate(), end_time=getDate())
	# 	self.assertStatusCode(r, u"历史总帐接口状态码错误%d" % r.status_code)
	#
	# # ******************历史开奖*****************************************************************************************
	# def test_lottery_infos_001(self):
	# 	'''历史开奖-极速赛车'''
	# 	r = self.req.get(interface_name="member_lottery_infos_001", url_change=True, created_at=getDate(), lottery_id=6)
	# 	print(r.text)
	# 	self.assertStatusCode(r, u"历史开奖接口状态码错误%d" % r.status_code)
	# 	self.assertHasStr(r.text, "results", u"历史开奖接口未返回结果results")
	# 	self.assertNotNull(r.json()["results"], u"历史开奖返回开奖结果为空")
	# 	self.assertNotNull(r.json()["results"][0]["lottery_numbers"], u"历史开奖返回开奖结果号码为空")
	# 	self.assertNotNull(r.json()["results"][0]["details"][0]["lottery_result"], u"冠亚军和或者1~5龙虎为空")
	# 	self.assertNotNull(r.json()["results"][0]["details"][1]["lottery_result"], u"冠亚军和或者1~5龙虎为空")
	#
	# def test_lottery_infos_002(self):
	# 	'''历史开奖-幸运飞艇'''
	# 	r = self.req.get(interface_name="member_lottery_infos_001", url_change=True, created_at=getDate(), lottery_id=2)
	# 	# print(r.text, type(r.text))
	# 	# print(r.content, type(r.content))
	# 	self.assertStatusCode(r, u"历史开奖接口状态码错误%d" % r.status_code)
	# 	self.assertHasStr(r.text, "results", u"历史开奖接口未返回结果results")
	# 	self.assertNotNull(r.json()["results"], u"历史开奖返回开奖结果为空")
	# 	self.assertNotNull(r.json()["results"][0]["lottery_numbers"], u"历史开奖返回开奖结果号码为空")
	# 	self.assertNotNull(r.json()["results"][0]["details"][0]["lottery_result"], u"冠亚军和或者1~5龙虎为空")
	# 	self.assertNotNull(r.json()["results"][0]["details"][1]["lottery_result"], u"冠亚军和或者1~5龙虎为空")
	#
	#
	# # ******************自动下单-新增方案*********************************************************************************
	# def auto_bet(self, category):
	# 	'''
	# 	新增自动下单方案
	# 	:param category: 名次1，车号2, 大小3, 单双4, 随机名次5, 自选名次6, 随机选号7, 自选号码8
	# 	:return:
	# 	'''
	# 	data = {
	# 		"name": "名称-冠军开1号",  # 名称
	# 		"take_profit": 10000,  # 止盈金额
	# 		"stop_profit": -10000,  # 止损金额
	# 		"bet_amount_list": "10,20",  # 投注关卡
	# 		"category": 1,  # 下单方式
	# 	}
	# 	names = {"1": "名次", "2": "车号", "3": "大小", "4": "单双", "5":"随机名次", "6":"自选名次", "7":"随机选号", "8":"自选号码"}
	# 	num = 0
	# 	if category in (1, 2):
	# 		num = 11
	# 	elif category in (3, 4):
	# 		num = 3
	# 	else:
	# 		num = 2
	#
	# 	bet_amount = 10
	# 	data["category"] = category
	# 	config_text = {}
	# 	config_text["take_profit"] = data["take_profit"]
	# 	config_text["stop_profit"] = data["stop_profit"]
	# 	for i in range(1, num):
	# 		data["bet_amount_list"] = str(bet_amount) + "," + str(bet_amount + 10)
	# 		# 下单方式-名次\车号（category==1）
	# 		if category in (1, 2):
	# 			data["name"] = names[str(category)] + "-冠军开" + str(i) + "号"
	# 			data["previous_rank"] = 1
	# 			data["lottery_result"] = i
	# 			data["bet_result"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# 			config_text["name"] = data["name"]
	# 			config_text["bet_amount_list"] = data["bet_amount_list"]
	# 			config_text["category"] = data["category"]
	# 			config_text["previous_rank"] = data["previous_rank"]
	# 			config_text["lottery_result"] = data["lottery_result"]
	# 			config_text["bet_result"] = data["bet_result"]
	# 			data["config_text"] = json.dumps(config_text)
	#
	# 		# 下单方式-大小/单双（category==2）
	# 		elif category in (3, 4):
	# 			data["name"] = names[str(category)] + "-冠军开" + str(i) + "类型"
	# 			data["previous_rank"] = 1
	# 			data["lottery_result"] = i
	# 			data["bet_result"] = [1, 2]
	# 			config_text["name"] = data["name"]
	# 			config_text["bet_amount_list"] = data["bet_amount_list"]
	# 			config_text["category"] = data["category"]
	# 			config_text["previous_rank"] = data["previous_rank"]
	# 			config_text["lottery_result"] = data["lottery_result"]
	# 			config_text["bet_result"] = data["bet_result"]
	# 			data["config_text"] = json.dumps(config_text)
	#
	# 		# 随机名次
	# 		elif category == 5:
	# 			data["name"] = names[str(category)]
	# 			data["bet_game"] = 1
	# 			data["rand_count"] = 5
	# 			config_text["name"] = data["name"]
	# 			config_text["bet_amount_list"] = data["bet_amount_list"]
	# 			config_text["category"] = data["category"]
	# 			config_text["bet_game"] = data["bet_game"]
	# 			config_text["rand_count"] = data["rand_count"]
	# 			data["config_text"] = json.dumps(config_text)
	#
	# 		# 自选名次
	# 		elif category == 6:
	# 			data["name"] = names[str(category)]
	# 			data["bet_game"] = 1
	# 			data["bet_position"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# 			config_text["name"] = data["name"]
	# 			config_text["bet_amount_list"] = data["bet_amount_list"]
	# 			config_text["category"] = data["category"]
	# 			config_text["bet_game"] = data["bet_game"]
	# 			config_text["bet_position"] = data["bet_position"]
	# 			data["config_text"] = json.dumps(config_text)
	#
	# 		# 随机选号
	# 		elif category == 7:
	# 			data["name"] = names[str(category)]
	# 			data["bet_position"] = 1
	# 			data["rand_count"] = 5
	# 			config_text["name"] = data["name"]
	# 			config_text["bet_amount_list"] = data["bet_amount_list"]
	# 			config_text["category"] = data["category"]
	# 			config_text["bet_position"] = data["bet_position"]
	# 			config_text["rand_count"] = data["rand_count"]
	# 			data["config_text"] = json.dumps(config_text)
	#
	# 		# 自选号码
	# 		elif category == 8:
	# 			data["name"] = names[str(category)]
	# 			data["bet_position"] = 1
	# 			data["bet_ball"] = [1, 6, 7, 2, 3, 4, 5, 9, 10, 8]
	# 			config_text["name"] = data["name"]
	# 			config_text["bet_amount_list"] = data["bet_amount_list"]
	# 			config_text["category"] = data["category"]
	# 			config_text["bet_position"] = data["bet_position"]
	# 			config_text["bet_ball"] = data["bet_ball"]
	# 			data["config_text"] = json.dumps(config_text)
	# 		else:
	# 			print("wrong category：%d" % category)
	# 			break
	#
	# 		r = self.req.post(interface_name="member_tw_auto_bet_001", data_change=True, data=data)
	# 		self.assertStatusCode(r, r.content)
	# 		self.assertEqual(data["name"], r.json()["name"].encode("utf-8"))
	#
	# 		bet_amount += 20
	#
	# @unittest.skip("skip")
	# def test_tw_auto_bet_001(self):
	# 	# 新增按名次下单方案
	# 	self.auto_bet(category=1)
	#
	# @unittest.skip("skip")
	# def test_tw_auto_bet_002(self):
	# 	# 新增按车号下单方案
	# 	self.auto_bet(category=2)
	#
	# @unittest.skip("skip")
	# def test_tw_auto_bet_003(self):
	# 	# 新增按大小下单方案
	# 	self.auto_bet(category=3)
	#
	# @unittest.skip("skip")
	# def test_tw_auto_bet_004(self):
	# 	# 新增按单双下单方案
	# 	self.auto_bet(category=4)
	#
	# @unittest.skip("skip")
	# def test_tw_auto_bet_005(self):
	# 	# 新增按随机名次下单方案
	# 	self.auto_bet(category=5)
	#
	# @unittest.skip("skip")
	# def test_tw_auto_bet_006(self):
	# 	# 新增按自选名次下单方案
	# 	self.auto_bet(category=6)
	#
	# @unittest.skip("skip")
	# def test_tw_auto_bet_007(self):
	# 	# 新增按随机选号下单方案
	# 	self.auto_bet(category=7)
	#
	# @unittest.skip("skip")
	# def test_tw_auto_bet_008(self):
	# 	# 新增按自选号码下单方案
	# 	self.auto_bet(category=8)


if __name__ == '__main__':
	suite = unittest.TestSuite(unittest.makeSuite(TestMember))
	unittest.TextTestRunner(verbosity=2).run(suite)
