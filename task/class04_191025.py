"""
============================
Author  : XiaoLei.Du
Time    : 2019/10/25 22:25
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""

'''
一、请指出下面那些为可变类型的数据，那些为不可变类型的数据
1、 (11)    
2、 {11，22}
3、 ([11,22,33])
4、 {"aa":111}
'''

print('*'*6+'第一题'+'*'*6)
print('1、为数值类型，属于不可变类型\n2、为集合，属于可变类型\n3、为列表，属于可变类型\n4、为字典，属于可变类型')




'''
二、有5道题（通过字典来存储数据）： 某比赛需要获取你的个人信息，设计一个程序， 
 1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
 2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
 3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 
 4、平台为了保护你的隐私，需要你删除你的联系方式；
 5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
'''
print('*'*6+'第二题'+'*'*6)
name=input('请输入姓名：')
sex=input('请输入性别：')
age=input('请输入年龄：')
di1={'name':name,'sex':sex,'age':age}
print('di1=',di1)
print('我的名字{}，今年{}岁，性别{}，喜欢敲代码'.format(di1['name'],di1['age'],di1['sex']))
height=float(input('请输入身高：'))
phone=int(input('请输入联系方式：'))
di1.update({'height':height,'phone':phone})
print(di1)
di1.pop('phone')
print(di1)
skill=input('我最擅长的技能是：')
di1['skill']=skill
print(di1)

'''
三、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
 要求一：去除列表中的重复元素，
 要求二：删除 77，88，99这三个元素
'''
print('*'*6+'第三题'+'*'*6)
li = [11,22,33,22,22,44,55,77,88,99,11]
li1=list(set(li))
print(li1)
# #第一种粗暴的方法
# li1.clear()
# li1=[33, 11, 44, 22, 55]
# #第二种方法
# li1.remove(77)
# li1.remove(88)
# li1.remove(99)
# print(li1)
# 第三种方法
li1.pop(1)
li1.pop(3)
li1.pop()
print(li1)

'''
四、有下面几个数据 ，
t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",11)]
请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":22,"bb":22}
要注意字典中元素的位置（使用python3.5以下的同学不用考虑位置）
'''
print('*'*6+'第四题'+'*'*6)
t1 = ("aa",11);t2= ("bb",22);li1 = [("cc",11)]
li1.append(t2)
li1.insert(0,t1)
dic1=dict(li1)
dic1['cc']=22
print(dic1)






