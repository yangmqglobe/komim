# -*- coding:utf-8 -*-
"""
@author: 杨满球
@file: komim.py
@time: 2016/11/5 11:54
"""

from .exceptions import *
from .result import *
import requests


class Komim:
    """
    Komim对象，用于向OMIM的api发起请求，提供各种api
    """
    __apikey = ''
    __session = None
    resp = None

    def __init__(self, apikey, check=False):
        """
        构造方法，初始化请求对象，其次添加ApiKey
        :param apikey: 从OMIM申请的ApiKey
        :param check: 是否检查ApiKey可用性，需要发起一次请求，消耗资源
        """
        self.__session = requests.session()
        self.update_apikey(apikey)
        if check:
            self.check_apikey()

    def update_apikey(self, apikey):
        """
        更新ApiKey
        :param apikey:新的ApiKey
        """
        self.__apikey = apikey
        cookies = {'ApiKey': apikey}
        self.__session.cookies.update(cookies)

    def check_apikey(self):
        """
        检查ApiKey是否可用，不可用将抛出异常
        """
        url = 'http://api.omim.org/api/apiKey'
        data = {
            'apiKey': self.__apikey,
            'format': 'json'
        }
        self.resp = self.__session.post(url, data=data)
        if self.resp.status_code == 200:
            pass
        else:
            raise IllegalArgumentException(self.resp.text)

    @staticmethod
    def __init_param(param, parameters):
        for parameter in parameters.keys():
            if parameters[parameter]:
                param['include'].append(parameter)
            else:
                param['exclude'].append(parameter)
        param['mimNumber'] = ','.join(param['mimNumber'])
        if len(param['include']) > 0:
            param['include'] = ','.join(param['include'])
        else:
            param['include'] = None
        if len(param['exclude']) > 0:
            param['exclude'] = ','.join(param['exclude'])
        else:
            param['exclude'] = None
        return param

    def entry(self, mimnumber, respformat='json', **parameters):
        param = {
            'mimNumber': [mimnumber],
            'format': respformat,
            'include': [],
            'exclude': []
        }
        param = self.__init_param(param, parameters)
        url = 'http://api.omim.org/api/entry'
        self.resp = self.__session.get(url, params=param)
        if respformat == 'json':
            return Entry(self.resp)
        else:
            return Text(self.resp)

    def entries(self, minumbers, respformat='json', **parameters):
        self.resp = []
        url = 'http://api.omim.org/api/entry'
        param = {
            'format': respformat,
            'include': [],
            'exclude': []
        }
        i = 0
        while i < len(minumbers):
            minumbers20 = minumbers[i:i + 20]
            param20 = {
                'mimNumber': minumbers20
            }
            param20.update(param)
            param20 = self.__init_param(param20, parameters)
            resp20 = self.__session.get(url, params=param20)
            self.resp.append(resp20)
            i += 20
        return EntryList(self.resp)
