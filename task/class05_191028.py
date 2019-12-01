"""
============================
Author  : XiaoLei.Du
Time    : 2019/10/28 22:19
E-mail  : 506615839@qq.com
============================
"""

'''
1、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给打九折，
如果购买金额大于100元会给打八折。编写一程序，询问购买价格，再打印出折扣和最终价格。
'''
print('\n'+'*'*6+'第一题'+'*'*6)
try:
    price = float(input('请问你购买了多少钱？'))
    if 0 < price < 50:
        print('对不起，没有折扣，一共{:.2f}元'.format(price))
    elif 50 <= price <= 100:
        print('给您打九折，一共{:.2f}元'.format(price * 0.9))
    elif price > 100:
        print('给您打八折，一共{:.2f}元'.format(price * 0.8))
    else:
        print('您的输入有误')
except:
    print('你输入的不是数值')

'''
2、输入一个 5 位数，判断它个位与万位相同，十位与千位相 同。 根据判断打印出相关信息，
相同打印结果：该数据符合规范，不相同打印：该数据不符合规范
'''
print('\n'+'*'*6+'第二题'+'*'*6)
try:
    num = int(input('请输入一个5位数：'))
    num = str(num)
    if len(num)==5:
        if num[0] == num[4] and num[1] == num[3]:
            print('该数据符合规范')
        else:
            print('该数据不符合规范')
    else:
        print('你输入的不是5位数')
except :
    print('你输入的不是数字')

'''
3、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印大于随机数。
小了，则打印小于随机数。如果相等，则打印等于随机数
'''
print('\n'+'*'*6+'第三题'+'*'*6)
import random
try:
    ran = random.randint(1, 9)
    print('随机数是：', ran)
    num = int(input('请输入一个数字：'))
    if 1 <= num <= 9:
        if num > ran:
            print('大于随机数')
        elif num < ran:
            print('小于随机数')
        elif num == ran:
            print('等于随机数')
    else:
        print('您输入的不是1-9之间的数字')
except:
    print('你输入的不是数字')

'''
4、实现剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
 电脑随机出拳比较胜负，显示 用户胜、负还是平局。
'''
print('\n'+'*'*6+'第四题'+'*'*6)
import random
computer=random.randint(1,3)
print('---石头剪刀布游戏开始----')
print('请按下面提示出拳：')
# print('电脑出拳:',computer)
try:
    while True:
        print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
        x = int(input('请输入你的选项：'))
        if 1 <= x <= 4:
            if x == 1 and computer == 3:
                print('您的出拳为：石头，电脑出拳：布，您输了')
            elif x == 1 and computer == 2:
                print('您的出拳为：石头，电脑出拳：剪刀，您胜利了')
            elif x == 2 and computer == 3:
                print('您的出拳为：剪刀，电脑出拳：布，您胜利了')
            elif x == 2 and computer == 1:
                print('您的出拳为：剪刀，电脑出拳：石头，您输了')
            elif x == 3 and computer == 1:
                print('您的出拳为：布，电脑出拳：石头，您胜利了')
            elif x == 3 and computer == 2:
                print('您的出拳为：布，电脑出拳：剪刀，您输了')
            elif x == computer:
                print('平局')
            elif x == 4:
                break
        else:
            print('请输入1-4之间的数字')
except:
    print('你输入的不正确')
print('游戏结束')



