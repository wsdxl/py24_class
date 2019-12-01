"""
============================
Author  : XiaoLei.Du
Time    : 2019/10/29 21:50
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
# 登录小例子
user={'username':'python24','passwd':'abc123456'}
name=input('请输入用户名：')
passwd=input('请输入密码：')

if name==user['username']:
    if passwd==user['passwd']:
        print('用户名密码正确，登录成功')
    else:
        print('密码错误')
else:
    print('用户名不存在')

# if name==user['username'] and passwd==user['passwd']:
#     print('登录成功')
# else:
#     print('用户名或密码错误')

# # 打印100遍hello python
# n=0
# while n<100:
#     print('这是第{}遍，hello python'.format(n+1))
#     n+=1

# 计算 1+2+3+....10,当n=5时停止循环

# n=1
# s=0
# while n<=10:
#     s+=n
#     print(n,s)
#     if n==5:
#         break
#     n+=1
# print(s)
