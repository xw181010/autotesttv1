# -*-  conding: utf-8 -*-
# Author: xxx
# Datetime : 2020/12/14 10:04
# usage:测试用例执行控制

import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import logging
from autotesttv.case_serach import Caseserach
from autotesttv.case_detail import Casedetail
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



if __name__ == '__main__':
    print("===================================用例执行开始===================================")
    suite = unittest.TestSuite()
    # 把写的用例加进来（将Casetest类加进来）,执行一个类
    # suite.addTest(unittest.makeSuite(Caseserach))
    suite.addTest(unittest.makeSuite(Casedetail))
    #只执行Casetest类下的一条用例
    # suite.addTest(Casetest("test_01aaa"))
    #不添加测试报告运行命令
    #unittest.main(defaultTest='suite')
    nowtime = time.strftime('%Y%m%d_%H.%M.%S',time.localtime())
    # 以二进制模式打开一个文件
    f = open(os.getcwd()+"/"+nowtime+"report.html", 'wb')
    runner = HTMLTestRunner(f, title='TV端自动化测试报告', description='用例执行结果详情')
    # 运行用例（用例集合)
    runner.run(suite)
    logger.debug(suite)

