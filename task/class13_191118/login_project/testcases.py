"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/17 20:20
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
import unittest
from login import login_check

class LoginTest(unittest.TestCase):

    def __init__(self,methodName,data,expect):
        super().__init__(methodName)
        self.data=data
        self.expect=expect

    def test_login(self):
        # 第一步：准备测试数据
        data=self.data
        expect=self.expect
        # 第二步：执行功能函数
        result=login_check(*data)
        # 第三步：比较实际结果和预期结果
        self.assertEqual(expect,result)



if __name__ == '__main__':
    unittest.main()