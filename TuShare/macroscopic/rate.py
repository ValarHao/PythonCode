# -*- coding: utf-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
from pylab import mpl
import pandas as pd

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

fig = plt.figure()
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

deposit_rate = ts.get_deposit_rate()  # 存款利率
deposit_rate = deposit_rate.sort_index(ascending=False)
deposit_rate.set_index('date', inplace=True)  # 将date列作为索引
deposit_rate.index = pd.to_datetime(deposit_rate.index)
# print(deposit_rate)
half_year_deposit_rate = deposit_rate.ix[deposit_rate.deposit_type == u'定期存款整存整取(半年)', ['rate']]
# print(half_year_deposit_rate)
call_deposit_rate = deposit_rate.ix[deposit_rate.deposit_type == u'活期存款(不定期)', ['rate']]
# print(call_deposit_rate)

ax1.plot(half_year_deposit_rate.rate, c='k', label=u'半年定期存款')
ax1.plot(call_deposit_rate.rate, c='b', label=u'活期存款')
ax1.set_ylabel(u'利率(%)')
ax1.grid(axis='y')
ax1.legend()

loan_rate = ts.get_loan_rate()  # 贷款利率
loan_rate = loan_rate.sort_index(ascending=False)
loan_rate.set_index('date', inplace=True)
loan_rate.index = pd.to_datetime(loan_rate.index)
# print(loan_rate)
half_year_loan_rate = loan_rate.ix[loan_rate.loan_type == u'短期贷款(六个月至一年)', ['rate']]
# print(half_year_loan_rate)

ax1.plot(half_year_loan_rate.rate, c='r', label=u'半年短期贷款')
ax1.legend()

rrr = ts.get_rrr()
rrr = rrr.sort_index(ascending=False)
rrr.set_index('date', inplace=True)
rrr.index = pd.to_datetime(rrr.index)
print(rrr)
now_rrr = rrr.ix[:, ['now']]
print(now_rrr)

ax2.plot(now_rrr.now, c='g', label=u'准备金率')
ax2.set_ylabel(u'准备金率(%)')
ax2.grid(axis='y')

plt.show()
