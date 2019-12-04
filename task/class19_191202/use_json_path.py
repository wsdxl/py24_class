"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/3 15:43
E-mail  : 506615839@qq.com
File    : use_json_path.py
============================
"""
import requests
import jsonpath
login_url='http://api.lemonban.com/futureloan/member/login'
login_data={
    "mobile_phone": "13641878111",
    "pwd": "12345678",
}
login_header={
    "X-Lemonban-Media-Type":"lemonban.v2"
}

response=requests.post(url=login_url,json=login_data,headers=login_header)
res=response.json()
# print(res)
# 获取用户id
member_id=jsonpath.jsonpath(res,'$..id')[0]
# 获取token类型
token_type=jsonpath.jsonpath(res,'$..token_type')[0]
# 获取token值
token=jsonpath.jsonpath(res,'$..token')[0]
# print(member_id)
# print(token_type)
# print(token)

token_data=token_type+' '+token

# -----------------充值---------------------
recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
recharge_data={
    'member_id':member_id,
    'amount':1000
}
recharge_header={
    "X-Lemonban-Media-Type":"lemonban.v2",
    "Authorization":token_data
}
recharge_response=requests.post(url=recharge_url,json=recharge_data,headers=recharge_header)
recharge_data=recharge_response.json()
print(recharge_data)