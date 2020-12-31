# -*-  conding: utf-8 -*-
# Author: xxx
# Datetime : 2020/12/14 10:05
# usage:被调用的函数类
import unittest
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import os
import time
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
auto_setup(__file__)

# logging.info()

class TestMethod(unittest.TestCase):
    nowtime = time.strftime('%Y%m%d_%H.%M.%S', time.localtime())
    # 以二进制模式打开一个文件
    f = open(os.getcwd() + "/" + nowtime + "report.html", 'wb')

    def setUp(self):
        '''每条测试用例之前'''
        print("\n测试准备")

    def tearDown(self):
        '''每条测试用例之后'''
        print("\n测试结束")

    @classmethod
    def setUpClass(cls):
        '''每个类执行之前'''
        print("类前执行")

    @classmethod
    def tearDownClass(cls):
        '''每个类执行之后'''
        # keyevent("KEYCODE_HOME")
        print("类后执行")

    def keepCmd(self,count,cmd):
        '''
        连续点击事件
        :param cmd:keycode值 count：次数
        :return:
        '''
        i = 0
        while i < count:
            keyevent(cmd)
            i += 1

    def direction_centerCmd(self,cmd):
        '''
        点击一次方向键并点击确认键
        :param cmd:keycode值
        :return:
        '''
        keyevent(cmd)
        keyevent("KEYCODE_DPAD_CENTER")


    def getImg(self):
        imgPath = r"D:\SOFTWARE_DATA\PycharmProject\PycharmProjects\untitled\autotesttv\img\\"
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath1 = os.path.join(imgPath, '%s.png' % str(timestrmap))
        snapshot(filename=imgPath1, msg="111")
        print('screenshot:',timestrmap, '.png')

    def waitEle_assertion(self,element,expString):
        '''
        等待元素，判断元素是否存在并断言
        :param element: 元素
        :param expString: 期望的断言结果值
        :return:
        '''
        try:
            poco(element).wait_for_appearance(timeout=8)
        except:
            # print("元素未找到")
            self.assertTrue(False, "元素未找到")
        try:
            self.assertTrue((poco(element).get_text()==expString or poco(element).get_name()==expString or (poco(element).attr("resourceId")==expString)),"断言失败")
            logger.debug(poco(element).get_text())
            logger.debug(poco(element).get_name())
            logger.debug(poco(element).attr("resourceId"))
            self.getImg()
            return True
        except:
            self.getImg()
            # print("断言失败")
            self.assertTrue(False,"断言失败111111")
            self.getImg()
            return False


    def waitEle_assertion_index(self, element,id,expString):
        '''
        等待元素，判断元素是否存在并断言
        :param element: 元素  id：索引
        :param expString: 期望的断言结果值
        :return:
        '''
        try:
            poco(element)[id].wait_for_appearance(timeout=8)
        except:
            # print("元素未找到")
            self.assertTrue(False, "元素未找到")
        try:
            self.assertTrue((poco(element)[id].get_text() == expString or poco(element)[id].get_name() == expString or (
            poco(element)[id].attr("resourceId") == expString)), "断言失败")
            self.getImg()
            return True
        except:
            self.getImg()
            # print("断言失败")
            self.assertTrue(False, "断言失败")
            return False



    def searchEntrance(self):
        '''搜索入口'''
        keyevent("KEYCODE_DPAD_UP")
        self.keepCmd(count=4,cmd="KEYCODE_DPAD_RIGHT")
        keyevent("KEYCODE_DPAD_LEFT")

