"""
============================
Author  : XiaoLei.Du
Time    : 2019/10/19 10:17
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""

'''
1、下面那些不能作为标识符？

1、find     2、 _num   3、7val   4、add.    5、def     
6、pan     7、-print   8、open_file 9、FileName   10、9print  
11、INPUT   12、ls     13、user^name  14、list1   15、str_
16、_888       17、is      18、true     19、none        20、try  

答：3、4、5、7、10、12、13、17、20
'''

'''
2、写一段代码，运行的时候依次提示输入姓名，年龄、性别
然后在控制台 按照以下格式输出信息  ：姓名、年龄、性别 ：
'''
a=input('姓名：')
b=input('性别：')
c=input('年龄：')
print('****************')
print('姓名：',a)
print('性别：',b)
print('年龄：',c)
print('****************')


'''
3、请描述一下变量的命名规范，和有哪几种命名风格？（简单题）
答：
只使用数字、字母和下划线组成，但不能使用数字开头
变量命名应该做到见名之意，尽量不用拼音
常见的命名风格有3种：
1）纯小写字母，每个单词之间用下划线隔开
min_num=25
2）大驼峰命名法，每个单词第一个字母用大写
MinNum=26
3）小驼峰命名法，第一个单词首字母小写，后面单词的第一个字母大写
minNum=27
'''


'''
4、把今天学的python基本语法，总结成笔记

print输出：直接输出内容到控制台
print默认输出是自动换行的
如：print('hello python')
如果不想换行用逗号隔开并加上end=''
如：print('hello python',end='')

数值：和数学中的数字表示是一样的，数值不用加引号
如：print(5)
print(1.5)

字符串：可以用引号、双引号和三引号来表示字符串
print('hello python')
print("hello python")
print("""hello python""")
字符串中有单引号，就用双引号包起来，有双引号，就用单引号包起来
print('成绩："90"')
print("成绩：'90'")
字符串和数值不能相加减
如：print('9'+9)

注释：用来对代码进行说明
单行注释用以#开始，多行注释用三个单引号或三个双引号，注释的代码不会被执行
注释的快捷键：ctrl+/,也可以取消注释

变量：
只使用数字、字母和下划线组成，但不能使用数字开头
x=3
y2=8
z_3=66
_min=45
变量命名应该做到见名之意，尽量不用拼音
name='xiaoming'
age=18
常见的命名风格有3种：
1）纯小写字母，每个单词之间用下划线隔开
min_num=25
2）大驼峰命名法，每个单词第一个字母用大写
MinNum=26
3）小驼峰命名法，第一个单词首字母小写，后面单词的第一个字母大写
minNum=27

标识符：只要是自己起的名字都是标识符，
变量名、类名、包名、函数名、模块名（py文件）
标识符的命名规范：
只使用数字、字母和下划线组成，但不能使用数字开头
变量命名应该做到见名之意，尽量不用拼音
注意点：标识符不能有关键字
import keyword
print(keyword.kwlist) 输出所有关键字
'False', 'None', 'True', 'and', 'as', 'assert',
 'async', 'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 
'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'


input:输入到控制台
name=input('请输入你的名字：')

'''