# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

ChinaBank = pd.read_csv('ChinaBank.csv', index_col='Date')
ChinaBank = ChinaBank.iloc[:, 1:]
print(ChinaBank.head())

ChinaBank.index = pd.to_datetime(ChinaBank.index)
Close = ChinaBank.Close
Open = ChinaBank.Open

fig = plt.figure()  # 创建Figure对象

# 坐标点法
# ax1 = fig.add_axes([0.1, 0.1, 0.3, 0.3])  # 绘图区域，(0.1, 0.1)为左下角坐标，0.3为X长度，0.3为Y长度
# ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.4])
# 子图法
ax1 = plt.subplot(211)  # 子图排队为2*1，当前为第一个图
ax2 = plt.subplot(212)  # 子图排队为2*1，当前为第二个图

Close15 = Close['2015']
Open15 = Open['2015']
ax1.plot(Close15, color='k', label='Close price')
ax1.plot(Open15, color='r', label='Open price')
ax1.set_title('ChinaBank 2015 Close price')
ax1.set_ylabel('Close price')
ax1.legend()

Volume15 = ChinaBank.Volume['2015']
left1 = Volume15.index[Close15 >= Open15]
hight1 = Volume15[left1]
ax2.bar(left1, hight1, color='r')
left2 = Volume15.index[Close15 < Open15]
hight2 = Volume15[left2]
ax2.bar(left2, hight2, color='g')
ax2.set_title('ChinaBank 2015 Volume')
ax2.set_ylabel('Volume')

plt.show()
