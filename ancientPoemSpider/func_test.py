#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : func_test.py
# @Description:
# @Time       : 2021-12-29 下午 3:54
# @Author     : Hou


class Kls(object):
    def __init__(self, data):
        self.data = data
    def printd(self):
        print(self.data)
    @staticmethod
    def smethod(*arg):
        print('Static:', arg)
    @classmethod
    def cmethod(*arg):
        print('Class:', arg)


if __name__ == '__main__':
    ik = Kls(23)
    ik.printd()
    ik.smethod()
    ik.cmethod()
    # Kls.printd()
    Kls.cmethod()
    Kls.smethod()