"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/3 20:50
E-mail  : 506615839@qq.com
File    : test_register.py
============================
"""
import os
import random
import requests
import unittest
from library.ddt import ddt, data
from common import read_excel
from common.contans import DataDir
from common.read_conf import conf
from common.my_logger import my_logger
from common.hander_request import HanderRequest

base_url = conf.get('env', 'url')
header = eval(conf.get('env', 'header'))

@ddt
class TestRegister(unittest.TestCase):
    datapath = os.path.join(DataDir, 'cases.xlsx')
    excel = read_excel.ReadExcel(datapath, 'register')
    register_data = excel.read_excel()
    rest = HanderRequest()

    @data(*register_data)
    def test_register(self, case):
        # 判断是否有手机号码需要替换
        if '#phone#' in case['data']:
            phone=self.random_phone()
            case['data']=case['data'].replace('#phone#',phone)
        data = eval(case['data'])
        expected = eval(case['expected'])
        case_id = case['case_id']
        url = case['url']
        register_url = base_url + url
        method = case['method']
        response = self.rest.send(url=register_url, method=method, json=data, headers=header)
        res = response.json()
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as e:
            self.excel.write_excel(row=case_id + 1, column=8, value='未通过')
            my_logger.info('用例-->{}:执行未通过'.format(case['title']))
            my_logger.error(e)
            print("预期结果：{}".format(expected))
            print("实际结果：{}".format(res))
            raise e
        else:
            self.excel.write_excel(row=case_id + 1, column=8, value='已通过')
            my_logger.info('用例-->{}:执行已通过'.format(case['title']))

    @staticmethod
    def random_phone():
        phone = '186'
        for i in range(8):
            phone += str(random.randint(0, 9))
        return phone