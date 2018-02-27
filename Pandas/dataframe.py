# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

dates = ['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04', '2016-01-05', '2016-01-06']
dates = pd.to_datetime(dates)
df = pd.DataFrame(np.random.randn(6, 4), dates, columns=list('ABCD'))
print(df)

print("----------查看前3行数据----------")
print(df.head(3))
print("----------查看后3行数据----------")
print(df.tail(3))
print("----------查看列名----------")
print(df.columns)
print("----------查看行名----------")
print(df.index)
print("----------查看数据----------")
print(df.values)

print("----------对行进行切片----------")
print(df[1:3])
print("----------提取单独一列----------")
print(df['A'])
print("----------提取几列----------")
print(df[['A', 'C']])
print("----------根据条件提取----------")
print(df[df['A'] > 0])

# 通过行和列的标签名来提取相应的数据，主要是运用 df.loc[row_indexer, column_indexer] 进行操作
print("----------提取某一列数据----------")
print(df.loc[:, 'A'])
print("----------提取几列数据----------")
print(df.loc[:, 'A':'C'])
print("----------提取特定行和列----------")
print(df.loc[dates[0:2], 'A':'C'])
print("----------提取特定标量----------")
print(df.loc[dates[0], 'A'])
print("----------根据条件提取----------")
print(df.loc[df.loc[:, 'A'] > 0])

# 通过位置来提取相应的数据，主要是运用 df.iloc[row_indexer, column_indexer] 进行操作
print("----------提取某行数据----------")
print(df.iloc[2])
print("----------提取某列数据----------")
print(df.iloc[:, 2])
print("----------提取某几行和某几列数据----------")
print(df.iloc[[1, 4], [2, 3]])
print("----------切片----------")
print(df.iloc[1:4, 2:4])
print("----------提取特定标量----------")
print(df.iloc[3, 3])
print("----------根据条件提取----------")
print(df.loc[:, df.iloc[3] > 0])

# 广义索引与切片，比标签、位置更为实用
print("----------对行切片----------")
print(df.ix[2:5])
print("----------提取某几行某几列----------")
print(df.ix[[1, 3], 'C'])
print("----------对行与列进行切片----------")
print(df.ix[1:3, 'A':'C'])
print("----------根据条件提取----------")
print(df.ix[1:3, df.iloc[3] > 0])

print("----------转置----------")
print(df.T)  # DataFrame的数据结构是二维的，转置是将行和列对换

print("----------用来操作的一列数据----------")
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20160102', periods=6))
print(s1)
print("----------新增一列----------")
df['E'] = s1
print(df)
print("----------横向合并----------")
df = df[list('ABCD')]
print(pd.concat([df, s1], axis=1))
print("----------纵向合并----------")
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=pd.date_range('20160110', periods=3))
print(df1)
print(df.append(df1))
print(pd.concat([df, df1], join='inner'))
print("----------删除操作----------")
print(df.drop(dates[1:3]))  # 不变动原df
print(df.drop('A', axis=1))  # 不变动原df
del df['A']  # 变动原df
print(df)
print("----------标签索引替换----------")
df.loc[dates[2], 'C'] = 0
print(df)
print("----------位置索引替换----------")
df.iloc[0, 2] = 0
print(df)
print("----------替换整列----------")
df.loc[:, 'B'] = np.arange(0, len(df))
print(df)
print("----------重置索引----------")
new_index = pd.date_range('20160102', periods=7)
print(df.reindex(new_index, columns=list('ABCD')))  # 返回一个新的对象，如果新对象的某个索引值或列名不存在于原对象中，则引入缺失值NaN
