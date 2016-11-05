# -*- coding:utf-8 -*-
"""
@author: 杨满球
@file: result.py
@time: 2016/11/5 19:25
"""


class Result:
    """
    结果解析类
    """
    def __init__(self, resp):
        self.resp = resp
        self.text = resp.text
        self.content = resp.content
        #直接去除掉最外层的结构，支持属性取值
        self.dict = resp.json()['omim']
        self.version = self['version']
        self.entryList = self['entryList']

    def __getitem__(self, key):
        """
        支持像字典一样取值
        """
        return self.dict[key]

    def entry_list(self):
        """
        返回entry列表
        """
        return self['entryList']

    def as_dict(self):
        """
        作为字典返回结果
        :return:
        """
        return self.dict

    def len_entry(self):
        return len(self.entryList)
