# -*- coding: utf-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
from pylab import mpl
import pandas as pd

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

fig = plt.figure()
ax1 = plt.subplot(111)

cpi = ts.get_cpi()  # 居民消费价格指数
cpi = cpi.sort_index(ascending=False)
cpi.set_index('month', inplace=True)
cpi.index = pd.to_datetime(cpi.index)
print(cpi)
ppi = ts.get_ppi()  # 工业品出厂价格指数
ppi = ppi.sort_index(ascending=False)
ppi.set_index('month', inplace=True)
ppi.index = pd.to_datetime(ppi.index)
print(ppi)

ax1.plot(cpi.cpi, c='b', label='CPI')
ax1.plot(ppi.ppi, c='g', label='PPI')
ax1.set_ylabel(u'价格指数')
ax1.grid(axis='y')
ax1.legend()

plt.show()
