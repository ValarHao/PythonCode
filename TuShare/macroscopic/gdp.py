# -*- coding: utf-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

fig = plt.figure()
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

gdp_year = ts.get_gdp_year()  # 年度GDP
gdp_year = gdp_year.sort_index(ascending=False)
gdp_year.set_index('year', inplace=True)
print(gdp_year)

ax1.plot(gdp_year.gdp, c='b', label='GDP')
ax1.set_ylabel(u'国内生产总值')
ax1.grid(axis='y')
ax1.legend()

gdp_for = ts.get_gdp_for()  # 三大需求对GDP贡献
gdp_for = gdp_for.sort_index(ascending=False)
gdp_for.set_index('year', inplace=True)
print(gdp_for)

ax2.plot(gdp_for.end_for, c='k', label=u'消费')
ax2.plot(gdp_for.asset_for, c='b', label=u'投资')
ax2.plot(gdp_for.goods_for, c='g', label=u'净出口')
ax2.set_ylabel(u'三大需求贡献率(%)')
ax2.grid(axis='y')
ax2.legend()

gdp_contrib = ts.get_gdp_contrib()  # 三大产业贡献率
gdp_contrib = gdp_contrib.sort_index(ascending=False)
gdp_contrib.set_index('year', inplace=True)
print(gdp_contrib)

ax3.plot(gdp_contrib.pi, c='k', label=u'第一产业贡献率')
ax3.plot(gdp_contrib.si, c='b', label=u'第二产业贡献率')
ax3.plot(gdp_contrib.ti, c='g', label=u'第三产业贡献率')
# ax3.plot(gdp_contrib.industry, c='r', label=u'其中工业贡献率')
ax3.set_ylabel(u'三大产业贡献率(%)')
ax3.grid(axis='y')
ax3.legend()

plt.show()
