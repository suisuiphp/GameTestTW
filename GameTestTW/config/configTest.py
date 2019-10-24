#!/usr/bin/env python
#coding:utf-8

#Author:TiFity

import ConfigParser
import os

config_file = os.path.join(os.path.dirname(__file__),"config.ini")
conf = ConfigParser.ConfigParser()
print(conf.read(config_file))

sections = conf.sections()
print('获取配置文件所有的section', sections)

options = conf.options('mysql')
print('获取指定section下所有option', options)


items = conf.items('mysql')
print('获取指定section下所有的键值对', items)


value = conf.get('mysql', 'host')
print('获取指定的section下的option', type(value), value)
