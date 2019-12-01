"""
============================
Author  : XiaoLei.Du
Time    : 2019/10/21 22:16
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""

# 1、用户输入一个数值，请判断用户输入的是否为偶数？是偶数输出True,不是输出False（提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法将字符串转换为数值类型，再做判段）

# try:
#     x = int(input('请输入一个数值：'))
#     if x%2==0:
#         print(True)
#     else:
#         print(False)
# except:
#     print('您输入的不是数值')

# 2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间），最后计算出应该支付的金额！
# import random
# s1=random.randint(5,9)
# s2=random.random()
# s3=s1+s2
# print(s3)
# s=float(input('您的橘子价格为：'))
# p=s*s3
# print('您应支付的金额为：',p)
# 3、现在有变量 a = （‘hello’,‘python18’,‘!’）,通过相关操作转换成字符串：'hello python18 !'（注意点:转换之后单词之间有空格）
a = ('hello','python18','!')
b =' '.join(a)
print(b)

# 4、使用random模块和字符串拼接的方法，随机生成一个130开头的手机号码。
# import random
# a=str(130)
# b=random.randint(00000000,99999999)
# c=a+str(b)
# print(c)


