# -*- coding: utf-8 -*-

import numpy as np

array1 = np.array(range(6))
print(array1)
print(array1.shape)  # sharp属性查看数据结构

array1.shape = 2, 3  # 2行3列
print(array1)
print(array1.shape)

array4 = np.arange(13, 1, -1)  # 根据起始值、结束值、步长生成等差一维数组
print(array4)
