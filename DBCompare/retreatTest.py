#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

from rfelibGame import rfelibGame

if __name__ == '__main__':

	url = 'https://tw.admin.game.cqut.net'
	db = "mysql,root/123456@192.168.1.10:30827/game_api_stage_tw"
	token = "c68782fc718de7c2c1e5da900ba4f402a995ed31849b7347e248da30205aea0b"
	ids = {'main_id': 1, 'line_organizations': [1, 189, 190, 191, 192, 193], 'last_member_id': 32}
	lottery_id = 6
	setting_group_id = 224
	amount = 10
	
	obj = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	# rs = obj.case("1/1")
	# if rs:
	# 	print("*INFO* 1/1 pass")
	# else:
	# 	print("*ERROR* 1/1 fail")
	#
	# # case2 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	# rs = obj.case("2/1")
	# if rs:
	# 	print("*INFO* 2/1 pass")
	# else:
	# 	print("*ERROR* 2/1 fail")
	#
	# # case3 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	# rs = obj.case("3/1")
	# if rs:
	# 	print("*INFO* 3/1 pass")
	# else:
	# 	print("*ERROR* 3/1 fail")
	#
	# # case4 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	# rs = obj.case("4/1")
	# if rs:
	# 	print("*INFO* 4/1 pass")
	# else:
	# 	print("*ERROR* 4/1 fail")
	#
	# # case5 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	# rs = obj.case("5/1")
	# if rs:
	# 	print("*INFO* 5/1 pass")
	# else:
	# 	print("*ERROR* 5/1 fail")
	#
	# # case6 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	# rs = obj.case("1/2")
	# if rs:
	# 	print("*INFO* 1/2 pass")
	# else:
	# 	print("*ERROR* 1/2 fail")
	#
	# # case7 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	# rs = obj.case("2/2")
	# if rs:
	# 	print("*INFO* 2/2 pass")
	# else:
	# 	print("*ERROR* 2/2 fail")
	#
	# # case8 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	# rs = obj.case("3/2")
	# if rs:
	# 	print("*INFO* 3/2 pass")
	# else:
	# 	print("*ERROR* 3/2 fail")

	# case9 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	rs = obj.case("4/2")
	if rs:
		print("*INFO* 4/2 pass")
	else:
		print("*ERROR* 4/2 fail")

	# # case10 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
	# rs = obj.case("5/2")
	# if rs:
	# 	print("*INFO* 5/2 pass")
	# else:
	# 	print("*ERROR* 5/2 fail")
