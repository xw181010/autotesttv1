# -*-  conding: utf-8 -*-
# Author: xxx
# Datetime : 2020/12/14 10:04
# usage:测试case

import unittest
# from autotesttv.test_method import TestMethod
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
import os
import time
auto_setup(__file__)


#
# @unittest.skip("练习模块，暂不测试")
# class Casetest(TestMethod):
#
#     def test_01aaa(self):
#         '''Case第一条'''
#         print("第一条Case")
#         TestMethod.keepCmd(4,"KEYCODE_DPAD_RIGHT")
#
#
#     def test_02bbb(self):
#         print("第二条Case")

