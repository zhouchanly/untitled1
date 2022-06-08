from airtest.core.api import *
from airtest.core.api import using
# using("F:/PycharmProjects/untitled1/airdir.air")
import sys
sys.path.append(r"F:\PycharmProjects\untitled1\airdir.air")
using("airdir.air")
# from airdir import *
# a=airdir.Ooo().aaa
print('test')
class Ass():
    def __init__(self):
        print('__init__')
    def a1(self):
        print("10000")
    def a2(self):
        print("qwerr")
        
        