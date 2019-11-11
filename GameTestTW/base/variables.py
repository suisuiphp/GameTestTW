#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

global BJSC, JSSSC, XYNC, JSSC, XYFT, CQHLSS, JSFT, GXKS, GDSYXW
BJSC = 1  # 北京赛车
XYFT = 2  # 幸运飞艇
JSSSC = 3  # 极速时时彩
XYNC = 5  # 幸运农场
JSSC = 6  # 极速赛车
CQHLSS = 7  # 重庆欢乐生肖
JSFT = 9  # 极速飞艇
GXKS = 10  # 广西快三
GDSYXW = 11  # 广东十一选五

global LOTTERIES
LOTTERIES = {}
LOTTERIES[BJSC] = "北京赛车"
LOTTERIES[XYFT] = "幸运飞艇"
LOTTERIES[JSSSC] = "极速时时彩"
LOTTERIES[XYNC] = "幸运农场"
LOTTERIES[JSSC] = "极速赛车"
LOTTERIES[CQHLSS] = "重庆欢乐生肖"
LOTTERIES[JSFT] = "极速飞艇"
LOTTERIES[GXKS] = "广西快三"
LOTTERIES[GDSYXW] = "广东十一选五"



class Variables:
	# environment = "TEST"
	environment = "PRODUCTION"
	
	# 亚马逊环境
	if environment == "PRODUCTION":
		url_admin = "http://admin.win2019.cc"
		url_member = "http://member.win2019.cc"
		db = "mysql,zoujun/Zj123456@game-database.cluster-ccw6luzub8ta.ap-northeast-1.rds.amazonaws.com:3306/game-api-production"
		
		admin_account = "sub01/6yhn6tfc"
		member_account = "ee1/qwe123"
		
		admin_mark = "01"
		member_mark = "zy"
	
		# line1：非独立调配02，line2，独立调配01
		ids_a = {"top_id": 1, "line1": [324, 325, 326, 327, 328, 329, 330, 331, 332, 333],
		         "members1": [532, 533, 534, 535, 536, 537, 538, 539, 540, 541],
		         "line2": [314, 315, 316, 317, 318, 319, 320, 321, 322, 323],
		         "members2": [522, 523, 524, 525, 526, 527, 528, 529, 530, 531]}
		
		# line1：独立调配01，line2，独立调配03, line3：非独立调配02
		ids_b = {"top_id": 1, "line1": [314, 315, 316, 317, 318, 319, 320, 321, 322, 323],
		         "members1": [522, 523, 524, 525, 526, 527, 528, 529, 530, 531],
		         "line2": [354, 355, 356, 357, 358, 359, 360, 361, 362, 363],
		         "members2": [543, 544, 545, 546, 547, 548, 549, 550, 551, 552],
		         "line3": [324, 325, 326, 327, 328, 329, 330, 331, 332, 333],
		         "member3": [532, 533, 534, 535, 536, 537, 538, 539, 540, 541]}
		
		# line1：独立调配01，line2，独立调配03, line3：非独立调配02
		ids_c = {"top_id": 1, "line1": [314, 315, 316, 317, 318, 319, 320, 321, 322, 323],
		         "members1": [522, 523, 524, 525, 526, 527, 528, 529, 530, 531],
		         "line2": [354, 355, 356, 357, 358, 359, 360, 361, 362, 363],
		         "members2": [543, 544, 545, 546, 547, 548, 549, 550, 551, 552],
		         "line3": [324, 325, 326, 327, 328, 329, 330, 331, 332, 333],
		         "member3": [532, 533, 534, 535, 536, 537, 538, 539, 540, 541]}
		
		# line1：非独立调配02，line2，非独立调配06, line3:独立调配01
		ids_d = {"top_id": 1, "line1": [324, 325, 326, 327, 328, 329, 330, 331, 332, 333],
		         "members1": [532, 533, 534, 535, 536, 537, 538, 539, 540, 541],
		         "line2": [364, 365, 366, 367, 368, 369, 370, 371, 372, 373],
		         "members2": [553, 554, 555, 556, 557, 558, 559, 560, 561, 562],
		         "line3": [314, 315, 316, 317, 318, 319, 320, 321, 322, 323],
		         "member3": [522, 523, 524, 525, 526, 527, 528, 529, 530, 531]}
		
		# line1：非独立调配02，line2，非独立调配06, line3:独立调配01
		ids_m = {"top_id": 1, "line1": [324, 325, 326, 327, 328, 329, 330, 331, 332, 333],
		         "members1": [532, 533, 534, 535, 536, 537, 538, 539, 540, 541],
		         "line2": [364, 365, 366, 367, 368, 369, 370, 371, 372, 373],
		         "members2": [553, 554, 555, 556, 557, 558, 559, 560, 561, 562],
		         "line3": [314, 315, 316, 317, 318, 319, 320, 321, 322, 323],
		         "member3": [522, 523, 524, 525, 526, 527, 528, 529, 530, 531]}
	
	# 本地测试环境
	if environment == "TEST":
		db = "mysql,root/123456@192.168.1.10:30827/game_api_stage_tw"


def getAdminUrl():
	return Variables.url_admin


def getMemberUrl():
	return Variables.url_member


def getDb():
	return Variables.db


def getAdminAccount():
	return Variables.admin_account


def getMemberAccount():
	return Variables.member_account


def getMemberMark():
	return Variables.member_mark


def getAdminMark():
	return Variables.admin_mark


def getIds(id_mark):
	if id_mark == "a":
		return Variables.ids_a
	elif id_mark == "b":
		return Variables.ids_b
	elif id_mark == "c":
		return Variables.ids_c
	elif id_mark == "d":
		return Variables.ids_d
	elif id_mark == "m":
		return Variables.ids_m
	else:
		print("Wrong id_mark!")
