"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/26 18:59
E-mail  : 506615839@qq.com
File    : python基本语法.py
============================
"""


import random
# import decimal
# num=random.random()
# print(num)
# num1=random.randint(1,9)
# print(num1)
# num2=num+num1
# print(num2)
# a=decimal.Decimal('4.29')
# b=decimal.Decimal('3.85')
# c=a-b
# print(c)
# a1=4.29
# b1=3.85
# c1=a1-b1
# print(c1)
# a=''
# b=' '
# print(bool(a))
# print(bool(b))
# x='hello python'
# print(x[-3::-2])
# 4、使用random模块和字符串拼接的方法，随机生成一个130开头的手机号码
# n='130'
# for i in range(1,9):
#     num=str(random.randint(1,9))
#     n+=num
# print('手机号码:',n)

print('{:<8}****'.format('abc'))  #左对齐填充
print('{:>8}****'.format('abc'))   #右对齐填充
print('{:^8}****'.format('abc'))

