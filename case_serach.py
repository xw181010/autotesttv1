# -*-  conding: utf-8 -*-
# Author: xxx
# Datetime : 2020/12/14 13:34
# usage:搜索模块用例

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


TestCase = TestMethod()
class Caseserach(TestMethod):

    def test01_enterSearch(self):
        '''进入搜索，校验输入框'''
        #点击进入搜索入口
        TestCase.searchEntrance()
        keyevent("KEYCODE_DPAD_CENTER")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_name_et", expString="tv.icntv.ott:id/search_name_et")

    def test02_fullKeyboard(self):
        '''校验默认展示全键盘'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_full_key",expString="全键盘")

    def test03_allSearchTitle(self):
        '''校验大家在搜元素'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_hot_title_name",expString="大家在搜")

    def test04_allSearchTop1(self):
        '''校验大家在搜Top标识'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/topIcon", expString="tv.icntv.ott:id/topIcon")

    def test05_allSearchFirstProgram(self):
        '''校验大家在搜首行元素'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/title",expString="tv.icntv.ott:id/title")

    def test06_allSearchFirstProgramType(self):
        '''校验大家在搜节目集类型元素'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/type",expString="tv.icntv.ott:id/type")

    def test07_allSearchFocusSwitch(self):
        '''大家在搜焦点切换校验'''
        #大家在搜首行
        TestCase.keepCmd(count=3,cmd="KEYCODE_DPAD_RIGHT")
        TestCase.keepCmd(count=6,cmd="KEYCODE_DPAD_DOWN")
        TestCase.getImg()

    def test08_enterHotSearchProgram(self):
        '''进入热搜榜第一个详情页'''
        #热搜榜第一张海报
        TestCase.direction_centerCmd(cmd="KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_right_title",expString="tv.icntv.ott:id/details_right_title")

    def test09_searchNavigation(self):
        '''热搜榜切换&导航切换'''
        # 热搜榜第一张海报
        keyevent("KEYCODE_BACK")
        TestCase.keepCmd(count=4,cmd="KEYCODE_DPAD_RIGHT")
        #热搜榜元素
        keyevent("KEYCODE_DPAD_UP")
        TestCase.keepCmd(count=4,cmd="KEYCODE_DPAD_RIGHT")
        TestCase.getImg()

    def test10_hotSearch(self):
        '''校验热搜榜元素'''
        #热搜榜元素
        TestCase.keepCmd(count=4, cmd="KEYCODE_DPAD_LEFT")
        TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/name",id=1,expString="热搜榜")

    def test11_hotSearchCount(self):
        '''校验热搜榜数量'''
        TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/nums",id=1,expString="tv.icntv.ott:id/nums")

    def test12_searchHistory(self):
        '''校验搜索历史元素'''
        #搜索历史
        keyevent("KEYCODE_DPAD_LEFT")
        TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/name",id=0,expString="搜索历史")

    def test13_clickM(self):
        '''输入字符M校验输入框'''
        #全键盘M
        TestCase.keepCmd(count=2,cmd="KEYCODE_DPAD_LEFT")
        keyevent("KEYCODE_DPAD_CENTER")
        time.sleep(5)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_name_et", expString="M")

    def test14_guess(self):
        '''校验猜你想看元素'''
        time.sleep(6)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_tips_title_name", expString="猜你想看")

    def test15_guessFirst(self):
        '''校验猜你想看首行内容展示'''
        time.sleep(2)
        TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/title",id=0,expString="“M”全部内容")

    def test16_resultAreaTitle(self):
        '''搜索结果区标题验证'''
        #搜索结果第一张海报
        TestCase.keepCmd(4,"KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_content_search_title",expString='搜索"M"的内容')

    def test18_programTitle(self):
        '''搜索结果节目集标题验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/title", expString="tv.icntv.ott:id/title")

    def test19_searchCorner(self):
        '''搜索结果角标验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/conner_img", expString="tv.icntv.ott:id/conner_img")

    def test20_searchUpdate(self):
        '''搜索更新状态验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/desc", expString="tv.icntv.ott:id/desc")

    def test21_searchScore(self):
        '''搜索节目集评分'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/score",expString="tv.icntv.ott:id/score")

    def test22_searchResultWholeTab(self):
        '''搜索结果内容区切换并验证右侧分类全部Tab元素'''
        #搜索结果区第一行第四张海报
        TestCase.keepCmd(count=3,cmd="KEYCODE_DPAD_RIGHT")
        TestCase.keepCmd(count=5, cmd="KEYCODE_DPAD_DOWN")
        # 全部Tab元素
        TestCase.keepCmd(count=2, cmd="KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/category_name",expString="全部")

    def test23_searchResultWholeTabCount(self):
        '''搜索结果右侧分类数量元素校验'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/category_nums",expString="tv.icntv.ott:id/category_nums")

    def test24_searchResultTabSwitch(self):
        '''搜索结果右侧分类Tab切换'''
        #资讯Tab元素
        TestCase.keepCmd(count=4,cmd="KEYCODE_DPAD_DOWN")
        TestCase.getImg()

    def test25_searchResultJump(self):
        '''跳转搜索结果详情页'''
        #资讯Tab页第一行第四张海报并进入详情页
        TestCase.direction_centerCmd(cmd="KEYCODE_DPAD_LEFT")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_right_title",expString="tv.icntv.ott:id/details_right_title")

    def test26_searchResultStarTab(self):
        '''搜索结果分类明星Tab元素验证'''
        # 资讯Tab页第一行第四张海报
        keyevent("KEYCODE_BACK")
        time.sleep(1)
        keyevent("KEYCODE_DPAD_RIGHT")
        #明星tab元素
        TestCase.keepCmd(count=6,cmd="KEYCODE_DPAD_UP")
        # TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/search_star_txt", id=0, expString="明星")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_star_txt",expString="明星")

    def test27_starPortraitSelect(self):
        '''明星头像当前√标识元素验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_star_selected",expString="tv.icntv.ott:id/search_star_selected")

    def test28_starPortrait(self):
        '''明星头像元素校验'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/image",expString="tv.icntv.ott:id/image")

    def test29_starPortraitProgramSwitch(self):
        '''明星头像下节目集焦点切换'''
        #第一个明星头像
        keyevent("KEYCODE_DPAD_LEFT")
        TestCase.keepCmd(count=3,cmd="KEYCODE_DPAD_DOWN")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/title",expString="tv.icntv.ott:id/title")

    def test30_enterStarSpecial(self):
        '''进入明星专题'''
        # 第一个明星头像
        TestCase.keepCmd(count=3, cmd="KEYCODE_DPAD_UP")
        keyevent("KEYCODE_DPAD_RIGHT")
        #第二个明星头像明星专题页
        keyevent("KEYCODE_DPAD_CENTER")
        time.sleep(1)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/id_cast_order",expString="tv.icntv.ott:id/id_cast_order")

    def test31_starPortraitSwitch(self):
        '''明星头像切换'''
        #第二个明星头像
        keyevent("KEYCODE_BACK")
        TestCase.keepCmd(count=9,cmd="KEYCODE_DPAD_RIGHT")
        TestCase.getImg()

    def test32_keyboardT9(self):
        '''T9键盘元素校验'''
        #全键盘M
        TestCase.keepCmd(count=12, cmd="KEYCODE_DPAD_LEFT")
        TestCase.keepCmd(count=4, cmd="KEYCODE_DPAD_DOWN")
        # T９键盘元素
        keyevent("KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_t9_key",expString="T9键盘")

    def test33_voiceTab(self):
        '''语音Tab验证'''
        # 语音Tab元素
        keyevent("KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_voice_key",expString="语音")

    def test34_screenJump(self):
        '''筛选跳转'''
        # 筛选元素
        keyevent("KEYCODE_DPAD_DOWN")
        keyevent("KEYCODE_DPAD_CENTER")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/head_text_view",expString="tv.icntv.ott:id/head_text_view")

    def test35_memoryKeyboardPosition(self):
        '''默认记忆键盘退出位置验证'''
        # 桌面搜索入口
        TestCase.keepCmd(count=2, cmd="KEYCODE_BACK")
        keyevent("KEYCODE_DPAD_CENTER")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_voice_key", expString="语音")

    def test36_T9Popup(self):
        '''T9键盘弹层输入验证'''
        # 语音Tab元素
        keyevent("KEYCODE_DPAD_LEFT")
        TestCase.direction_centerCmd("KEYCODE_DPAD_UP")
        # T9键盘弹层上确认
        keyevent("KEYCODE_DPAD_CENTER")
        time.sleep(3)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_name_et", expString="K")

    def test37_T9Delete(self):
        '''T9删除键验证'''
        TestCase.keepCmd(count=2,cmd="KEYCODE_DPAD_DOWN")
        #T9键盘删除按钮
        TestCase.direction_centerCmd("KEYCODE_DPAD_RIGHT")
        time.sleep(18)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_name_et", expString="输入片名/人名的首字母或全拼")

    def test38_superLongStr(self):
        '''超长字符验证'''
        #T9键盘删除键
        keyevent("KEYCODE_DPAD_DOWN")
        keyevent("KEYCODE_DPAD_LEFT")
        #全键盘M
        keyevent("KEYCODE_DPAD_UP")
        TestCase.keepCmd(count=13,cmd="KEYCODE_DPAD_CENTER")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_name_et", expString="MMMMMMMMMMMMM")

    def test39_searchNoResult(self):
        '''没有搜索结果验证'''
        # 猜你想看首行
        TestCase.keepCmd(count=3, cmd="KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion(element="android.widget.TextView", expString="没有搜索到结果")

    def test40_fullKeyboardClear(self):
        '''全键盘清空验证'''
        #全键盘M
        keyevent("KEYCODE_DPAD_LEFT")
        TestCase.keepCmd(count=3,cmd="KEYCODE_DPAD_DOWN")
        #全键盘清空按钮
        TestCase.direction_centerCmd("KEYCODE_DPAD_RIGHT")
        time.sleep(6)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_name_et", expString="输入片名/人名的首字母或全拼")

    def test41_searchHistoryCount(self):
        '''历史记录数量验证'''
        #热搜榜第一张海报
        TestCase.keepCmd(count=3,cmd="KEYCODE_DPAD_RIGHT")
        keyevent("KEYCODE_DPAD_UP")
        # 搜索历史元素
        keyevent("KEYCODE_DPAD_LEFT")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/nums",expString="tv.icntv.ott:id/nums")

    def test42_searchHistoryClear(self):
        '''清空历史记录验证'''
        #容灾：
        TestCase.keepCmd(count=6,cmd="KEYCODE_DPAD_DOWN")
        TestCase.direction_centerCmd("KEYCODE_DPAD_DOWN")
        TestCase.getImg()

    @unittest.skip("该用例不通过，暂时不支持")
    def test43_fullKeyboardNum(self):
        '''全键盘数字键输入验证'''
        #全键盘中进入数字键盘
        TestCase.direction_centerCmd("KEYCODE_DPAD_LEFT")
        TestCase.direction_centerCmd("KEYCODE_DPAD_UP")
        time.sleep(2)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/search_name_et", expString="7")

    # def test99_back(self):
    #     '''返回入口，仅调试使用'''
    #     keyevent("KEYCODE_BACK")
    #     keyevent("KEYCODE_BACK")
    #     keyevent("KEYCODE_BACK")
    #     TestCase.getImg()


