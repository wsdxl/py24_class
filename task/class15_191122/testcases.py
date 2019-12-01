"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/23 17:17
E-mail  : 506615839@qq.com
File    : testcases.py
============================
"""
import unittest
from ddt import ddt,data
from read_excel import ReadExcel
from login import login_check
from registerfunc import register
@ddt
class LoginTest(unittest.TestCase):
    excel=ReadExcel('case.xlsx','login')
    case_data=excel.read_excel()

    @data(*case_data)
    def test_login(self,case):
        # 第一步：准备测试数据
        data=eval(case['data'])
        expected=eval(case['expected'])
        case_id=case['case_id']
        # 第二步：调用功能函数
        result=login_check(*data)
        # 第三步：比对预期结果与实际结果
        try:
            self.assertEqual(expected,result)
        except AssertionError as e:
            self.excel.write_excel(row=case_id+1,column=5,value='未通过')
            raise e
        else:
            self.excel.write_excel(row=case_id+1, column=5, value='已通过')

@ddt
class RegisterTest(unittest.TestCase):
    excel=ReadExcel('case.xlsx','register')
    case_data=excel.read_excel()

    @data(*case_data)
    def test_register(self,case):
        # 第一步：准备测试数据
        data = eval(case['data'])
        expected = eval(case['expected'])
        case_id = case['case_id']
        # 第二步：调用功能函数
        result = register(*data)
        # 第三步：比对预期结果与实际结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            self.excel.write_excel(row=case_id + 1, column=5, value='未通过')
            raise e
        else:
            self.excel.write_excel(row=case_id + 1, column=5, value='已通过')

