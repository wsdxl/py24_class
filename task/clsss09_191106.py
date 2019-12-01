"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/6 22:08
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
# 1、写出异常处理语句中try作用是什么，except,else,finally下面的代码分别在什么时候运行？
print('\n'+'*'*6+'第一题'+'*'*6)
print('try：作用是监测有可能发生异常的代码\n'
      'except：处理异常之后的处理\n'
      'else：代码没有出现异常，执行else的代码\n'
      'finally：不管代码是否出现异常都会去执行的代码')

# 2、改善上节课的注册程序，打开文件的读取数据的时候，如果文件不存在会报错，请通过try-except来捕获这个错误，进行处理
print('\n'+'*'*6+'第二题'+'*'*6)
def operate():
    # 读取文件内容
    try:
        f = open(file='users.txt', mode='r', encoding='utf8')
        data = f.read()
        users = eval(data)
        print(users)
    except:
        users=[]

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
    print(users)

    # 将所有的用户数据再次写入到文件中
    f = open(file='users.txt', mode='w', encoding='utf8')
    c = str(users)
    f.write(c)
operate()

# 3、优化之前作业的石头剪刀布游戏，用户输入时，如果输入非数字会引发异常，请通过异常捕获来处理这个问题。
print('\n'+'*'*6+'第三题'+'*'*6)
import random
def game():
    print('---石头剪刀布游戏开始----')
    print('请按下面提示出拳：')
    # 创建一个列表来存储 石头 剪刀 布
    li = ['石头', '剪刀', '布']

    while True:
        print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
        # 用户输入数字
        try:
            user_num = int(input('请输入你的选项：'))
        except:
            print('用户的输入不符合规范，默认给1')
            user_num = 1
        # 电脑随机生成数字
        r_num = random.randint(1, 3)
        if 1 <= user_num <= 3:
            # 判断用户和电脑是否相等
            if r_num == user_num:
                print('您的出拳为:{}，电脑出拳:{}，平局'.format(li[user_num - 1], li[r_num - 1]))
            # 判断用户胜利的情况
            elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
                print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(li[user_num - 1], li[r_num - 1]))
            else:
                print('您的出拳为:{}，电脑出拳:{}，您输了'.format(li[user_num - 1], li[r_num - 1]))
        # 用户输入4，游戏结束
        elif user_num == 4:
            print('游戏结束')
            break
        else:
            print('您出拳有误，请按规矩出拳')
game()