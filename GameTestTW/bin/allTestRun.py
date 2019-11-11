#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

import unittest
import os, sys, time
import HTMLTestRunner
from utils.public import *

reload(sys)
sys.setdefaultencoding('utf-8')


def allTest():
	dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"tests")

	suite = unittest.TestLoader().discover(start_dir=dir_path, pattern="test_member.py", top_level_dir=None)
	return suite


def run():
	fp = data_dir("tests/testReport",getNowTime()+"testReport.html")
	HTMLTestRunner.HTMLTestRunner(stream=open(fp, "wb"), title="GameTW_TestReport").run(allTest())


if __name__ == '__main__':
	run()
