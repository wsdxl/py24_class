"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/28 18:57
E-mail  : 506615839@qq.com
File    : test.py
============================
"""
import os
from common.contans import ConfDir
from configparser import ConfigParser

class ReadConf(ConfigParser):
    def __init__(self,finename,encoding='utf8'):
        super().__init__()
        self.finename=finename
        self.encoding=encoding
        self.read(finename,encoding)

    def writeconf(self,section,option,value):
         self.set(section,option,value)
         self.write(open(self.finename,'w',encoding=self.encoding))

if __name__ == '__main__':
    confpath=os.path.join(ConfDir,'conf.ini')
    confi=ReadConf(confpath)
    print(confi.get('logging','filename'))
