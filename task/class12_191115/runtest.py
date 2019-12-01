"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/15 23:08
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
import unittest
import testcases
from HTMLTestRunnerNew import HTMLTestRunner
# 第一步:创建测试套件
suite=unittest.TestSuite()
# 第二步：将测试用例加载到测试套件中
# 第1种：通过模块去加载用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))
#第2种：通过测试用例类去加载
# suite.addTest(loader.loadTestsFromTestCase(testcases.RegisterTestCase))
# # # 第3种：添加单条测试用例
# from testcases import RegisterTestCase
# # 创建一个对象
# # 通过通过用例类创建对象，需要传入用例方法名（字符串）
# case=RegisterTestCase('test_register_pass')
# suite.addTest(case)
# 第三步：创建一个测试运行启动器
# runner=unittest.TextTestRunner()
runner= HTMLTestRunner(
    stream=open('report.html',mode='wb'),
    title='第一个单元测试报告',
    description='python24期第一个测试报告',
    tester='小磊'
)
# 第四步：使用启动器去执行测试套件
runner.run(suite)
