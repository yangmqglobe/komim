# -*- coding:utf-8 -*-
"""
@author: 杨满球
@file: exceptions.py
@time: 2016/11/5 13:04
"""
import re

class IllegalArgumentException(Exception):
    """
    参数错误异常，与API返回的异常一致
    """
    def __init__(self, e):
        description = re.findall('IllegalArgumentException: (.+)</h1>', e)[0]
        self.description = description

    def __str__(self):
        return repr(self.description)
