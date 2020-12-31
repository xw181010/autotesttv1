# -*-  conding: utf-8 -*-
# Author: xxx
# Datetime : 2020/12/22 11:26
# usage:
import unittest
from autotesttv.test_method import TestMethod
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
import time
auto_setup(__file__)
#
# TestCase = TestMethod()
# class Test(TestMethod):
#     def ww(self):
#         aa = poco("android.widget.TextView")[0].get_text()
#         # self.assertIsNotNone(aa,msg="ddd")
#         # TestCase.waitEle_assertion_index_NotNone(element="android.widget.TextView", id=0)
#         assert_equal(aa,aa,)

# print(poco("android.widget.TextView")[0].get_text())

for i in range(1000):
    # os.system(r"adb shell input keyevent KEYCODE_MEDIA_FAST_FORWARD")
    os.system(r"adb shell input keyevent KEYCODE_DPAD_RIGHT")
    print(i)