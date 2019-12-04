"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/3 14:55
E-mail  : 506615839@qq.com
File    : getdata.py
============================
"""
import requests
# 获取注册member_id
register_url='http://api.lemonban.com/futureloan/member/register'
data={"mobile_phone":"13641878102","pwd":12345678,"regname":"test02"}
header={
    "X-Lemonban-Media-Type":"lemonban.v1"
}
response=requests.post(url=register_url,json=data,headers=header)
res=response.json()
print(res)
# # 获取id
# id=res['data']['id']
# print(id) # 1922
# -------------------登录------------------------------
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
# 获取登录后用户id
member_id=res['data']['id']
# print(member_id)
# 获取token_type
token_type=res['data']['token_info']['token_type']
# print(token_type)
token=res['data']['token_info']['token']
# print(token)
token_data=token_type+' '+token
# print(token_data)

# -------------------充值接口------------------
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
# print(recharge_data)
