"""
============================
Author  : XiaoLei.Du
Time    : 2019/10/30 22:25
E-mail  : 506615839@qq.com
============================
"""
'''
1、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）
'''
print('\n'+'*'*6+'第一题'+'*'*6)
def mul_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}*{}={:<4}'.format(i, j, (i * j)), end=' ')
        print('')

mul_table()
'''
2、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
'''
print('\n'+'*'*6+'第二题'+'*'*6)
def counter_num():
    conunter = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for v in range(1, 5):
                if i != j and j != v and i != v:
                    print('{}{}{}'.format(i, j, v), end=' ')
                    conunter += 1
        print('')
    print(f'一共有{conunter}种组合')
counter_num()


'''
3、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，然后再提示用户选择 ：
   加【1】    减【2】    乘【3】      除【4】，根据不同的选择完成不同的计算 
   每个方法使用一个函数来实现， 选择后调用对应的函数，然后返回结果。
'''
print('\n'+'*'*6+'第三题'+'*'*6)
a = int(input('请输入数字1：'))
b = int(input('请输入数字2：'))
c = int(input('请选择：加(1) 减(2) 乘(3) 除(4):'))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if c == 1:
    print(add(a, b))
elif c == 2:
    print(sub(a, b))
elif c == 3:
    print(mul(a, b))
else:
    print(div(a, b))




'''
4、学习控制流程时，我们讲了一个登录的案例，现在要求大家通过代码实现一个注册的流程，基本要求：
    1、运行程序，提示用户，输入用户名，输入密码，再次确认密码。
    2、判读用户名有没有被注册过，如果用户名被注册过了，那么打印结果该用户名已经被注册。
    3、用户名没有被注册过，则判断两次输入的密码是否一致，一致的话则注册成功，否则给出对应的提示。
'''
print('\n'+'*'*6+'第四题'+'*'*6)
# 第一种方法：
def gister():
    user=['user1','user2']
    while True:
        name = input('请输入用户名：')
        if name in user:
            print('该用户名已经被注册')
            break
        else:
            passwd = input('请输入密码：')
            repass = input('请再次确认密码：')
            if passwd !=repass:
                print('两次输入的密码不一致')
                break
            else:
                user.append(name)
                print('注册成功')
                break
gister()


## 第二种方法：
# def gister():
#     user = [{'username': 'xiaoming', 'passwd': 'abc123456'}]
#     for i in user:
#         name = input('请输入用户名：')
#         # print(i)
#         if i['username'] == name:
#             print('该用户名已经被注册')
#         else:
#             passwd = input('请输入密码：')
#             repass = input('请再次确认密码：')
#             if passwd != repass:
#                 print('两次输入的密码不一致')
#             else:
#                 user.append({'username': name, 'passwd': passwd})
#                 print('注册成功')
#                 break
# gister()

# # 第三种方法：用迭代器
# def gister1():
#     name = input('请输入用户名：')
#     check_name(name)
#     passwd = input('请输入密码：')
#     repass = input('请再次确认密码：')
#     check_pass(passwd,repass)

# def check_name(name):
#     user = ['user1','user2']
#     if name in user:
#         check_name(input('该用户名已经被注册,请重新输入用户名：'))       
    

# def check_pass(pass1,pass2):
#     if pass1 !=pass2:
#         print('两次输入的密码不一致')
#     else:
#         print('注册成功！')

# gister1()










