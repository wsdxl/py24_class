"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/15 22:16
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
import unittest
from registerfunc import register
from login import login_check
from readexcel import ReadExcel

excel=ReadExcel('case.xlsx','login')
excel2=ReadExcel('case.xlsx','register')

class LoginTest(unittest.TestCase):

    def __init__(self,methodName,data,expect,case_id):
        super().__init__(methodName)
        self.data=data
        self.expect=expect
        self.case_id=case_id

    def test_login(self):
        # 第一步：准备测试数据
        data=self.data
        expect=self.expect
        # 第二步：执行功能函数
        result=login_check(*data)
        # 第三步：比较实际结果和预期结果
        try:
            self.assertEqual(expect,result)
        except AssertionError as e:
            excel.write_data(row=self.case_id+1,column=5,value='不通过')
            raise e
        else:
            excel.write_data(row=self.case_id+1,column=5,value='通过')


class RegisterTestCase(unittest.TestCase):

    def __init__(self,methodName,data,expected,case_id):
        super().__init__(methodName)
        self.data=data
        self.expected=expected
        self.case_id=case_id

    def test_register(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users =self.data
        # 2、预期结果：
        expected=self.expected
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        try:
            self.assertEqual(expected,restult)
        except AssertionError as e:
            excel2.write_data(row=self.case_id + 1, column=5, value='不通过')
            raise e
        else:
            excel2.write_data(row=self.case_id + 1, column=5, value='通过')





if __name__ == '__main__':
    unittest.main()