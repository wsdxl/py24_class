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
class RegisterTestCase(unittest.TestCase):

    def test_1register_pass(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users = ('xiaoming','123456','123456')
        # 2、预期结果：
        expected={"code": 1, "msg": "注册成功"}
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        self.assertEqual(expected,restult)

    def test_2user_None(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users = ('','123456','123456')
        # 2、预期结果：
        expected={"code": 0, "msg": "所有参数不能为空"}
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        self.assertEqual(expected,restult)

    def test_3pwd_None(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users = ('xiaohong','','')
        # 2、预期结果：
        expected={"code": 0, "msg": "所有参数不能为空"}
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        self.assertEqual(expected,restult)

    def test_4pwd_diff(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users = ('xiaohong','123456','1234567')
        # 2、预期结果：
        expected={"code": 0, "msg": "两次密码不一致"}
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        self.assertEqual(expected,restult)

    def test_5user_exist(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users = ('python24','123456','123456')
        # 2、预期结果：
        expected={"code": 0, "msg": "该账户已存在"}
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        self.assertEqual(expected,restult)

    def test_6pwd_error(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users = ('user01','1234','1234')
        # 2、预期结果：
        expected={"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        self.assertEqual(expected,restult)
    def test_7pwd_error2(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users = ('user02','1234567891234567891','1234567891234567891')
        # 2、预期结果：
        expected={"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        self.assertEqual(expected,restult)

    def test_8user_error(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users = ('user','123456','123456')
        # 2、预期结果：
        expected={"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        self.assertEqual(expected,restult)

    def test_9user_error2(self):
        # 第一步、准备用例数据
        # 1、用例参数
        users = ('testing123456789python','123456','123456')
        # 2、预期结果：
        expected={"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 执行功能函数获得实际结果
        restult=register(*users)
        # 第三步：比对预期结果和实际结果
        self.assertEqual(expected,restult)

if __name__ == '__main__':
    unittest.main()