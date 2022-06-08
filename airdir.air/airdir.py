import sys
from airtest.core.api import *
auto_setup(__file__)
from airtest.core.api import using


# ST.PROJECT_ROOT=r'F:\PycharmProjects\untitled1\aaair.air'  #用这行不行，也一样会报错
# sys.path.append(r"F:\PycharmProjects\untitled1\aaair.air")
using(r"F:\PycharmProjects\untitled1\aaair.air")

from aaair import Ass
a=Ass()
a.a1()
a.a2()

class Ooo():
    def aaa(self):
        print('8888888888')

    def airrr(self):
        print('git')

print('tt')
Ooo().aaa()