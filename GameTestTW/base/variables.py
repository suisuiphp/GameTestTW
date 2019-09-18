#!/usr/bin/env python
# coding:utf-8

# Author:TiFity
class Variables:
	url_admin = "http://admin.win2019.cc"
	url_member = "http://member.win2019.cc"
	db = "mysql,root/123456@192.168.1.10:30827/game_api_stage_tw"
	
	admin_account = "sub01/6yhn6tfc"
	member_account = "zy830-1/6yhn6tfc"
	
	admin_mark = "19"
	member_mark = "zy"
	
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