"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/30 9:52
E-mail  : 506615839@qq.com
File    : 初识接口测试.py
============================
"""
import requests
# url='http://api.lemonban.com/futureloan/member/register'
# data={
#     'mobile_phone':13641878100,
#     'pwd':'12345678',
#     'reg_name':'大王'
# }
# header={
#     'X-Lemonban-Media-Type':'lemonban.v1'
# }
# # post请求方法
# response=requests.post(url=url,json=data,headers=header)
# print(response.json())

url='http://api.lemonban.com/futureloan/loans?pageSize=4'
# data={"pageIndex":1,"pageSize":4}
header={
    'X-Lemonban-Media-Type':'lemonban.v1'
}
response=requests.get(url=url,headers=header)
res=response.json()
print(len(res['data']))