"""
============================
Author  : XiaoLei.Du
Time    : 2019/10/23 22:27
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""

# 1、现有字符串
# str1 = "PHP is the best programming language in the world! "
# 要求一：将给定字符串的PHP替换为Python
str1 = "PHP is the best programming language in the world! "
str2=str1.replace('PHP','Python')
print(str2)
# 要求二：替换以后，将字符串以空格为分割点进行分割得到一个列表
str3=str2.split(' ')
print(str3)

# 2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”（要求：使用上课学过的知识点来做）
num=int(input('请输入1-7之间的数字：'))
li1=['一','二','三','四','五','六','末']
day='今天是周{}'.format(li1[num-1])
print(day)

# 3、现在有一个列表 li2 = [1，2，3，4，5]
# 第一步：请通过三行代码将上面的列表，改成这个样子
# li2 = [0，1，2，3，66，5，11，22，33]
li2 = [1,2,3,4,5]
li2.insert(0,0)
print(li2)
li2[4]=66
print(li2)
li2.extend([11,22,33])
print(li2)

# 第二步：对li2进行排序处理 （从大到小）
li2.sort(reverse=True)
print(li2)
# 第三步：对修改后的列表
# 进行降序排序（从大到小）
li2.sort()
li2.reverse()
print(li2)

# 4、切片
#1、li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 请通过切片得出结果[3, 6, 9]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res=li[2::3]
print(res)
# 2、s = 'python java php',通过切片获取: java
s='python java php'
s1=s[7:11]
print(s1)

# 5、定义一个空列表user = [], 分别提示用户输入，姓名，年龄，身高，用户输入完之后，将输入的信息添加的列表中保存，然后按照一下格式输出：

# 用户的姓名为：xxx, 年龄为：xxx, 身高为：xxx, 请仔细核对（要求：输出的身高要求保留2位小数）
user=[]
name=input('请输入您的姓名：')
age=input('请输入您的年龄：')
height=float(input('请输入您的身高：'))
user.append(name)
user.append(age)
user.append(height)
s='用户的姓名为：{}, 年龄为：{}岁, 身高为：{:.2f}cm,请仔细核对'.format(user[0],user[1],user[2])
print(s)