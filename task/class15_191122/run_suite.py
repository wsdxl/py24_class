"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/23 17:22
E-mail  : 506615839@qq.com
File    : run_suite.py
============================
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
import testcases

# 第一步：新建测试套件
suite=unittest.TestSuite()
# 第二步：加载测试用例到测试套件
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))
# 第三步：新建测试用例启动器
runner=HTMLTestRunner(stream=open('report.html','wb'),
                      title='测试注册和登录功能测试报告',
                      description='使用unittest框架测试注册和登录功能测试报告',
                      tester='小磊同学'
                      )
# 第四步：运行用例启动器
runner.run(suite)