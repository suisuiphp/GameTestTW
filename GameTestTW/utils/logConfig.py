#!/usr/bin/env python
# coding:utf-8

# Author:TiFity

import logging,sys
from utils.public import *

# 声明一个logger对象
logger = logging.getLogger(__name__)

# 定义日志等级
logger.setLevel(level=logging.DEBUG)

# 声明一个handler
handler = logging.FileHandler(data_dir("data/logInfo", "log.md"), "a")

# 设置handler的格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# 将handler添加到logger里面
logger.addHandler(handler)

