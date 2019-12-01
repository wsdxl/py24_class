"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/6 21:15
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
class A:
    pass
a=A()
setattr(a,'name','xiaoming')
a=A()
setattr(a,'age',18)

print(getattr(a,name))


