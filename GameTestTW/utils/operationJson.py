#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

import json
from utils.public import *

class OperationJson(object):
	def readAllJsonData(self,filename):
		with open(filename,"r") as f:
			jsonData = json.load(f)
		return jsonData
		
	def getJsonDataByKey(self,filename,key):
		with open(filename,"r") as f:
			jsonData = json.load(f)
			
		return jsonData.get(key,"not found value by {0}".format(key))

		
			
if __name__ == '__main__':
    obj = OperationJson()
    print(obj.readAllJsonData(data_dir("data","requestData.json")))
    data = {"name": "zhuoyan"}

