# _*_ coding: utf-8 _*_
import pymysql
import sys
# sys.setdefaultencoding('utf-8')
from unittest import TestCase


class DBApi():
	# "oracle,pdwdata_uat/123456@10.20.112.123:1521/pdw"
	def __init__(self, db):
		self.dbtype = db.split(",")[0]
		self.db = db.split(",")[1]
		if self.dbtype.lower() not in ("mysql", "oracle"):
			print("*ERROR* Database %s type can only be oracle and mysql" % self.db)
	
	def DB_connect(self):
		'''
		连接数据库,连接成功返回连接，否则退出程序
		'''
		if self.dbtype == "oracle":
			# connect = cx_Oracle.connect(self.db)
			pass
		if self.dbtype == "mysql":
			conn = None
			cur = None
			dbuser = self.db.split("/")[0]
			dbpasswd = self.db.split("/")[1].split("@")[0]
			dbhost = self.db.split("@")[1].split(":")[0]
			dbport = int(self.db.split(":")[1].split("/")[0])
			dbdatabase = self.db.split("/")[2]
			
			try:
				conn = pymysql.connect(user=dbuser, password=dbpasswd, host=dbhost, port=dbport, db=dbdatabase,
				                       charset="utf8")
				cur = conn.cursor()
			except Exception as e:
				print("*ERROR*" + repr(e))
		return conn, cur
	
	def DB_close(self, connection, cursor):
		'''
		断开数据库连接
		:param connection: 数据库连接，cursor：游标
		:return:
		'''
		try:
			if cursor != None:
				cursor.close()
			if connection != None:
				connection.close()
		except Exception as e:
			print("*ERROR*" + repr(e))
	
	def listDataBySQL(self, str_sql):
		'''
		获取所有查询结果
		:param str_sql: var Str_sql
		:return: 返回List列表，列表中的元素为TUPLE类型
		'''
		conn, cur = self.DB_connect()
		list_rs = []
		try:
			cur.execute(str_sql)
			list_rs = cur.fetchall()
		except Exception as e:
			print("*ERROR* ", repr(e))
		finally:
			self.DB_close(conn, cur)
		return list_rs
	
	def insertData(self, str_sql, params, isSingle=True):
		'''
		插入数据
		:param str_sql:"INSERT INTO user(telephone,username,password) VALUES (%s,%s,%s)"
		:param params: [("18101111112", "zy2", "123456"), ("18101111113", "zy3", "123456")]
		:param isSingle:True插入单条，False插入多条
		:return:
		'''
		
		conn, cur = self.DB_connect()
		try:
			if isSingle:
				cur.execute(str_sql, params)
				conn.commit()
			else:
				cur.executemany(str_sql, params)
				conn.commit()
		except Exception as e:
			print("*ERROR* ", repr(e))
		finally:
			self.DB_close(conn, cur)
	
	def deleteData(self, str_sql, params):
		'''
		删除数据
		:param str_sql:"delete from  user where username=%s"
		:param params: ("zy2",),注意参数必须是元祖，一个元素的元祖有逗号
		:return:
		'''
		
		conn, cur = self.DB_connect()
		try:
			cur.execute(str_sql, params)
			conn.commit()
		except Exception as e:
			print("*ERROR* ", repr(e))
		finally:
			self.DB_close(conn, cur)


if __name__ == '__main__':
	db = DBApi("mysql,root/123456@127.0.0.1:3306/db_flask")
	sql = "delete from user where username=%s"
	params = ("zy2",)
	db.deleteData(sql,params)
