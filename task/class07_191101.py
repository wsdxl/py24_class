"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/1 22:17
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
'''
第一题：简单题 
 1、什么是全局变量？ 
    直接定义在py文件（模块）中的变量叫全局变量，全局变量在当前文件的任何地方都可以使用。

 2、什么是局部变量？
    定义在函数内部的变量叫局部变量，局部变量只能在定义的函数内部使用。

 3、函数内部如何修改全局变量（如何声明全局变量 ）？
    函数内部用global关键字声明全局变量并进行修改

 4、写出已经学过的所有python关键字，分别写出用途？
    False：布尔类型值为假
    True：布尔类型值为真 
    and：逻辑运算符表示与
    not：逻辑运算符表示取反
    or：逻辑运算符表示或
    if:条件语句关键字后面条件成立执行代码
    elif：条件语句中关键字条件成立执行代码
    else：条件语句关键字，如果if语句中条件不成立则运行else下的代码
    while：while循环语句关键字 
    for：for循环语句关键字
    in：for循环语句关键字
    break：终止循环，跳出循环体
    continue：终止当前本轮循环，开启下一个循环
    def：定义函数或方法关键字
    global：声明函数内部变量为全局变量 
    return：函数或方法内表示返回值
    del：删除数据的关键字   
'''

'''
第二题：数据转换 
现在有以下数据， li1 = ["{'a':11,'b':2}","[11,22,33,44]"] 
需要转换为以下格式： li1 = [{'a':11,'b':2},[11,22,33,44]] 
请封装一个函数，按上述要求实现数据的格式转换
'''
print('\n'+'-'*6+'第二题'+'-'*6)
def func():
    li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]
    list1 = []
    for i in li1:
        list1.append(eval(i))
    return list1
d=func()
print(d)

'''
第三题：数据转换
'''
print('\n'+'-'*6+'第三题'+'-'*6)
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
def tran_res1():
    res1 = []
    for i in cases[1:]:
        res = zip(cases[0], i)
        res2 = dict(res)
        res1.append(res2)
    return res1
print('要求一的结果是：\n{}\n'.format(tran_res1()))

def tran_res():
    res = []
    for v in tran_res1():
        if v['case_id'] > 3:
            res.append(v)
    return res
print('要求二的结果是：\n{}'.format(tran_res()))





