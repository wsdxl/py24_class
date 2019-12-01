"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/1 8:54
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
# users=[{'name':'py01','pwd':'123'},{'name':'py02','pwd':'123'},\
#        {'name':'py03','pwd':'123'},{'name':'py04','pwd':'123'}]
# for user in users:
#     if user['name']=='py03':
#         print('找到用户py03')
#         break
# else:
#     print('没有找到用户py03')



# res1=[
#     {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
#     {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}]
#
# data=filter(lambda x:x['case_id']>3,res1)
# print(list(data))

# f=lambda x,y:x+y
# print(f(11,22))

# def operate():
#     # 读取文件内容
#     # users=[{'name': 'py01', 'password': '123'}]
#     f = open(file='users.txt', mode='r', encoding='utf8')
#     data = f.read()
#     users = eval(data)
#     print(users)
#
#     # 注册功能
#     username = input('请输入新账号:')  # 输入账号
#     password1 = input('请输入密码：')  # 输入密码
#     password2 = input('请再次确认密码：')  # 再次确认密码
#
#     for user in users:  # 遍历出所有账号，判断账号是否存在
#         if username == user['name']:
#             print('该账户已存在')  # 账号存在，
#             break
#     else:
#         # 判断两次密码是否一致
#         if password1 != password2:
#             print('注册失败，两次输入的密码不一致')
#         else:
#             # 账号不存在 密码一样，则添加到账户列表中
#             users.append({'name': username, 'pwd': password2})
#             print('注册成功！')
#     # print(users)
#
#     # 将所有的用户数据再次写入到文件中
#     f = open(file='users.txt', mode='w', encoding='utf8')
#     c = str(users)
#     f.write(c)
# operate()

# def editor():
#     f = open(file='test.txt', mode='r', encoding='utf8')
#     data = f.readlines()
#     di1 = {}
#     for index, value in enumerate(data):
#         print(index, value)
#         key = '数据{}'.format(index)
#         value = value.strip('\n')
#         di1[key] = value
#     return di1
#
# print(editor())




# list1=[
# {'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}, {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
# {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
# ]
#
# dic1={}
# for key,value in enumerate(list1):
#     print(key,value)
#     key='data{}'.format(key+1)
#     dic1[key]=value
# print(dic1)

import os

print(os.path.dirname(__file__))

