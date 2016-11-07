# komim
an OMIM API SDK.

一个用于OMIM API 的SDK。

## 警告

未完成，请勿用于重要项目！由于申请的ApiKey已经过期，无法再继续开发，等待申请通过中！

## 依赖

依赖`requests`库，请自行安装

```
pip install requests
```

## 用法

```python
k = komim.Komim('your_ApiKey_here')
r = k.entry('100050')
print(e.mimNumber)
```

申请ApiKey请[前往OMIM官网](https://omim.org/api/)，使用ApiKey实例化`Komim`类就可以用了，如果需要检查你的ApiKey是否可用，请加上`check`属性，不可用将抛出异常

```python
k = komim.Komim('your_ApiKey_here', check=Ture)
```

### 支持OMIM自带的参数

```python
r = k.entry('100050', text=Ture)
```

写上`Ture`的参数为包含（include），需要去除（exclude）的属性请设置为`False`

### 可以控制返回的格式

```python
r = k.entry('100050', respformat='html')
```

参数`respformat`控制返回的文本类型，由于`format`是Python自带的关键词，所以用`respformat`代替。设置了返回格式，结果集的很多方法都不能再使用，请一定注意！！！

### 结果的解析

```python
e = k.entry('100100', all=True)
# 返回的<Entry>对象支持属性访问
print(e.mimNumber)
# 支持以属性访问
print(e['status'])
# 直接获取其字符串表现形式（dict）
print(e.text)
```

### 批量获取

```python
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
```


