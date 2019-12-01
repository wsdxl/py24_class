"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/9 12:11
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
'''
1、类属性怎么定义？ 实例属性怎么定义？什么属性适合定义为类属性，什么属性适合定义成实例属性（简答）
类属性的定义：直接定义在类里面的变量，实例属性的定义：对象.属性名=属性值;
这个类所有的对象都有这个属性，属性值是一样的适合定义为类属性；
这个类所有的对象都可能这个属性，每个对象的属性值都有可能不一样适合定义为实例属性

2、实例方法中的self代表什么？（简答）
代表的是对象本身，哪个对象去调用该方法，那么self代表的就是哪个对象

3、类中__init__方法在什么时候调用的？（简答）
初始化方法在实例化类对象的时候调用

'''
'''
4、封装一个学生类，(自行分辨定义为类属性还是实例属性，方法定义为实例方法)

-  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，

-  方法一：计算总分，方法二：计算三科平均分，方法三：打印学生的个人信息。
'''
print('\n'+'*'*6+'第四题'+'*'*6)
class Student:
    identity='学生'
    def __init__(self,name,age,sex,english_score,math_score,chinese_score):
        self.name=name
        self.age=age
        self.sex=sex
        self.english_score=english_score
        self.math_score=math_score
        self.chinese_score=chinese_score

    def total_scores(self):
        return self.english_score+self.math_score+self.chinese_score

    def avg_score(self):
        return (self.english_score+self.math_score+self.chinese_score)/3

    def person_msg(self):
        print(f'姓名：{self.name}\n年龄：{self.age}岁\n性别：{self.sex}\n英语：{self.english_score}分\n\
数学：{self.math_score}分\n语文：{self.english_score}分')

obj=Student('小明',18,'男',98,100,99)
print(f'{obj.name}的身份是{obj.identity}')
print(f'{obj.name}的总分是{obj.total_scores()}')
print(f'{obj.name}的平均分是{obj.avg_score()}')
obj.person_msg()

'''
5、封装一个测试用例类(自行分辨定义为类属性还是实例属性)，
-  属性：用例编号  url地址   请求参数   请求方法    预期结果   实际结果
'''
print('\n'+'*'*6+'第五题'+'*'*6)
class TestCases:
    def __init__(self,id,url,rst_parama,rst_method,expect,res):
        self.id=id
        self.url=url
        self.rst_parama=rst_parama
        self.rst_method=rst_method
        self.expect=expect
        self.res=res

    def case_msg(self):
        print(f'用例编号：{self.id}\nurl：{self.url}\n请求参数：{self.rst_parama}\n\
请求方法：{self.rst_method}\n预期结果：{self.expect}\n实际结果：{self.res}')

test_case=TestCases(1,'192.168.0.65','xxxx','post','status=1','status=1')
test_case.case_msg()