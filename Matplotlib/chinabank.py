# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

ChinaBank = pd.read_csv('ChinaBank.csv', index_col='Date')
ChinaBank = ChinaBank.iloc[:, 1:]
print(ChinaBank.head())

ChinaBank.index = pd.to_datetime(ChinaBank.index)
Close = ChinaBank.Close  # Close这一列

plt.plot(Close['2014'], label='Close price')
plt.title('ChinaBank price curve')  # 标题
plt.xlabel('Date')  # X轴名称
plt.ylabel('Price')  # Y轴名称
plt.grid(axis='y')  # Y轴辅助线

Open = ChinaBank.Open  # Open这一列
# c图形颜色  'r'red  'k'black  'b'blue  'c'cyan  'y'yellow  'w'white  'g'green
# marker点的形状  '.'点  'o'圆  'x'叉号  'D'钻石  '*'星号
# ls线条类型  '-'实线  '--'虚线  '-.'线点  ':'点线  ' '不画线
# lw线宽
plt.plot(Open['2014'], c='r', marker='.', label='Open price', ls='-', lw=2)
plt.legend()  # 增加Open曲线图例

plt.show()
