# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

plt.plot([1, 1, 0, 0, -1, 0, 1, 1, -1])
plt.ylim(-1.5, 1.5)  # 调节Y轴坐标范围
plt.xticks(range(9),  # 修改横坐标标签
           ['2015-02-01', '2015-02-02', '2015-02-03', '2015-02-04',
            '2015-02-05', '2015-02-06', '2015-02-07', '2015-02-08', '2015-02-09'])
plt.title('This is a title')  # 设置标题
plt.xlabel('Date')  # X轴名称
plt.ylabel('Price')  # Y轴名称
plt.grid()  # 显示网格
plt.show()
