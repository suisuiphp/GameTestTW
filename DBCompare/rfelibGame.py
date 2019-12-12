#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

from DBApi import DBApi
import requests
from copy import deepcopy

class rfelibGame():
	def __init__(self,token,db,url,ids,lottery_id,setting_group_id,amount):
		self.token = token
		self.ids = ids
		self.main_id = ids["main_id"]
		self.line_organizations = ids['line_organizations']
		self.last_member_id = ids['last_member_id']
		self.setting_group_id = setting_group_id
		self.lottery_id = lottery_id
		self.amount = 10
		self.db = DBApi(db)
		self.url = url
		self.headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'Accept': 'application/json, text/plain, */*',
			'token': self.token
		}
	
	def get_retreating_data(self, id=1, usertype=1, setting_group_id=220):
		'''
		根据组织id、会员id、分组id获取退水配置信息
		:param id: 组织id或会员id
		:param usertype: 用户类型，1代表组织，2代表会员
		:param setting_group_id:
		:return: 列表（A盘退水、B盘退水、C盘退水、D盘退水、E盘退水、F盘退水、单注最高、单注最低、单期限额）
		'''
		
		if usertype == 1:
			sql = 'SELECT a_proportion,b_proportion,c_proportion,d_proportion,e_proportion,f_proportion,single_highest_quota,single_lowest_quota,single_period_quota' \
			      ' FROM retreating_instances ' \
			      ' WHERE setting_group_id =' + str(setting_group_id) + '' \
			                                                            ' AND organization_id =' + str(id)
		
		
		elif usertype == 2:
			sql = 'SELECT a_proportion,b_proportion,c_proportion,d_proportion,e_proportion,f_proportion,single_highest_quota,single_lowest_quota,single_period_quota' \
			      ' FROM retreating_instances ' \
			      ' WHERE setting_group_id =' + str(setting_group_id) + '' \
			                                                            ' AND member_id =' + str(id)
		else:
			print("*ERROR*  Wrong usertype!")
			return
		
		retreating_data = self.db.listDataBySQL(sql)
		list_retreating_data = [item for item in retreating_data[0]]
		return list_retreating_data
		
	
	def change_retreating(self,link_item,equal_add,add_amount=10,lottery_id=6,setting_group_id=220,channel=1):
		'''
		修改退水
		:param link_item: 条件（1：不影响，2：影响该层级，3：影响该组织线，4：影响全部层级，5：全部影响）
		:param equal_add: 条件（1：等量增加，2：不等量增加）
		:param add_amount: 增减的量
		:param lottery_id: 彩种id
		:param setting_group_id: 分组id
		:param channel:
		:return:
		'''
		# lottery_id = lottery_id
		# add_amount = add_amount
		# setting_group_id = setting_group_id
		# equal_add = equal_add
		# channel = channel
		origin_data = self.get_retreating_data(id=1,usertype=1,setting_group_id=setting_group_id)
		origin_a_proportion = origin_data[0]
		origin_b_proportion = origin_data[1]
		origin_c_proportion = origin_data[2]
		origin_d_proportion = origin_data[3]
		origin_e_proportion = origin_data[4]
		origin_f_proportion = origin_data[5]
		origin_single_highest_quota = origin_data[6]
		origin_single_lowest_quota = origin_data[7]
		origin_single_period_quota = origin_data[8]

		data = '{"data": [{' + '"lottery_id": ' + str(lottery_id) + ',"in_data": [{' +'' \
		        '"a_proportion": ' + str(origin_a_proportion+add_amount) + ',' + '' \
		        '"b_proportion": ' + str(origin_b_proportion+add_amount) + ',' + '' \
		        '"c_proportion": ' + str(origin_c_proportion+add_amount) + ',' + '' \
		        '"d_proportion": ' + str(origin_d_proportion+add_amount) + ',' + '' \
		        '"e_proportion": ' + str(origin_e_proportion+add_amount) + ',' + '' \
		        '"f_proportion": ' + str(origin_f_proportion+add_amount) + ',' + '' \
		        '"single_period_quota": ' + str(origin_single_period_quota+add_amount) + ',' + '' \
		        '"single_highest_quota": ' + str(origin_single_highest_quota+add_amount) + ',' + '' \
		        '"single_lowest_quota": ' + str(origin_single_lowest_quota+add_amount) + ',' + '' \
		        '"origin_a_proportion": ' + str(origin_a_proportion) + ',' + '' \
		        '"origin_b_proportion": ' + str(origin_b_proportion) + ',' + '' \
		        '"origin_c_proportion": ' + str(origin_c_proportion) + ',' + '' \
		        '"origin_d_proportion": ' + str(origin_d_proportion) + ',' + '' \
		        '"origin_e_proportion": ' + str(origin_e_proportion) + ',' + '' \
		        '"origin_f_proportion": ' + str(origin_f_proportion) + ',' + '' \
		        '"origin_single_period_quota": ' + str(origin_single_period_quota) + ',' + '' \
		        '"origin_single_highest_quota": ' + str(origin_single_highest_quota) + ',' + '' \
		        '"origin_single_lowest_quota": ' + str(origin_single_lowest_quota) + ',' + '' \
		        '"setting_group_id": ' + str(setting_group_id) + ',' + '' \
		        '"group": 1}]}],'  + '' \
		        '"equal_add": ' + str(equal_add) + ',' + '' \
		        '"channel": ' + str(channel) + ',' + '' \
		        '"link_item": ' + str(link_item) + ',' + '' \
		        '"setting_group_ids": [' + str(setting_group_id) + ']}'

		url = self.url+'/server/api/tw_manage/system_manage/limit_quota'
		res = requests.post(url=url, data=data, headers=self.headers)
		# print(res.status_code)
		if res.status_code != 201:
			print("退水修改失败")
			return False
		else:
			# print("退水修改成功")
			return True
	
	
	def assert_dict_data(self, refer_data, object_data):
		'''
		比较两个字段中，相同key的value值是否相同
		:param refer_data:
		:param object_data:
		:return:
		'''
		
		for key in refer_data:
			if refer_data[key] != object_data[key]:
				print("用户id:%s 退水配置错误\nexpect:%s\nacturl:%s" % (key, str(refer_data[key]), str(object_data[key])))
				return False
		return True
	
	def get_retreating_datas_from_db(self, organization_ids, member_id=None, setting_group_id=220):
		'''
		从数据库中查询组织或者会员的退水配置信息
		:param organization_ids: 组织id列表
		:param member_id:
		:param setting_group_id:
		:return: {id:[]}
		'''
		retreating_datas = {}
		
		for id in organization_ids:
			retreating_data = self.get_retreating_data(int(id), 1, setting_group_id)
			retreating_datas[id] = retreating_data
		if member_id != None:
			retreating_data = self.get_retreating_data(member_id, 2, setting_group_id)
			retreating_datas[member_id] = retreating_data
		
		return retreating_datas
	
	def calculate_retreating_datas(self, origin_retreating_data, change_type, ids, amount=10):
		'''
		计算配置修改后的预期结果数据
		:param origin_retreating_data:字典，修改前的退水配置信息，{id:[10,20...]}
		:param change_type:修改条件，"1/1","1/2","2/1","2/2"，"3/1"...
		:param ids:{'main_id':1,'line_organizations':[61,62,63],'last_member_id':32}
		:param amont:增见量
		:return:修改后的预期结果数据，字典
		'''
		result_retreating_data = deepcopy(origin_retreating_data)
		main_id = ids["main_id"]  # 修改人的id
		line_organizations = ids['line_organizations'][:]
		last_member_id = ids['last_member_id']
		
		#不影响/等量增加；不影响/不等量增加；影响该层级/等量增加；影响该层级/不等量增加
		if change_type in ("1/1","1/2","2/1","2/2"):
			result_retreating_data[main_id] = self.add_amount_for_list(result_retreating_data[main_id],amount)

				
		#影响该组织线/等量增加；全部影响/等量增加
		elif change_type in ("3/1","5/1"):
			line_organizations.append(last_member_id)
			for id in line_organizations:
				result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id],amount)
		
		#影响该组织线/不等量增加; 全部影响/不等量增加
		elif change_type in ("3/2","5/2"):
			result_retreating_data[main_id] = self.add_amount_for_list(result_retreating_data[main_id],amount)
			line_organizations.append(last_member_id)
			for id in line_organizations:
				result_retreating_data[id] = [effected_value for effected_value in result_retreating_data[main_id]]
		
		# 影响全部层级，等量增加
		elif change_type == "4/1":
			for id in line_organizations:
				result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id],amount)
			
		# 影响全部层级，不等量增加
		elif change_type == "4/2":
			result_retreating_data[main_id] = self.add_amount_for_list(result_retreating_data[main_id], amount)
			for id in line_organizations:
				result_retreating_data[id] = [effected_value for effected_value in result_retreating_data[main_id]]
		
		# # 影响全部影响，等量增加
		# elif change_type == "5/1":
		# 	pass
	
		# # 影响全部影响，不等量增加
		# elif change_type == "5/2":
		# 	pass
		
		else:
			print("错误的修改方式")
			
		
		
		return result_retreating_data
	
	def add_amount_for_list(self,list,amount):
		list = [x+amount for x in list ]
		return list
			
	def case(self,condition):
		'''
		
		:param condition: "1/1" "link_item/equal_add"
		:return:
		'''
		print("condition:%s" % condition)
		
		link_item = condition.split("/")[0]
		equal_add = condition.split("/")[1]
		
		#测试前先保证总公司与分公司的值不相同
		# self.change_retreating(lottery_id=self.lottery_id,
		#                           setting_group_id=self.setting_group_id,
		#                           add_amount=-self.amount,
		#                           link_item=1,
		#                           equal_add=1)
		# self.change_retreating(lottery_id=self.lottery_id,
		#                        setting_group_id=self.setting_group_id,
		#                        add_amount=self.amount,
		#                        link_item=1,
		#                        equal_add=1)
		
		#修改前退水配置
		origin_retreating_data = self.get_retreating_datas_from_db(self.line_organizations,self.last_member_id, self.setting_group_id)
		
		#修改初始限额退水配置
		if self.change_retreating(lottery_id = self.lottery_id,
		                                  setting_group_id = self.setting_group_id,
		                                  add_amount = self.amount,
		                                  link_item = link_item,
		                                  equal_add = equal_add):
			
			#获取修改后退水
			result_retreating_data = self.get_retreating_datas_from_db(self.line_organizations,self.last_member_id,self.setting_group_id)
		
		#计算预期结果
		expect_retreating_data = self.calculate_retreating_datas(origin_retreating_data,condition,self.ids,self.amount)

		#断言实际结果与预期结果是否一直
		rs = self.assert_dict_data(expect_retreating_data, result_retreating_data)
		# if rs:
		# 	print("case 1 pass")
		# else:
		# 	print("case 1 wrong")
		return rs
		
		
			

			
