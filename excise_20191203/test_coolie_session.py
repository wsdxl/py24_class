"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/3 21:45
E-mail  : 506615839@qq.com
File    : test_coolie_session.py
============================
"""
"""
使用cookie和session鉴权的接口处理
使用requests模块中的session对象来发请求
"""
import requests
# # 老版本的前程贷登录接口
# login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
# logon_data={
#     "mobilephone": "13367899876",
#     "pwd": "lemonban"
#       }
# res=requests.post(url=login_url,data=logon_data)
# # print(res.cookies)
#
# # 老版本的充值接口
# recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
# recharge_data = {
#     "mobilephone": "13367899876",
#     "amount": 200000
# }
#
# res1=requests.post(url=recharge_url,data=recharge_data)
# print(res1.json())

#-----------------使用requests模块中的session对象来发请求---------------

# 使用requests中的session对象保存cookies信息
sess = requests.session()
# 老版本的前程贷登录接口
login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
logon_data={
    "mobilephone": "13367899876",
    "pwd": "lemonban"
      }
res=sess.post(url=login_url,data=logon_data)
print(res.cookies)

# 老版本的充值接口
recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
recharge_data = {
    "mobilephone": "13367899876",
    "amount": 200000
}

res1=sess.post(url=recharge_url,data=recharge_data)
print(res1.json())