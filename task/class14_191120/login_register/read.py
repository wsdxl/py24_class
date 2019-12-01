"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/20 22:47
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
import openpyxl
wb=openpyxl.load_workbook('case.xlsx')
sh=wb['login']
rows=list(sh.rows)

title=[]
for i in rows[0]:
    title.append(i.value)

cases=[]
for r in rows[1:]:
    data=[]
    for m in r:
        data.append(m.value)
        case=dict(zip(title,data))
    cases.append(case)

print(cases)