# if __name__ == '__main__':
# 	url = 'https://tw.admin.game.cqut.net'
# 	db = "mysql,root/123456@192.168.1.10:30827/game_api_stage_tw"
# 	token = "04a6d15ec2a0c43187564686db7461df4ba755d2d2a047d47fcf861a13d0fa81"
# 	ids = {'main_id':1,'line_organizations':[1,189,190,191,192,193],'last_member_id':32}
# 	lottery_id = 6
# 	setting_group_id = 220
# 	amount = 10
#
# 	obj = rfelibGame(token,db,url,ids,lottery_id,setting_group_id,amount)
# 	rs = obj.case("1/1")
# 	if rs:print("*INFO* 1/1 pass")
# 	else:print("*ERROR* 1/1 fail")
#
# 	# case2 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
# 	rs = obj.case("2/1")
# 	if rs:print("*INFO* 2/1 pass")
# 	else:print("*ERROR* 2/1 fail")
#
# 	# case3 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
# 	rs = obj.case("3/1")
# 	if rs:print("*INFO* 3/1 pass")
# 	else:print("*ERROR* 3/1 fail")
#
# 	# case4 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
# 	rs = obj.case("4/1")
# 	if rs:print("*INFO* 4/1 pass")
# 	else:print("*ERROR* 4/1 fail")
#
# 	# case5 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
# 	rs = obj.case("5/1")
# 	if rs:print("*INFO* 5/1 pass")
# 	else:print("*ERROR* 5/1 fail")
#
# 	# case6 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
# 	rs = obj.case("1/2")
# 	if rs:print("*INFO* 1/2 pass")
# 	else:print("*ERROR* 1/2 fail")
#
# 	# case7 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
# 	rs = obj.case("2/2")
# 	if rs:print("*INFO* 2/2 pass")
# 	else:print("*ERROR* 2/2 fail")
#
# 	# case8 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
# 	rs = obj.case("3/2")
# 	if rs:print("*INFO* 3/2 pass")
# 	else:print("*ERROR* 3/2 fail")
#
# 	# case9 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
# 	rs = obj.case("4/2")
# 	if rs:print("*INFO* 4/2 pass")
# 	else:print("*ERROR* 4/2 fail")
#
# 	# case10 = rfelibGame(token, db, url, ids, lottery_id, setting_group_id, amount)
# 	rs = obj.case("5/2")
# 	if rs:print("*INFO* 5/2 pass")
# 	else:print("*ERROR* 5/2 fail")
	




	
	
		
	