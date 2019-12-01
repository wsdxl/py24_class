"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/15 23:08
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
import unittest
from testcases import RegisterTestCase,LoginTest
from HTMLTestRunnerNew import HTMLTestRunner
from readexcel import ReadExcel

# 第一步:创建测试套件
suite=unittest.TestSuite()
# 第二步：将测试用例加载到测试套件中
# 读取表单中所有数据
excel = ReadExcel('case.xlsx', 'login')
cases=excel.readdata()
for i in cases:
    case = LoginTest('test_login',eval(i['data']),eval(i['expect']),i['case_id'])
    suite.addTest(case)

excel=ReadExcel('case.xlsx','register')
datas=excel.readdata()
for i in datas:
    # 创建一个对象
    # 通过通过用例类创建对象，需要传入用例方法名（字符串）
    case = RegisterTestCase('test_register', eval(i['data']), eval(i['expected']),i['case_id'])
    suite.addTest(case)


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
