"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/26 16:16
E-mail  : 506615839@qq.com
File    : 配置文件的操作.py
============================
"""
from configparser import ConfigParser

# 创建一个操作配置文件的对象
conf=ConfigParser()
# 读取配置文件中的内容
conf.read('conf.ini',encoding='utf8')

# # get方法，读出来的内容都是字符串
# res=conf.get('logging','level')
# res2=conf.get('mysql','username')
# print(res,type(res))
# print(res2,type(res2))

# getint:读取出整数类型的内容
res3=conf.getint('mysql','port')
print(res3,type(res3))
# getfloat:读取出小数类型的内容
res4=conf.getfloat('dxl','age')
print(res4,type(res4))
# getboolean:读取出布尔类型的内容
res5=conf.getboolean('dxl','switch')
print(res5,type(res5))

# 配置数据的写入
conf.set('dxl','work',value='softtest')
conf.write(open('conf.ini','w',encoding='utf8'))