#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

from utils.DBApi import DBApi
from base.user import User
from base.variables import *
import json
from copy import deepcopy


class Retreat(User):
	'''
	使用该类里面的方法时，需要先执行初始化函数
	'''
	def __init__(self, user_type=1, id_mark="a",**kwargs):
		User.__init__(self,user_type,**kwargs)
		self.conn = DBApi(self.db)
		self.ids = getIds(id_mark)
	
	
	def error_msg(self, flag, msg, condition, id):
		if not flag:
			msg.append(
				"*INIT-ERROR*----%s,organization_id:%d,link_item=1, equal_add=1, add_amount=-10" % (condition, id))
		return msg
	
	def reset_retreat_data(self, condition, normal_case=True, independent=False):
		interface_name = "admin_limit_quota_001"
		flag = True
		msg = ["*INIT-ERROR*-----------------"]
		if normal_case and condition in ("1/1", "1/2"):
			print("----------reset_retreat_data:1/1,1/2")
			flag = self.post(
				interface_name=interface_name, data_change=True,
				organization_id=self.ids["line1"][0], link_item=1, equal_add=1,
				add_amount=-10, lottery_id=6, setting_group_id=220, channel=2)
			self.error_msg(flag, msg, condition, self.ids["line1"][0])
		
		elif normal_case and condition == "2/1":
			flag = self.post(
				interface_name=interface_name, data_change=True,
				organization_id=self.ids["line1"][0], link_item=1, equal_add=1,
				add_amount=-10, lottery_id=6, setting_group_id=220, channel=2)
			self.error_msg(flag, msg, condition, self.ids["line1"][0])
			
			flag = self.post(
				interface_name=interface_name, data_change=True,
				organization_id=self.ids["line2"][0], link_item=1, equal_add=1,
				add_amount=-15, lottery_id=6, setting_group_id=220, channel=2)
			self.error_msg(flag, msg, condition, self.ids["line2"][0])
		
		elif normal_case and condition == "2/2":
			if not independent:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=1, link_item=5, equal_add=2, add_amount=10, lottery_id=6,
					setting_group_id=220, channel=1)
				self.error_msg(flag, msg, condition, 1)
			flag = self.post(
				interface_name=interface_name, data_change=True,
				organization_id=self.ids["line1"][0], link_item=1, equal_add=1,
				add_amount=-10, lottery_id=6, setting_group_id=220, channel=2)
			self.error_msg(flag, msg, condition, self.ids["line1"][0])
			flag = self.post(
				interface_name=interface_name, data_change=True,
				organization_id=self.ids["line2"][0], link_item=1, equal_add=1,
				add_amount=-10, lottery_id=6, setting_group_id=220, channel=2)
			self.error_msg(flag, msg, condition, self.ids["line2"][0])
		
		elif normal_case and condition in ("3/1", "3/2"):
			for id in self.ids["line1"]:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=-20,
					lottery_id=6, setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=10, lottery_id=6,
					setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
		
		elif normal_case and condition in ("4/1", "4/2", "5/1", "5/2"):
			if not independent:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=1, link_item=5, equal_add=2, add_amount=10, lottery_id=6,
					setting_group_id=220, channel=1)
				self.error_msg(flag, msg, condition, 1)
			for id in self.ids["line1"]:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=-20,
					lottery_id=6, setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=10, lottery_id=6,
					setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
			for id in self.ids["line2"]:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=-20,
					lottery_id=6, setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=10, lottery_id=6,
					setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
		
		elif (not normal_case) and condition in ("2/1", "4/1", "5/1"):  # 影响该层级，等量增加不成功
			if not independent:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=1, link_item=5, equal_add=2, add_amount=10, lottery_id=6,
					setting_group_id=220, channel=1)
				self.error_msg(flag, msg, condition, 1)
			for id in self.ids["line1"]:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=-20,
					lottery_id=6, setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=10, lottery_id=6,
					setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
			for id in self.ids["line2"]:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=-10,
					lottery_id=6, setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=5, lottery_id=6,
					setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
		elif (not normal_case) and condition in ("2/2", "4/2", "5/2"):  # 影响该层级，并影响下级
			if not independent:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=1, link_item=5, equal_add=2, add_amount=10, lottery_id=6,
					setting_group_id=220, channel=1)
				self.error_msg(flag, msg, condition, 1)
			for id in self.ids["line1"]:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=-20,
					lottery_id=6, setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=10, lottery_id=6,
					setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
			for id in self.ids["line2"]:
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=-10,
					lottery_id=6, setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
				flag = self.post(
					interface_name=interface_name, data_change=True,
					organization_id=id, link_item=1, equal_add=1, add_amount=5, lottery_id=6,
					setting_group_id=220, channel=2)
				self.error_msg(flag, msg, condition, id)
			flag = self.post(
				interface_name=interface_name, data_change=True,
				organization_id=self.ids["line1"][0], link_item=1, equal_add=1,
				add_amount=-20, lottery_id=6, setting_group_id=220, channel=2)  # line1第一个用户减20
			self.error_msg(flag, msg, condition, self.ids["line1"][0])
		else:
			print("*ERROR* wrong reset condition!")
		
		return flag, "\n".join(msg)
	
	def reset_independent_retreat_data(self, gs_id):
		'''
		必须由总公司执行，总公司在用户管理修改独立调配公司的数据，全部影响不等量增加
		:param gs_id:
		:return:
		'''
		print("-------------总公司在用户管理页面修改公司退水，5/2，+10")
		interface_name = "admin_limit_quota_001"
		flag = self.post(
			interface_name=interface_name, data_change=True, organization_id=gs_id, link_item=5, equal_add=2,
			add_amount=10, lottery_id=6, setting_group_id=220, channel=2)
	
	def get_retreating_datas_from_db(self, ids, setting_group_id=220):
		'''
		从数据库中查询组织或者会员的退水配置信息
		:param ids: ids = {"top_id":1,"line1":[478, 479],"members1":[139, 140], "line2":[488, 489],"members2":[151, 152]}
		:param member_id:
		:param setting_group_id:
		:return: {id:[]}
		'''
		retreating_datas = {}
		
		retreating_data = self.get_retreating_data(int(ids["top_id"]), 1, setting_group_id)
		retreating_datas[ids["top_id"]] = retreating_data
		for id in ids["line1"]:
			retreating_data = self.get_retreating_data(int(id), 1, setting_group_id)
			retreating_datas[id] = retreating_data
		for id in ids["line2"]:
			retreating_data = self.get_retreating_data(int(id), 1, setting_group_id)
			retreating_datas[id] = retreating_data
		for id in ids["members1"]:
			retreating_data = self.get_retreating_data(int(id), 2, setting_group_id)
			retreating_datas[id] = retreating_data
		for id in ids["members2"]:
			retreating_data = self.get_retreating_data(int(id), 2, setting_group_id)
			retreating_datas[id] = retreating_data
		# print(retreating_datas)
		
		return retreating_datas
	
	def add_amount_for_list(self, list, amount):
		list = [x + amount for x in list]
		return list
	
	def calculate_retreating_datas(self, origin_retreating_data, change_type, ids, obj_id, amount=10):
		'''
		计算配置修改后的预期结果数据
		:param origin_retreating_data:字典，修改前的退水配置信息，{id:[10,20...]}
		:param change_type:修改条件，"1/1","1/2","2/1","2/2"，"3/1"...
		:param ids: {"top_id":1,"line1":[478, 479],"members1":[139, 140], "line2":[488, 489],"members2":[151, 152]}
		:param is_top:true：修改顶层用户总公司、独立调配公司 false：修改下级用户
		:param amont:增减量
		:return:修改后的预期结果数据，字典
		'''
		result_retreating_data = deepcopy(origin_retreating_data)
		
		# 修改总公司初始限额
		if obj_id == 1:
			# line1 为非独立调配公司线，line2为独立调配公司线
			result_retreating_data[ids["top_id"]] = self.add_amount_for_list(result_retreating_data[ids["top_id"]],
			                                                                 amount)
			# 不影响/等量增加；不影响/不等量增加；影响该层级/等量增加；影响该层级/不等量增加
			if change_type in ("1/1", "1/2", "2/1", "2/2"):
				pass
			
			# 影响该组织线/等量增加；全部影响/等量增加
			elif change_type in ("3/1", "5/1"):
				for id in ids["line1"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
				for id in ids["members1"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
			
			# 影响该组织线/不等量增加; 全部影响/不等量增加
			elif change_type in ("3/2", "5/2"):
				for id in ids["line1"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["top_id"]]]
				for id in ids["members1"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["top_id"]]]
			
			# 影响全部层级，等量增加
			elif change_type == "4/1":
				for id in ids["line1"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
			
			# 影响全部层级，不等量增加
			elif change_type == "4/2":
				for id in ids["line1"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["top_id"]]]
			else:
				print("错误的修改方式")
		
		else:  # 修改公司或以下层级
			# 不影响/等量增加；不影响/不等量增加；
			if change_type in ("1/1", "1/2"):
				result_retreating_data[ids["line1"][0]] = self.add_amount_for_list(
					result_retreating_data[ids["line1"][0]], amount)
			
			# 影响该层级/等量增加 若该层级等量增加后超过上级，那么会修改不成功
			elif change_type in ("2/1"):
				result_retreating_data[ids["line1"][0]] = self.add_amount_for_list(
					result_retreating_data[ids["line1"][0]], amount)
				effected_line2_data = self.add_amount_for_list(result_retreating_data[ids["line2"][0]], amount)
				for i in range(0, len(effected_line2_data)):
					if effected_line2_data[i] > result_retreating_data[ids["top_id"]][i]:
						print("退水配置超过上级，则设置等于上级，id：{0}".format(ids["line2"][0]))
						effected_line2_data[i] = result_retreating_data[ids["top_id"]][i]
				result_retreating_data[ids["line2"][0]] = [value for value in effected_line2_data]
			
			# 影响该层级/不等量增加 若该层级被影响为相同值后低于下级，则更新下级值为相同值,这里只改了一个层级，需要优化
			elif change_type in ("2/2"):
				result_retreating_data[ids["line1"][0]] = self.add_amount_for_list(
					result_retreating_data[ids["line1"][0]], amount)
				result_retreating_data[ids["line2"][0]] = [
					effected_value for effected_value in result_retreating_data[ids["line1"][0]]]
				for j in range(0, len(ids["line2"]) - 1):
					for i in range(0, len(result_retreating_data[ids["line2"][j]])):
						if result_retreating_data[ids["line2"][j]][i] < result_retreating_data[ids["line2"][j + 1]][i]:
							# print("退水配置低于下级，id：{0}，将修改下级id{1}数据".format(ids["line2"][j]), ids["line2"][j + 1])
							result_retreating_data[ids["line2"][j + 1]][i] = result_retreating_data[ids["line2"][j]][i]
				for j in range(0, len(ids["line2"])):
					for i in range(0, len(result_retreating_data[ids["line2"][j]])):
						if result_retreating_data[ids["line2"][j]][i] < result_retreating_data[ids["members2"][j]][i]:
							result_retreating_data[ids["members2"][j]][i] = result_retreating_data[ids["line2"][j]][i]
			
			
			# 影响该组织线/等量增加
			elif change_type in ("3/1"):
				for id in ids["line1"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
				for id in ids["members1"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
			
			# 影响该组织线/不等量增加
			elif change_type in ("3/2"):
				result_retreating_data[ids["line1"][0]] = self.add_amount_for_list(
					result_retreating_data[ids["line1"][0]], amount)
				for id in ids["line1"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["line1"][0]]]
				for id in ids["members1"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["line1"][0]]]
			
			# 影响全部层级，等量增加
			elif change_type == "4/1":
				for id in ids["line1"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
				for id in ids["line2"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
				for i in range(0, len(result_retreating_data[ids["line2"][0]])):
					if result_retreating_data[ids["line2"][0]][i] > result_retreating_data[ids["top_id"]][i]:
						print("退水配置超过上级，更新为与上级相同，id：{0}".format(ids["line2"][0]))
						result_retreating_data[ids["line2"][0]][i] = result_retreating_data[ids["top_id"]][i]
				# result_retreating_data[ids["line2"][0]] = self.add_amount_for_list(result_retreating_data[ids["line2"][0]],-amount)
				# break
				for j in range(0, len(ids["line2"]) - 1):
					for i in range(0, len(result_retreating_data[ids["line2"][j]])):
						if result_retreating_data[ids["line2"][j + 1]][i] > result_retreating_data[ids["line2"][j]][i]:
							print("退水配置超过上级，更新为与上级相同，id：{0}".format(ids["line2"][j + 1]))
							result_retreating_data[ids["line2"][j + 1]][i] = result_retreating_data[ids["line2"][j]][i]
				# result_retreating_data[ids["line2"][j+1]] = self.add_amount_for_list(result_retreating_data[ids["line2"][j+1]],-amount)
				# break
			
			
			# 影响全部层级，不等量增加
			elif change_type == "4/2":
				result_retreating_data[ids["line1"][0]] = self.add_amount_for_list(
					result_retreating_data[ids["line1"][0]], amount)
				for id in ids["line1"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["line1"][0]]]
				for id in ids["line2"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["line1"][0]]]
				for j in range(0, len(ids["line2"])):
					for i in range(0, len(result_retreating_data[ids["line2"][j]])):
						if result_retreating_data[ids["line2"][j]][i] < result_retreating_data[ids["members2"][j]][i]:
							result_retreating_data[ids["members2"][j]][i] = result_retreating_data[ids["line2"][j]][i]
			
			
			# 全部影响/等量增加
			elif change_type == "5/1":
				for id in ids["line1"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
				for id in ids["line2"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
				for id in ids["members1"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
				for id in ids["members2"]:
					result_retreating_data[id] = self.add_amount_for_list(result_retreating_data[id], amount)
				
				for i in range(0, len(result_retreating_data[ids["line2"][0]])):
					if result_retreating_data[ids["line2"][0]][i] > result_retreating_data[ids["top_id"]][i]:
						print("退水配置超过上级，更新为与上级相同，id：{0}".format(ids["line2"][0]))
						result_retreating_data[ids["line2"][0]][i] = result_retreating_data[ids["top_id"]][i]
				# result_retreating_data[ids["line2"][0]] = self.add_amount_for_list(result_retreating_data[ids["line2"][0]],-amount)
				# break
				for j in range(0, len(ids["line2"]) - 1):
					for i in range(0, len(result_retreating_data[ids["line2"][j]])):
						if result_retreating_data[ids["line2"][j + 1]][i] > result_retreating_data[ids["line2"][j]][i]:
							print("退水配置超过上级，更新为与上级相同，id：{0}".format(ids["line2"][j + 1]))
							result_retreating_data[ids["line2"][j + 1]][i] = result_retreating_data[ids["line2"][j]][i]
				# result_retreating_data[ids["line2"][j+1]] = self.add_amount_for_list(result_retreating_data[ids["line2"][j+1]],-amount)
				# break
				for j in range(0, len(ids["members2"])):
					for i in range(0, len(result_retreating_data[ids["members2"][j]])):
						if result_retreating_data[ids["members2"][j]][i] > result_retreating_data[ids["line2"][j]][i]:
							print("退水配置超过上级，更新为与上级相同，id：{0}".format(ids["members2"][j]))
							result_retreating_data[ids["members2"][j]][i] = result_retreating_data[ids["line2"][j]][i]
				# result_retreating_data[ids["members2"][j]] = self.add_amount_for_list(result_retreating_data[ids["members2"][j]],-amount)
				# break
			
			
			# 全部影响/不等量增加
			elif change_type in ("5/2"):
				result_retreating_data[ids["line1"][0]] = self.add_amount_for_list(
					result_retreating_data[ids["line1"][0]], amount)
				for id in ids["line1"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["line1"][0]]]
				for id in ids["line2"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["line1"][0]]]
				for id in ids["members1"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["line1"][0]]]
				for id in ids["members2"]:
					result_retreating_data[id] = [
						effected_value for effected_value in result_retreating_data[ids["line1"][0]]]
			
			else:
				print("错误的修改方式")
		return result_retreating_data
	
	def assert_dict_data(self, refer_data, object_data):
		'''
		比较两个字段中，相同key的value值是否相同
		:param refer_data:
		:param object_data:
		:return:
		'''
		
		mark = True
		for key in refer_data:
			if refer_data[key] != object_data[key]:
				print("用户id:%s 退水配置错误\nexpect:%s\nacturl:%s" % (key, str(refer_data[key]), str(object_data[key])))
				mark = False
		
		return mark
	
	def case(self, condition, channel, obj_id):
		'''

		:param condition: "1/1" "link_item/equal_add"
		:return:
		'''
		print("-------------condition:%s" % condition)
		interface_name = "admin_limit_quota_001"
		
		link_item = condition.split("/")[0]
		equal_add = condition.split("/")[1]
		
		# 获取修改前退水配置
		print("-------------获取修改前退水配置")
		origin_retreating_data = self.get_retreating_datas_from_db(self.ids, 220)
		
		# 修改退水
		print("-------------修改%d退水，add_amount=10" % obj_id)
		result_retreating_data = None
		if self.post(
				interface_name=interface_name, data_change=True, organization_id=obj_id, link_item=link_item,
				equal_add=equal_add, add_amount=10, lottery_id=6, setting_group_id=220, channel=channel):
			print("-------------获取修改后退水配置")
			result_retreating_data = self.get_retreating_datas_from_db(self.ids, 220)

		# 计算预期结果
		print("-------------计算退水预期结果")
		expect_retreating_data = self.calculate_retreating_datas(
			origin_retreating_data, condition, self.ids, obj_id, amount=10)

		# 断言实际结果与预期结果是否一致
		print("-------------断言实际结果与预期结果是否一致")
		rs = self.assert_dict_data(expect_retreating_data, result_retreating_data)
		return rs


ob = Retreat(user_type=1, id_mark="c", username="zy-gs01", password="6yhn6tfc")
print(ob.account,ob.ids)
print(ob.ids["line1"][0])