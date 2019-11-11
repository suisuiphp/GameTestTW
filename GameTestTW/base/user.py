#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

import json, requests
from utils.requestExcel.operationRequestExcel import OperationRequestExcel
from utils.operationTXT import OperationTxt
from utils.DBApi import DBApi
from utils.public import *
from base.variables import *
from copy import deepcopy
from utils.proportionExcel.opertionProportionExcel import OpertionProportionExcel


obj_excle = OperationRequestExcel()


class User():
	'''
	User实例化时会登录，首次登录会修改密码
	'''
	
	def __init__(self, user_type=1, **kwargs):
		'''
		按用户类型初始化
		:param user_type: 管理层级1，会员2
		'''
		self.excle = OperationRequestExcel()
		self.headers = {
			'Content-Type': "application/json",
			'cache-control': "no-cache",
			'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
		}
		
		if user_type == 1:
			self.url = getAdminUrl()
			self.account = getAdminAccount().split("/")[0]
			self.password = getAdminAccount().split("/")[1]

		else:
			self.url = getMemberUrl()
			self.account = getMemberAccount().split("/")[0]
			self.password = getMemberAccount().split("/")[1]
			
		if kwargs.get("username"):
			self.account = kwargs["username"]
			self.password = kwargs["password"]
		
		if kwargs.get("db"):
			self.db = kwargs["db"]
		else:
			self.db = getDb()
			
		self.login(user_type)
		# self.conn = DBApi(self.db)
		# self.ids = getIds()
		
	def post(self, interface_name, data_change=False,**kwargs):
		try:
			if data_change:
				# print("1----url:", self.url + self.excle.get_interface(interface_name))
				print("2----data:", self.set_data_by_key(interface_name,**kwargs))
				# print("3----headers:", self.headers)
				req = requests.post(
					url=self.url + self.excle.get_interface(interface_name),
					data=self.set_data_by_key(interface_name,**kwargs),
					headers=self.headers)
			else:
				req = requests.post(
					url=self.url + self.excle.get_interface(interface_name),
					data=self.excle.get_requestdata(interface_name),
					headers=self.headers)
			return req
		except Exception as e:
			print("*ERROR* %s:接口请求发生未知错误" % interface_name)
			print(repr(e))
	
	def get(self, interface_name, url_change=False, **kwargs):
		try:
			if url_change:
				print(self.url + self.set_url_by_key(interface_name, **kwargs))
				req = requests.get(
					url=self.url + self.set_url_by_key(interface_name, **kwargs),
					params=None,
					headers=self.headers)
			else:
				print(self.url + self.excle.get_interface(interface_name))
				req = requests.get(
					url=self.url + self.excle.get_interface(interface_name),
					params=None,
					headers=self.headers)
			return req
		except Exception as e:
			print(self.url + self.excle.get_interface(interface_name))
			print("*ERROR* %s:接口请求发生未知错误" % interface_name)
			print(repr(e))
			
	def login(self,user_type):
		
		if user_type == 1:
			interface_login="admin_login_001"
			interface_update_pwd = "admin_password_001"
		else:
			interface_login="member_login_001"
			interface_update_pwd = "member_password_001"
		r = self.post(interface_name=interface_login,data_change=True,account=self.account,password=self.password)
		try:
			self.headers["token"] = r.json()["token"]
		except Exception as e:
			print("*ERROR* " + repr(e) + r.content)
	
		# 验证是否首次登录,若不是，则更新密码未"6yhn6tfc'再登录
		if not r.json()['is_update_password']:
			# r_update = self.post(interface_name=interface_update_pwd,data_change=True,user_id=r.json()["user_id"])
			r_update = requests.put(
				url=self.url + self.excle.get_interface(interface_update_pwd),
				data=self.set_data_by_key(interface_update_pwd,user_id=r.json()["user_id"]),
				headers=self.headers)
			try:
				if r_update.content == "true":
					print("用户：%s，id：%d，密码修改成功" % (self.account,r.json()["user_id"]))
					self.password = "6yhn6tfc"
				else:
					print("--------------------------")
					print("用户：%s，id：%d，密码修改失败" % (self.account,r.json()["user_id"]))
					print(r_update.content)
			except Exception as e:
				print("*ERROR* " + repr(e) + r.content)
	
	def set_data_by_key(self, key, **kwargs):
		
		# 动态修改下单请求数据
		# 登录接口
		if key in("member_login_001","admin_login_001"):
			return self.__set_data_login_001(key,kwargs["account"],kwargs["password"])
		
		# 修改密码接口
		elif key in ("admin_password_001","member_password_001"):
			return self.__set_data_admin_password_001(key,kwargs["user_id"])
		
		#会员-下注接口
		elif key in ("member_bet_001", "member_bet_002", "member_bet_003", "member_bet_004"):
			return self.__set_data_member_bet_001(key, kwargs["lottery_id"])
		
		#管理-新增会员接口
		elif key == "admin_new_member_001":
			return self.__set_data_admin_new_member_001(
				key=key,
				organization_id=kwargs["organization_id"],
				account=kwargs["account"])
		
		#管理-修改占成接口
		elif key == "admin_update_proportion_001":
			return self.__set_data_admin_update_proportion_001(
				key=key,
				organization_id=kwargs["organization_id"],
				proportion_details=kwargs["proportion_details"],
				proportion_mode=kwargs["proportion_mode"])
			
		# 管理-修改初审限额/退水接口
		elif key == "admin_limit_quota_001":
			return self.__set_data_admin_limit_quota_001(
				organization_id=kwargs["organization_id"], link_item=kwargs["link_item"], equal_add=kwargs["equal_add"],
				add_amount=kwargs["add_amount"], lottery_id=kwargs["lottery_id"],
				setting_group_id=kwargs["setting_group_id"], channel=kwargs["channel"])
		
		#会员-自动下单接口
		elif key =="member_tw_auto_bet_001":
			return self.__set_data_member_tw_auto_bet_001(data=kwargs["data"])
		
		else:
			print("*ERROR* Wrong Key!!")
			
	def set_url_by_key(self, key, **kwargs):
		'''
		动态修改请求地址
		:param key:
		:param kwargs:
		:return:
		'''
		
		# 报表查询接口
		if key == "member_reports_001":
			return self.__set_url_member_reports_001(key, kwargs["lottery_id"])
		
		# 当前期数接口\上期开奖\获取赔率\最新订单
		elif key in (
				"member_period_infos_001",  # 当前期数接口
				"member_recently_number_001",  # 上期开奖
				"member_execution_odds_001",  # 获取赔率
				"member_orders_001",  # 最新订单
				"member_statistic_infos_001",  # 两面长龙
				"member_show_group_history_001"  # 冠亚和历史
		):
			return self.__set_url_by_lotteryId(key, kwargs["lottery_id"])

		
		# 报表明细查询接口
		elif key == "member_reports_retreating_001":
			return self.__set_url_member_reports_retreating_001(key, kwargs["lottery_id"], kwargs["date"])
		
		# 历史总帐查询接口
		elif key == "member_history_001":
			return self.__set_url_member_history_001(key, kwargs["start_time"], kwargs["end_time"])
		
		# 历史开奖查询接口
		elif key == "member_lottery_infos_001":
			return self.__set_url_member_lottery_infos_001(key, kwargs["created_at"], kwargs["lottery_id"])
		
		# 管理端-查询会员占成接口
		elif key == "admin_member_proportions_001":
			return self.__set_url_admin_member_proportions_001(key,kwargs["member_id"])
		
		# 管理端-修改用户页面获取组织信息接口
		elif key == "admin_update_company_sources_001":
			return self.__set_url_admin_update_company_sources_001(key,kwargs["organization_id"])
		
		else:
			print("*ERROR* Wrong Key!!")
	
	def create_proxy_all(self, user_mark=getAdminMark(), first_organization_id=1, file=data_dir("data","proxy_info.txt"), gs_tpye=1):
		'''
		创建所有层级代理包括(单个)：公司、分公司、大总监、总监、大股东、股东、总代理、一级代理、二级代理、三级代理
		需要读取
		:param user_mark 管理层级的账号标记 账号名称=固定+user_mark
		:param first_organization_id 创建第一个组织的直属上级id
		:param file: 用户信息文件包含account,max_member_count,cash_credits,self_highest_proportion
		:param  gs_tpye:1为独立调配，2为非独立调配
		:return:
		'''
		organization_id = first_organization_id
		
		fp = OperationTxt()
		user_info_list = fp.fileRead(file, "r")
		
		proxy_ids = []
		proxy_accounts = []
		
		for i in range(1, len(user_info_list)):
			proxy_info = user_info_list[i].split(",")
			account = proxy_info[0] + user_mark
			max_member_count = proxy_info[1]
			cash_credits = proxy_info[2]
			self_highest_proportion = proxy_info[3]
			data = {}
			data["organization_id"] = organization_id
			data["account_select"] = "myz102"
			data["account_input"] = account
			data["password"] = "6tfc6yhn"
			data["name"] = account
			data["max_member_count"] = max_member_count
			data["member_highest_credits"] = 0
			data["credit_mode"] = 1
			data["cash_credits"] = cash_credits
			data["handicaps"] = [1, 2, 3, 4, 5, 6]
			data["odds_diff_permission"] = "true"
			data["proportion_mode"] = 1
			if i == 1 and gs_tpye == 1:
				data["auto_recycle_permission"] = "true"  # true 自动盈利回收
				data["operate_permission"] = "true"  # true
				data["operate_restore_permission"] = "true"  # true
				data["open_system"] = "true"  # true开放公司系统
				data["independent_permission"] = "true"  # true独立调配
				data["online_manage"] = "true"  # true
			else:
				data["auto_recycle_permission"] = "false"  # true
				data["operate_permission"] = "false"  # true
				data["operate_restore_permission"] = "false"  # true
				data["open_system"] = "false"  # true开放公司系统
				data["independent_permission"] = "false"  # true独立调配
				data["online_manage"] = "false"  # true
			data["is_open_credits"] = "true"
			data["lotteries"] = [1, 3, 5, 6, 2, 7, 9, 10, 11]
			data["proportion_mode"] = 1
			
			
			
			data["proportion_details"] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
			
			data["proportion_details"][0]["lottery_id"] = BJSC  # 北京赛车
			data["proportion_details"][0]["self_highest_proportion"] = self_highest_proportion
			data["proportion_details"][0]["down_lowest_proportion"] = 0
			data["proportion_details"][0]["down_highest_proportion"] = 1
			
			data["proportion_details"][1]["lottery_id"] = JSSSC  # 极速时时彩
			data["proportion_details"][1]["self_highest_proportion"] = self_highest_proportion
			data["proportion_details"][1]["down_lowest_proportion"] = 0
			data["proportion_details"][1]["down_highest_proportion"] = 1
			
			data["proportion_details"][2]["lottery_id"] = XYNC  # 幸运农场
			data["proportion_details"][2]["self_highest_proportion"] = self_highest_proportion
			data["proportion_details"][2]["down_lowest_proportion"] = 0
			data["proportion_details"][2]["down_highest_proportion"] = 1
			
			data["proportion_details"][3]["lottery_id"] = JSSC  # 极速赛车
			data["proportion_details"][3]["self_highest_proportion"] = self_highest_proportion
			data["proportion_details"][3]["down_lowest_proportion"] = 0
			data["proportion_details"][3]["down_highest_proportion"] = 1
			
			data["proportion_details"][4]["lottery_id"] = XYFT  # 幸运飞艇
			data["proportion_details"][4]["self_highest_proportion"] = self_highest_proportion
			data["proportion_details"][4]["down_lowest_proportion"] = 0
			data["proportion_details"][4]["down_highest_proportion"] = 1
			
			data["proportion_details"][5]["lottery_id"] = CQHLSS  # 重庆欢乐生肖
			data["proportion_details"][5]["self_highest_proportion"] = self_highest_proportion
			data["proportion_details"][5]["down_lowest_proportion"] = 0
			data["proportion_details"][5]["down_highest_proportion"] = 1
			
			data["proportion_details"][6]["lottery_id"] = JSFT  # 极速飞艇
			data["proportion_details"][6]["self_highest_proportion"] = self_highest_proportion
			data["proportion_details"][6]["down_lowest_proportion"] = 0
			data["proportion_details"][6]["down_highest_proportion"] = 1
			
			data["proportion_details"][7]["lottery_id"] = GXKS  # 广西快三
			data["proportion_details"][7]["self_highest_proportion"] = self_highest_proportion
			data["proportion_details"][7]["down_lowest_proportion"] = 0
			data["proportion_details"][7]["down_highest_proportion"] = 1
			
			data["proportion_details"][8]["lottery_id"] = GDSYXW  # 广东十一选五
			data["proportion_details"][8]["self_highest_proportion"] = self_highest_proportion
			data["proportion_details"][8]["down_lowest_proportion"] = 0
			data["proportion_details"][8]["down_highest_proportion"] = 1
			
			data["credits"] = 0
			data["account"] = account
			data["receive_level"] = 2
			
			print(json.dumps(data))
			organization_id = self.create_user(json.dumps(data))
			proxy_ids.append(organization_id)
			proxy_accounts.append(account)
		# print([proxy_accounts,proxy_ids])
		return [proxy_accounts, proxy_ids]

	def create_user(self, user_data, type=1):
		'''
		创建用户，代理及会员
		:param user_data: 请求参数
		:param type: 用户类型，1表示代理，非1表示会员
		:param interface: 创建用户接口
		:return: 返回用户organization_id 或者 member_id
		'''

		try:
			if type == 1:
				url = self.url + self.excle.get_interface("admin_new_company_001")
				req = requests.post(url=url, headers=self.headers, data=user_data)
				organization_id = req.json()["organization_id"]
				return organization_id
			else:
				url = self.url + self.excle.get_interface("admin_new_member_001")
				req = requests.post(url=url, headers=self.headers, data=user_data)
				member_id = req.json()["member_id"]
				return member_id
		except Exception as e:
			print("*ERROR* 新增用户接口发生未知错误")
			print(repr(e))
			print(req.text)
			
	def create_members(self,organization_id,num=1,member_mark="zy"):
		'''
		给一个组织创建多个会员
		:param organization_id:
		:param num:
		:param member_mark:
		:return:
		'''
		accounts = []
		member_ids = []
		account = member_mark + str(organization_id) + '-'
		for i in range(1,num+1):
			account = account + str(i)
			r = self.post(
				interface_name="admin_new_member_001",
				data_change=True,
				organization_id=organization_id,
				account=account)
			accounts.append(account)
			try:
				r.json()["member_id"]
				member_ids.append(r.json()["member_id"])
			except:
				print("\n新增会员失败%s-----------------------------" % account)
				print(r.content)
		return [accounts,member_ids]
	
	def bet(self,interface="member_bet_001", lottery_id=6):
		'''下注-冠军大-极速赛车'''
		count = 0
		flag = False
		error_msg = []
		while count < 30:
			r = self.post(interface_name=interface, data_change=True, lottery_id=lottery_id)
			try:
				if r.json()["message"] == u"下单成功":
					flag = True
					break
				elif r.json()["message"] == u"已封盘，停止下注":
					error_msg.append(u"已封盘，停止下注")
					count += 1
					time.sleep(2)
					continue
				else:
					print(u"下单未知错误")
					error_msg.append(u"下单未知错误")
					error_msg.append(r.text)
					break
			except Exception as e:
				print(repr(e))
				error_msg.append(repr(e))
				break
		return flag, "\n".join(error_msg)

	def __set_data_login_001(self,key,account,password):
		req_data = json.loads(self.excle.get_requestdata(key))
		req_data["account"] = account
		req_data["password"] = password
		return json.dumps(req_data)
	
	def __set_data_member_bet_001(self, key, lottery_id=6):
		req_data = json.loads(self.excle.get_requestdata(key))
		# print("key:",key)
		# print("req_data:",req_data)
		r = self.get(interface_name="member_execution_odds_001", url_change=True, lottery_id=lottery_id)
		odds = json.loads(r.content)
		for item in req_data["details"]:
			for record in odds:
				if item["game_id"] == record["game_id"]:
					item["execution_odds"] = record["execution_odds"]
		return json.dumps(req_data)
	
	def __set_url_by_lotteryId(self,key,lottery_id):
		'''
		更新只需要变更彩种id的请求接口
		:param key:
		:param lottery_id:
		:return:
		'''
		interface = self.excle.get_interface(key)
		new_interface = interface.replace("lottery_id=6", "lottery_id=" + str(lottery_id))
		return new_interface
	
	# def __set_url_member_period_infos_001(self,key,lottery_id):
	# 	interface = self.excle.get_interface(key)
	# 	new_interface = interface.replace("lottery_id=6","lottery_id="+str(lottery_id))
	# 	return new_interface
	
	# def __set_url_member_recently_number_001(self,key,lottery_id):
	# 	interface = self.excle.get_interface(key)
	# 	new_interface = interface.replace("lottery_id=6", "lottery_id="+str(lottery_id))
	# 	return new_interface
	
	# def __set_url_member_execution_odds_001(self,key,lottery_id):
	# 	interface = self.excle.get_interface(key)
	# 	new_interface = interface.replace("lottery_id=6", "lottery_id=" + str(lottery_id))
	# 	return new_interface
	
	# def __set_url_member_orders_001(self,key,lottery_id):
	# 	interface = self.excle.get_interface(key)
	# 	new_interface = interface.replace("lottery_id=6", "lottery_id=" + str(lottery_id))
	# 	return new_interface
	
	# def __set_url_member_statistic_infos_001(self,key,lottery_id):
	# 	interface = self.excle.get_interface(key)
	# 	new_interface = interface.replace("lottery_id=6", "lottery_id=" + str(lottery_id))
	# 	return new_interface
	
	def __set_url_member_reports_001(self, key, lottery_id):
		interface = self.excle.get_interface(key)
		lottery_info = "lottery_id=" + str(lottery_id)
		new_interface = interface.split("?")[0] + "?" + lottery_info
		return new_interface
	
	def __set_url_member_reports_retreating_001(self, key, lottery_id, date):
		interface = self.excle.get_interface(key)
		new_interface = interface.replace("date=2019-07-21", "date=" + date)
		if lottery_id != None:
			new_interface = new_interface.replace("lottery_id=", "lottery_id=" + str(lottery_id))
		return new_interface
	
	def __set_url_member_history_001(self, key, start_time, end_time):
		interface = self.excle.get_interface(key)
		new_interface = interface.replace("start_time=2019-07-26", "start_time=" + start_time)
		new_interface = new_interface.replace("end_time=2019-07-26", "end_time=" + end_time)
		return new_interface
	
	def __set_url_member_lottery_infos_001(self,key,created_at, lottery_id):
		interface = self.excle.get_interface(key)
		new_interface = interface.replace(
			"lottery_id=6&created_at=2019-07-28",
			"lottery_id=" + str(lottery_id) +"&created_at=" + created_at)
		return new_interface
	
	def __set_data_member_tw_auto_bet_001(self,data):
		return json.dumps(data)
	
	def __set_data_admin_password_001(self,key,user_id):
		req_data = json.loads(self.excle.get_requestdata(key))
		req_data["user_id"] = user_id
		return json.dumps(req_data)
		
	def __set_data_admin_new_member_001(self,key,organization_id,account):
		req_data = json.loads(self.excle.get_requestdata(key))
		req_data["organization_id"] = organization_id
		req_data["account"] = account
		# req_data["name"] = account
		return json.dumps(req_data)
	
	def __set_data_admin_update_proportion_001(self,key,organization_id,proportion_details,proportion_mode):
		req_data = json.loads(self.excle.get_requestdata(key))
		req_data["organization_id"] = organization_id
		req_data["proportion_details"] = proportion_details
		req_data["proportion_mode"] = proportion_mode
		return json.dumps(req_data)
		
	def __set_url_admin_member_proportions_001(self,key,member_id):
		interface = self.excle.get_interface(key)
		new_interface = interface.replace("member_id=146","member_id="+str(member_id))
		return new_interface
	
	def __set_url_admin_update_company_sources_001(self,key,organization_id):
		interface = self.excle.get_interface(key)
		new_interface = interface.replace("organization_id=586","organization_id="+str(organization_id))
		return new_interface
	
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
			                                                            ' AND organization_id =' + str(
				id) + ' AND member_id IS NULL'
		elif usertype == 2:
			sql = 'SELECT a_proportion,b_proportion,c_proportion,d_proportion,e_proportion,f_proportion,single_highest_quota,single_lowest_quota,single_period_quota' \
			      ' FROM retreating_instances ' \
			      ' WHERE setting_group_id =' + str(setting_group_id) + '' \
			                                                            ' AND member_id =' + str(id)
		else:
			print("*ERROR*  Wrong usertype!")
			return
		
		retreating_data = self.conn.listDataBySQL(sql)
		list_retreating_data = [item for item in retreating_data[0]]
		# print(list_retreating_data)
		return list_retreating_data
	
	def __set_data_admin_limit_quota_001(
			self, organization_id, link_item, equal_add, add_amount=10, lottery_id=6, setting_group_id=220, channel=1):
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
		# print("-----start change retreat :%d" % organization_id)
		origin_data = self.get_retreating_data(id=organization_id, usertype=1, setting_group_id=setting_group_id)
		origin_a_proportion = float(origin_data[0])
		origin_b_proportion = float(origin_data[1])
		origin_c_proportion = float(origin_data[2])
		origin_d_proportion = float(origin_data[3])
		origin_e_proportion = float(origin_data[4])
		origin_f_proportion = float(origin_data[5])
		origin_single_highest_quota = float(origin_data[6])
		origin_single_lowest_quota = float(origin_data[7])
		origin_single_period_quota = float(origin_data[8])
		
		data = {}
		data["equal_add"] = equal_add
		data["link_item"] = link_item
		data["channel"] = channel
		data["setting_group_ids"] = [setting_group_id]
		data["organization_id"] = organization_id
		data["data"] = [{"lottery_id": 6,
		                 "in_data": [{
			                 "a_proportion": 32,
			                 "b_proportion": 32,
			                 "c_proportion": 42,
			                 "d_proportion": 52,
			                 "e_proportion": 62,
			                 "f_proportion": 72,
			                 "origin_a_proportion": "31.0",
			                 "origin_b_proportion": "30.0",
			                 "origin_c_proportion": "40.0",
			                 "origin_d_proportion": "50.0",
			                 "origin_e_proportion": "60.0",
			                 "origin_f_proportion": "70.0",
			                 "single_period_quota": 30612,
			                 "single_highest_quota": 36102,
			                 "single_lowest_quota": "2.0",
			                 "origin_single_period_quota": "30610.0",
			                 "origin_single_highest_quota": "36100.0",
			                 "origin_single_lowest_quota": "2.0",
			                 "setting_group_id": 220,
			                 "group": 1}]}]
		data["data"][0]["lottery_id"] = lottery_id
		data["data"][0]["in_data"][0]["a_proportion"] = origin_a_proportion + add_amount
		data["data"][0]["in_data"][0]["b_proportion"] = origin_b_proportion + add_amount
		data["data"][0]["in_data"][0]["c_proportion"] = origin_c_proportion + add_amount
		data["data"][0]["in_data"][0]["d_proportion"] = origin_d_proportion + add_amount
		data["data"][0]["in_data"][0]["e_proportion"] = origin_e_proportion + add_amount
		data["data"][0]["in_data"][0]["f_proportion"] = origin_f_proportion + add_amount
		data["data"][0]["in_data"][0]["single_period_quota"] = origin_single_period_quota + add_amount
		data["data"][0]["in_data"][0]["single_highest_quota"] = origin_single_highest_quota + add_amount
		data["data"][0]["in_data"][0]["single_lowest_quota"] = origin_single_lowest_quota + add_amount
		data["data"][0]["in_data"][0]["origin_a_proportion"] = origin_a_proportion
		data["data"][0]["in_data"][0]["origin_b_proportion"] = origin_b_proportion
		data["data"][0]["in_data"][0]["origin_c_proportion"] = origin_c_proportion
		data["data"][0]["in_data"][0]["origin_d_proportion"] = origin_d_proportion
		data["data"][0]["in_data"][0]["origin_e_proportion"] = origin_e_proportion
		data["data"][0]["in_data"][0]["origin_f_proportion"] = origin_f_proportion
		data["data"][0]["in_data"][0]["origin_single_period_quota"] = origin_single_period_quota
		data["data"][0]["in_data"][0]["origin_single_highest_quota"] = origin_single_highest_quota
		data["data"][0]["in_data"][0]["origin_single_lowest_quota"] = origin_single_lowest_quota
		data["data"][0]["in_data"][0]["setting_group_id"] = setting_group_id
		
		return json.dumps(data)
	
if __name__ == '__main__':
	req = User(user_type=1)
	pro = OpertionProportionExcel()
	proxys = [['zy-gs01p1', 'zy-fgs01p1', 'zy-dzj01p1', 'zy-zj01p1'], [674, 675, 676, 677]]
	
	# 新增会员
	members = [[], []]
	for id in proxys[1]:
		temp_members = req.create_members(id)
		members[0].extend(temp_members[0])
		members[1].extend(temp_members[1])
		break
	print(members)
