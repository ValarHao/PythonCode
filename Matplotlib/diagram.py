# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ChinaBank = pd.read_csv('ChinaBank.csv', index_col='Date')
ChinaBank = ChinaBank.iloc[:, 1:]
print(ChinaBank.head())

ChinaBank.index = pd.to_datetime(ChinaBank.index)
Close = ChinaBank.Close  # Close这一列
print(Close.describe())  # 计算最小值、最大值、中位数、平均数等信息

# 统计各区间出现的个数
a = [0, 0, 0, 0]
for i in Close:
    if (i > 2) & (i <= 3):
        a[0] += 1
    elif (i > 3) & (i <= 4):
        a[1] += 1
    elif (i > 4) & (i <= 5):
        a[2] += 1
    else:
        a[3] += 1

print(a)

# 绘制柱状图
# plt.bar([2, 3, 4, 5], a, width=1.0, bottom=2.0, color='red', edgecolor='k')
# 绘制水平柱状图
# plt.barh([2, 3, 4, 5], a, height=1.0, color='red', edgecolor='k')
# 绘制直方图
# plt.hist(Close, bins=12, color='red', edgecolor='blue')
# 绘制饼图
# plt.pie(a, labels=('(2, 3]', '(3, 4]', '(4, 5]', '(5, 6]'), colors=('b', 'g', 'r', 'c'))
# 绘制箱线图
prcData = ChinaBank.iloc[:, :4]
data = np.array(prcData)
plt.boxplot(data, labels=('Open', 'High', 'Low', 'Close'))

plt.show()
