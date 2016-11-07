# -*- coding:utf-8 -*-
"""
@author: 杨满球（本地）
@file: example.py
@time: 2016/11/7 10:53
"""
import os
import komim

apikey = os.environ.get('OMIM_APIKEY')
# 准备好ApiKey然后生成Komim对象
k = komim.Komim(apikey)
# 利用mimNumber获取一个entry
e = k.entry('100100')
# 支持OMIM原始的参数，详见https://omim.org/help/api
# include的参数设置为True
# exclude的参数设置为False
e = k.entry('100100', all=True)
# 返回的<Entry>对象支持属性访问
print(e.mimNumber)
# 支持以属性访问
print(e['status'])
# 直接获取其字符串表现形式（dict）
print(e.text)
print('#############################')
mims = ['100050', '100070', '100100', '100200', '100300', '100500', '100600', '100640', '100650', '100660', '100670',
        '100675', '100678', '100680', '100690', '100700', '100710', '100720', '100725', '100730', '100735', '100740',
        '100790', '100800', '100820', '100850']
print(len(mims))  # len(mims)>20
# 批量获取多个entry,OMIM原生每次支持20个，这里可以一次多个
# 不建议数量过多，因为实际是分多次获取后合并，可能耗时较久或者中途请求失败
es = k.entries(mims)
print(len(es))
print(es.version)
print(es.text)
# 返回的<EntryList>对象可通过索引访问
print(es[0].mimNumber)
# 返回的<EntryList>对象可迭代
for e in es:
    print(e.mimNumber)
