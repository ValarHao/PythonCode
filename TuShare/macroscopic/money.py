# -*- coding: utf-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
from pylab import mpl
import pandas as pd

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

fig = plt.figure()
ax1 = plt.subplot(111)

money_supply = ts.get_money_supply()  # 货币供应量
money_supply = money_supply.sort_index(ascending=False)
money_supply.set_index('month', inplace=True)
money_supply.index = pd.to_datetime(money_supply.index)
# print(money_supply)
m2_temp = money_supply.ix[:, ['m2']]
m2 = m2_temp.ix[m2_temp.m2 != '--', :]  # 去除'--'的行
print(m2)
m1_temp = money_supply.ix[:, ['m1']]
m1 = m1_temp.ix[m1_temp.m1 != '--', :]  # 去除'--'的行
print(m1)
m0_temp = money_supply.ix[:, ['m0']]
m0 = m0_temp.ix[m0_temp.m0 != '--', :]  # 去除'--'的行
print(m0)

ax1.plot(m2.m2, c='k', label='M2')
ax1.plot(m1.m1, c='b', label='M1')
ax1.plot(m0.m0, c='g', label='M0')
ax1.set_ylabel(u'货币供应量')
ax1.grid(axis='y')
ax1.legend()

plt.show()
