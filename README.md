# komim
an OMIM API SDK.

一个用于OMIM API 的SDK。

## 警告

未完成！由于申请的ApiKey已经过期，无法再继续开发，等待申请通过中！

## 依赖

依赖`requests`库，请自行安装

```
pip install requests
```

## 用法

```python
k = komim.Komim('your_ApiKey_here')
r = k.entry('100050')
print(r.len_entry())
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

参数`respformat`控制返回的文本类型，由于`format`是Python自带的关键词，所以用`respformat`。设置了返回格式，结果集的很多方法都不能再使用，请一定注意！！！

### 结果的解析支持多种读取方式

```python
#以类属性来读取
r.entryList
#以函数返回
r.entry_list()
#用Key来取得对应属性
r['entryList']
```

### 也可以直接获得返回对象（requests库的返回对象）

```python
#获得请求方法对象
r.resp
#获得返回的文本
r.text
#获得二进制形式
r.content
```



