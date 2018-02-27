# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3], index=list('ABC'))
print(s1)
s2 = pd.Series([4, 5, 6], index=list('BCD'))
print(s2)

print("----------Series间运算----------")
print(s1 + s2)

print("----------DataFrame与Series运算----------")
df1 = pd.DataFrame(np.arange(1, 13).reshape(3, 4), index=list('abc'), columns=list('ABCD'))
print(df1)
print(df1 - s1)

print("----------DataFrame间运算----------")
df2 = pd.DataFrame(np.arange(1, 13).reshape(4, 3), index=list('bcde'), columns=list('CDE'))
print(df2)
print(df1 * df2)

print("----------函数应用----------")
df0 = pd.DataFrame(np.random.rand(6, 4), index=pd.date_range('20160101', periods=6), columns=list('ABCD'))
print(df0)
print(df0.apply(max, axis=0))
# 自定义函数应用
f = lambda x: x.max() - x.min()
print(df0.apply(f, axis=1))

