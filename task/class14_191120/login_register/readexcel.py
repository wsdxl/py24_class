"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/19 10:24
E-mail  : 506615839@qq.com
Software: PyCharm
============================
"""
import openpyxl
class CaseData:
    pass

class ReadExcel(object):

    def __init__(self,filename,sheetname):
        self.filename=filename
        self.sheetname=sheetname

    def open(self):
        self.wb=openpyxl.load_workbook(self.filename)
        self.sh=self.wb[self.sheetname]

    def close(self):
        '''关闭工作簿，释放内存'''
        self.wb.close()

    def readdata(self):
        self.open()
        rows = list(self.sh.rows)
        title = []
        for i in rows[0]:
            title.append(i.value)

        cases = []
        for r in rows[1:]:
            data = []
            for m in r:
                data.append(m.value)
            case = dict(zip(title, data))
            cases.append(case)
        self.close()
        return cases

    def read_data_obj(self):
        self.open()
        rows = list(self.sh.rows)
        title = []
        for i in rows[0]:
            title.append(i.value)

        cases = []
        for r in rows[1:]:
            data = []
            for m in r:
                data.append(m.value)
            case = list(zip(title, data))
            # print(case)
            case_obj=CaseData()
            for key,value in case:
                setattr(case_obj,key,value)
            cases.append(case_obj)
        self.close()
        return (cases)

    def write_data(self,row,column,value):
        self.open()
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.filename)
        self.close()








if __name__ == '__main__':
    excel=ReadExcel('case.xlsx','login')
    print(excel.read_data_obj())

