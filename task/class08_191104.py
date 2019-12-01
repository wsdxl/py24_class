"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/4 22:36
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""

# 第一题
print('\n'+'*'*6+'第一题'+'*'*6)
# 第一种
def editor():
    f = open(file='test.txt', mode='r', encoding='utf8')
    data = f.readlines()
    di1 = {}
    for index, value in enumerate(data):
        # print(index, value)
        key = '数据{}'.format(index)
        value = value.strip('\n')
        di1[key] = value
    return di1

print(editor())

#第二种
# def editor():
#     f = open(file='test.txt', mode='r', encoding='utf8')
#     t = f.readlines()
#     list1 = []
#     for i in t:
#         list1.append(i.strip('\n'))
#     print(list1)
#     data = ['data0', 'data1', 'data2', 'data3']
#     a = dict(zip(data, list1))
#     f.close()
#     return a
#
# print(editor())

# 第二题
print('\n'+'*'*6+'第二题'+'*'*6)
def tran_01():
    f = open(file='case.txt', mode='r', encoding='utf8')
    t1 = f.readlines()
    list2 = []
    for items in t1:
        di2 = {}
        for item in items.strip('\n').split(','):
            di2[item.split(':', 1)[0]] = item.split(':', 1)[1]
        list2.append(di2)
    return list2
print('要求一：\n{}'.format(tran_01()))

def tran_02(a):
    dic1 = {}
    for key, value in enumerate(tran_01()):
        # print(key, value)
        key = 'data{}'.format(key + 1)
        dic1[key] = value
    return dic1


print('要求二：\n{}'.format(tran_02(tran_01())))

# 第三题
print('\n'+'*'*6+'第三题'+'*'*6)
def operate():
    # 读取文件内容
    # users=[{'name': 'py01', 'password': '123'}]
    f = open(file='users.txt', mode='r', encoding='utf8')
    data = f.read()
    users = eval(data)
    print(users)

    # 注册功能
    username = input('请输入新账号:')  # 输入账号
    password1 = input('请输入密码：')  # 输入密码
    password2 = input('请再次确认密码：')  # 再次确认密码

    for user in users:  # 遍历出所有账号，判断账号是否存在
        if username == user['name']:
            print('该账户已存在')  # 账号存在，
            break
    else:
        # 判断两次密码是否一致
        if password1 != password2:
            print('注册失败，两次输入的密码不一致')
        else:
            # 账号不存在 密码一样，则添加到账户列表中
            users.append({'name': username, 'pwd': password2})
            print('注册成功！')
    # print(users)

    # 将所有的用户数据再次写入到文件中
    f = open(file='users.txt', mode='w', encoding='utf8')
    c = str(users)
    f.write(c)
operate()



