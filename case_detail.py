# -*-  conding: utf-8 -*-
# Author: xxx
# Datetime : 2020/12/18 15:58
# usage:电视剧类点播节目集详情页测试（铁道游击队）默认焦点在全屏按钮
import unittest
from autotesttv.test_method import TestMethod
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
import time
auto_setup(__file__)

TestCase = TestMethod()
# @unittest.skip()
class Casedetail(TestMethod):

    def test01_enterDeatil(self):
        '''点击进入详情页'''
        keyevent("KEYCODE_DPAD_CENTER")
        # time.sleep(3)
        # keyevent("KEYCODE_DPAD_RIGHT")
        TestCase.getImg()

    def test02_videoWindow(self):
        '''视频窗校验'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_player_image_bg",expString="tv.icntv.ott:id/details_player_image_bg")

    def test03_programSoure(self):
        '''视频窗节目集来源'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/lake_movie_sources",expString="tv.icntv.ott:id/lake_movie_sources")

    def test04_fullScreenTips(self):
        '''视频窗全屏操作提示'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/lake_tip_fullscreen",expString="按【ok】键全屏播放")

    def test05_programNavigation(self):
        '''节目集来源导航'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_top_path",expString="tv.icntv.ott:id/details_top_path")

    def test06_programTitle(self):
        '''节目集标题验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_right_title",expString="tv.icntv.ott:id/details_right_title")

    def test07_programScore(self):
        '''节目集评分验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_score",expString="tv.icntv.ott:id/details_score")

    def test08_programUpdate(self):
        '''节目集更新状态验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_play_time",expString="tv.icntv.ott:id/details_play_time")

    def test09_programPlayCount(self):
        '''节目集播放量验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_play_count_text",expString="tv.icntv.ott:id/details_play_count_text")

    def test10_programBitRate(self):
        '''码率验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_play_4k",expString="tv.icntv.ott:id/details_play_4k")

    def test11_ageTag(self):
        '''年代标签'''
        #年代标签
        TestCase.keepCmd(count=2,cmd="KEYCODE_DPAD_UP")
        TestCase.waitEle_assertion_index(element="android.widget.TextView",id=0,expString="android.widget.TextView")

    def test12_ageTagJump(self):
        '''年代标签跳转'''
        #年代标签
        keyevent("KEYCODE_DPAD_CENTER")
        time.sleep(3)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/head_text_view",expString="tv.icntv.ott:id/head_text_view")


    def test13_areaTag(self):
        '''地区标签'''
        keyevent("KEYCODE_BACK")
        TestCase.waitEle_assertion_index(element="android.widget.TextView", id=1, expString="android.widget.TextView")

    def test14_areaTagJump(self):
        '''地区标签跳转'''
        TestCase.direction_centerCmd("KEYCODE_DPAD_RIGHT")
        time.sleep(3)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/head_text_view",expString="tv.icntv.ott:id/head_text_view")

    def test15_typeTag(self):
        '''类型标签'''
        # 地区标签按钮
        keyevent("KEYCODE_BACK")
        time.sleep(1)
        TestCase.waitEle_assertion_index(element="android.widget.TextView", id=2, expString="android.widget.TextView")

    def test16_typeTagJump(self):
        '''类型标签跳转'''
        TestCase.direction_centerCmd("KEYCODE_DPAD_RIGHT")
        time.sleep(3)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/head_text_view", expString="tv.icntv.ott:id/head_text_view")

    def test17_programIntroduction(self):
        '''节目集简介'''
        # 第一个类型标签按钮
        keyevent("KEYCODE_BACK")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_brief",expString="tv.icntv.ott:id/details_brief")

    def test18_programIntroductionJump(self):
        '''节目介绍跳转'''
        #节目集简介页
        TestCase.direction_centerCmd("KEYCODE_DPAD_DOWN")
        time.sleep(2)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/brief_dialog_image",expString="tv.icntv.ott:id/brief_dialog_image")
        keyevent("KEYCODE_BACK")

    def test19_fullScreen(self):
        '''全屏按钮'''
        TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/details_block_item_top_text",id=0,expString="全屏")

    def test20_fullScreenJump(self):
        '''全屏按钮'''
        #全屏播放
        TestCase.direction_centerCmd("KEYCODE_DPAD_DOWN")
        TestCase.getImg()


    def test21_collection(self):
        '''收藏按钮'''
        #全屏按钮
        keyevent("KEYCODE_BACK")
        time.sleep(2)
        if poco(name="tv.icntv.ott:id/details_block_item_top_text")[1].get_text() == "收藏":
            TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/details_block_item_top_text", id=1,
                                             expString="收藏")
        else:
            TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/details_block_item_top_text", id=1,
                                             expString="已收藏")

    def test22_collectionClick(self):
        '''收藏按钮点击'''
        #收藏按钮
        TestCase.keepCmd(count=2,cmd="KEYCODE_DPAD_RIGHT")
        keyevent("KEYCODE_DPAD_CENTER")
        time.sleep(2)
        if poco(name="tv.icntv.ott:id/details_block_item_top_text")[1].get_text() == "收藏":
            TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/details_block_item_top_text", id=1,
                                             expString="收藏")
        else:
            TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/details_block_item_top_text", id=1,
                                             expString="已收藏")


    # def test23_purchase(self):
    #     '''购买按钮'''
    #     TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/details_block_item_top_text", id=1, expString="购买")
    #
    # def test24_purchaseJump(self):
    #     '''购买按钮跳转'''
    #

    def test25_marketingActivities(self):
        '''营销活动'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_btn_config_area_img",expString="tv.icntv.ott:id/details_btn_config_area_img")

    def test26_marketingActivitiesJump(self):
        '''营销活动跳转'''
        #营销活动页
        TestCase.direction_centerCmd("KEYCODE_DPAD_RIGHT")
        time.sleep(2)
        TestCase.getImg()

    def test27_programList(self):
        '''选集列表元素'''
        # 营销活动推荐位
        keyevent("KEYCODE_BACK")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/episode_title",expString="剧集列表")

    def test28_programDescribe(self):
        '''选集列表剧集描述'''
        keyevent("KEYCODE_DPAD_DOWN")
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/recommend_str_tv",expString="tv.icntv.ott:id/recommend_str_tv")

    def test29_listItem(self):
        '''列表单集海报推荐位元素校验'''
        TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/fall_item_card_img_new",id=0,expString="tv.icntv.ott:id/fall_item_card_img_new")

    def test30_listItemTitle(self):
        '''列表单集海报推荐位标题元素校验'''
        TestCase.waitEle_assertion_index(element="tv.icntv.ott:id/fall_item_card_bottom_desc_new", id=0, expString="tv.icntv.ott:id/fall_item_card_bottom_desc_new")

    def test31_listItemPlayIcon(self):
        '''列表单集海报推荐位正在播放播放Gif验证'''
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/fall_item_card_bottom_title_icon_new",expString="tv.icntv.ott:id/fall_item_card_bottom_title_icon_new")

    def test32_listCutSet(self):
        '''选集列表切集'''
        # 选集列表
        TestCase.direction_centerCmd("KEYCODE_DPAD_RIGHT")
        TestCase.getImg()
        # # 全屏播放呼出控制台
        # keyevent("KEYCODE_DPAD_RIGHT")
        # time.sleep(1)
        # TestCase.waitEle_assertion("tv.icntv.ott:id/lake_control_buttons_select","tv.icntv.ott:id/lake_control_buttons_select")

    def test33_listSortSwitch(self):
        '''列表分类切换'''
        #视频窗
        keyevent("KEYCODE_BACK")
        TestCase.keepCmd(count=2, cmd="KEYCODE_DPAD_DOWN")
        TestCase.keepCmd(count=2,cmd="KEYCODE_DPAD_RIGHT")
        TestCase.getImg()

    def test33_relevantRecommendations(self):
        '''相关推荐元素'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/details_bottom_title_name","相关推荐")

    def test34_floatingWindow(self):
        '''详情页悬浮窗'''
        keyevent("KEYCODE_DPAD_DOWN")
        TestCase.waitEle_assertion("tv.icntv.ott:id/detail_floating_video_container","正在播放")

    def test35_floatingWindowTitle(self):
        '''悬浮窗标题'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/detail_floating_title","tv.icntv.ott:id/detail_floating_title")

    def test36_floatingWindowScore(self):
        '''悬浮窗评分'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/detail_floating_grade_txt", "tv.icntv.ott:id/detail_floating_grade_txt")

    def test37_floatingWindowPlayCount(self):
        '''悬浮窗播放量'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/detail_floating_count_txt", "tv.icntv.ott:id/detail_floating_count_txt")

    def test38_floatingWindowBitRate(self):
        '''悬浮窗码率'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/detail_definition__txt", "tv.icntv.ott:id/detail_definition__txt")

    def test39_floatingWindowYearsTag(self):
        '''悬浮窗年代'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/detail_floating_time_txt", "tv.icntv.ott:id/detail_floating_time_txt")

    def test40_floatingWindowUpdate(self):
        '''悬浮窗更新状态'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/detail_floating_all_txt","tv.icntv.ott:id/detail_floating_all_txt")

    def test41_floatingWindowIntroduction(self):
        '''悬浮窗节目集简介'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/detail_floating_desc","tv.icntv.ott:id/detail_floating_desc")

    def test42_relevantRecommendationsJump(self):
        '''相关推荐跳转'''
        # 相关推荐第一张海报跳转详情页
        keyevent("KEYCODE_DPAD_CENTER")
        time.sleep(1)
        TestCase.waitEle_assertion(element="tv.icntv.ott:id/details_player_image_bg",expString="tv.icntv.ott:id/details_player_image_bg")

    def test43_relevantRecommenDationsFoucsSwitch(self):
        '''相关推荐焦点切换'''
        # 相关推荐第一张海报
        keyevent("KEYCODE_BACK")
        TestCase.keepCmd(5,"KEYCODE_DPAD_RIGHT")
        TestCase.getImg()

    def test44_relevantRecommenDationsTitle(self):
        '''相关推荐标题验证'''
        TestCase.keepCmd(5, "KEYCODE_DPAD_LEFT")
        TestCase.waitEle_assertion("tv.icntv.ott:id/item_details_bottom_text","tv.icntv.ott:id/item_details_bottom_text")

    def test45_relevantRecommenDationsScore(self):
        '''相关推荐评分验证'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/grade","tv.icntv.ott:id/grade")

    def test46_relatedStars(self):
        '''相关明星元素'''
        TestCase.keepCmd(2, "KEYCODE_DPAD_DOWN")
        TestCase.waitEle_assertion("tv.icntv.ott:id/details_person_title_name","相关明星")

    def test47_StarName(self):
        '''明星姓名校验'''
        TestCase.waitEle_assertion("tv.icntv.ott:id/details_person_item_name","tv.icntv.ott:id/details_person_item_name")

    def test48_StarClickJump(self):
        '''明星头像跳转'''
        TestCase.direction_centerCmd("KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion("tv.icntv.ott:id/id_name","tv.icntv.ott:id/id_name")

    def test49_backQuit(self):
        '''返回退出验证'''
        TestCase.keepCmd(2,"KEYCODE_BACK")
        TestCase.getImg()



    def test50_playOperationTips(self):
        '''全屏播放左下角操作提示验证'''
        # 全屏播放页
        keyevent("KEYCODE_DPAD_CENTER")
        time.sleep(1)
        keyevent("KEYCODE_DPAD_CENTER")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_tip_left_bottom_flip","tv.icntv.ott:id/lake_tip_left_bottom_flip")

    def test51_playController(self):
        '''播放器控制台验证'''
        # 呼出控制台
        keyevent("KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_control_seekbar","tv.icntv.ott:id/lake_control_seekbar")

    def test52_playTitle(self):
        '''全屏播放页右上角标题验证'''
        keyevent("KEYCODE_DPAD_LEFT")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_control_vod_tip_curent","tv.icntv.ott:id/lake_control_vod_tip_curent")

    def test53_playSeekForward(self):
        '''播放器快进操作'''
        TestCase.keepCmd(20,"KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion("tv.icntv.ott:id/live_time","tv.icntv.ott:id/live_time")

    def test54_playSeekFallBack(self):
        '''播放器快退操作'''
        TestCase.keepCmd(20, "KEYCODE_DPAD_LEFT")
        TestCase.waitEle_assertion("tv.icntv.ott:id/live_time", "tv.icntv.ott:id/live_time")

    def test55_playSelectedWorks(self):
        '''菜单键呼出选集列表'''
        keyevent("KEYCODE_MENU")
        TestCase.waitEle_assertion("tv.icntv.ott:id/vod_prog_rv","tv.icntv.ott:id/vod_prog_rv")

    def test56_playControllerSelectedWorks(self):
        '''控制台选集元素校验'''
        time.sleep(3)
        keyevent("KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_control_buttons_select","tv.icntv.ott:id/lake_control_buttons_select")

    def test57_playControllerSelectedWorksButton(self):
        '''控制台选集按钮呼出选集列表'''
        TestCase.direction_centerCmd("KEYCODE_DPAD_DOWN")
        TestCase.waitEle_assertion("tv.icntv.ott:id/vod_prog_rv", "tv.icntv.ott:id/vod_prog_rv")

    def test58_playControllerSelectedWorksSwitch(self):
        '''选集列表切集'''
        TestCase.direction_centerCmd("KEYCODE_DPAD_DOWN")
        time.sleep(4)
        # 呼出选集列表
        keyevent("KEYCODE_DPAD_DOWN")
        TestCase.waitEle_assertion("tv.icntv.ott:id/vod_prog_rv", "tv.icntv.ott:id/vod_prog_rv")

    def test59_playPause(self):
        '''播放器暂停校验'''
        time.sleep(3)
        keyevent("KEYCODE_DPAD_CENTER")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_control_buttons_playpause","tv.icntv.ott:id/lake_control_buttons_playpause")

    def test60_playContinuation(self):
        '''播放器继续播放'''
        keyevent("KEYCODE_DPAD_CENTER")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_control_buttons_playpause","tv.icntv.ott:id/lake_control_buttons_playpause")
        TestCase.getImg()

    def test61_playCollection(self):
        '''收藏验证'''
        keyevent("KEYCODE_DPAD_RIGHT")
        keyevent("KEYCODE_DPAD_DOWN")
        TestCase.keepCmd(2,"KEYCODE_DPAD_RIGHT")
        # 收藏按钮
        keyevent("KEYCODE_DPAD_CENTER")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_control_buttons_collect","tv.icntv.ott:id/lake_control_buttons_collect")

    def test62_playRecommendProgram(self):
        '''收视推荐校验'''
        keyevent("KEYCODE_DPAD_DOWN")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_recommend_root_text","收视推荐")

    def test63_playRecommendProgramFocusSwitch(self):
        '''收视推荐焦点切换'''
        TestCase.keepCmd(5,"KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_recommend_root_text","收视推荐")

    def test64_playRecommendProgramJump(self):
        '''收视推荐校验'''
        keyevent("KEYCODE_DPAD_CENTER")
        time.sleep(2)
        keyevent("KEYCODE_DPAD_RIGHT")
        TestCase.waitEle_assertion("tv.icntv.ott:id/lake_control_vod_tip_curent","tv.icntv.ott:id/lake_control_vod_tip_curent")

    def test65_playLastSet(self):
        '''返回校验'''
        keyevent("KEYCODE_BACK")
        keyevent("KEYCODE_BACK")
        TestCase.getImg()

    """
    SEEK自动切集
    收视推荐
    从头播放
    退出
    购买
    
    """