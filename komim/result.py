# -*- coding:utf-8 -*-
"""
@author: 杨满球
@file: result.py
@time: 2016/11/5 19:25
"""


class Text:
    def __init__(self, resp):
        self.text = resp.text


class Entry:
    def __init__(self, obj, version=None):
        if isinstance(obj, dict):
            self.__init_from_dict(obj, version)
        else:
            self.__init_from_resp(obj)

    def __init_from_resp(self, resp):
        self.entry = resp.json()['omim']['entryList'][0]['entry']
        self.text = str(self.entry)
        self.version = resp.json()['omim']['version']
        self.mimNumber = self.entry['mimNumber']
        self.status = self.entry['status']

    def __init_from_dict(self, entry, version):
        self.entry = entry['entry']
        self.text = str(self.entry)
        self.version = version
        self.mimNumber = self.entry['mimNumber']
        self.status = self.entry['status']

    def __getitem__(self, key):
        return self.entry[key]

    def __repr__(self):
        return '<Entry  mimNumber={}>'.format(self.mimNumber)

class EntryList:
    def __init__(self, resps):
        resp0 = resps.pop()
        self.resp = resp0.json()
        for resp in resps:
            self.resp['omim']['entryList'].extend(resp.json()['omim']['entryList'])
        self.text = str(self.resp)
        self.version = self.resp['omim']['version']
        self.entryList = [
            Entry(entry, version=self.version) for entry in self.resp['omim']['entryList']
        ]

    def __repr__(self):
        return '<EntryList len={}>'.format(len(self.entryList))

    def __len__(self):
        return len(self.entryList)

    def __getitem__(self, index):
        return self.entryList[index]


