"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/17 20:51
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
import unittest
from testcases import LoginTest
from HTMLTestRunnerNew import HTMLTestRunner
from readexcel import ReadExcel

# 第一步：创建测试套件
suite=unittest.TestSuite()
# 读取表单中所有数据
excel = ReadExcel('case.xlsx', 'login')
cases=excel.read_data()
for i in cases:
    case = LoginTest('test_login',eval(i['data']),eval(i['expect']))
    suite.addTest(case)

# 第三步：创建一个测试运行启动器
runner=HTMLTestRunner(
    stream=open('report.html','wb'),
    title='测试登录用例',
    description='第二次使用unittest单元测试框架测试登录用例',
    tester='小磊')
# 使用启动器执行测试套件
runner.run(suite)

