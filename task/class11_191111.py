"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/11 22:26
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
# 1、上课的手机类继承代码自己敲一遍进行提交
print('\n'+'*'*6+'第一题'+'*'*6)
class BigPhone:
    def call_phone(self):
        print('可以打语音电话')

class Phone_V1(BigPhone):
    def music(self):
        print('可以听音乐')
    def send_msg(self):
        print('可以发信息')

class Phone_V2(Phone_V1):
    def game(self):
        print('可以玩游戏')
    def send_msg(self):
        super().send_msg()
        print('可以发彩信')

phone=Phone_V2()
phone.call_phone()
phone.music()
phone.send_msg()

'''
2、有一组数据，如下格式：
[
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 2,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'}, 
{'case_id': 3, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 4,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'}, 
{'case_id': 4, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 5,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'}, 
]
定义一个如下的类
请列表中的每个字典遍历出来，每个字典的数据用一个对象来保存，
要求：通过setattr 把字典中数据设为对象的属性和值，字典中的key对应属性名，value为属性值。
最后把所有的对象，放入一个列表中，得到如下如格式的数据：
[用例对象，用例对象，用例对象...]
class CaseData:
    pass
'''
print('\n'+'*'*6+'第二题'+'*'*6)
data=[
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 2,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
{'case_id': 3, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 4,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
{'case_id': 5, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 6,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
]
li1=[]
class CaseData:
    pass
for i in data:
    case=CaseData()
    for k,v in i.items():
        setattr(case,k,v)
    li1.append(case)

for m in li1:
    print(m.__dict__)





