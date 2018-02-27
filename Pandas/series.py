# -*- coding: utf-8 -*-

import pandas as pd

s1 = pd.Series()  # 创建空Series
print(s1)

s2 = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])  # 通过index和values创建Series
print(s2)
print(s2.values)
print(s2.index)

s2['f'] = 11  # 添加新元素
print(s2)

s3 = pd.Series({'a': 1, 'b': 3, 'c': 5, 'd': 7})  # 通过字典创建Series
print(s3)

s4 = pd.Series([1, 3, -5, 7])  # 通过values创建Series，默认index从0开始
print(s4)

s5 = pd.Series([0, 1, 2, 4, 6, 8, 10, 12])
print(s5.head(3))  # 查看Series的前3个数据
print(s5.tail(3))  # 查看Series的后3个数据
print(s5.take([2, 4]))  # 查看指定索引的数据

print(s2[2])  # 位置索引访问
print(s2['d'])  # 标签索引访问

print(s2[[1, 3, 4]])  # 位置列表索引访问
print(s2[['b', 'd', 'e']])  # 标签列表索引访问

print(s2[0: 4])  # 位置切片
print(s2['a': 'd'])  # 标签切片

dates = ['2016-01-01', '2016-01-02', '2016-01-03']
ts = pd.Series([1, 2, 3], index=pd.to_datetime(dates))  # 时间作为索引
print(ts)

print(ts.shift(1))  # 将数据滞后
print(ts.shift(-1))  # 将数据超前
