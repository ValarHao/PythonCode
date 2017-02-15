import matplotlib.pyplot as plt

# x_broad = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_broad = range(1, 11)
y_broad = [30, 31, 31, 32, 33, 35, 35, 40, 47, 62]

# x_join = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_join = range(1, 11)
y_join = [32, 32, 32, 33, 34, 34, 34, 34, 38, 43]
labels = ['64k', '128k', '256k', '512k', '1024k', '2048k', '4096k',
          '8M', '16M', '32M', '64M', '128M', '256M', '512M']
plt.title('broadcast(b) vs join(r)')
plt.xlabel('data size')
plt.ylabel('time(s)')

plt.plot(x_broad, y_broad, 'r', label='broadcast')
plt.plot(x_join, y_join, 'b', label='join')
plt.xticks(x_broad, labels, rotation=0)

plt.legend(bbox_to_anchor=[0.3, 1])
plt.grid()
plt.show()
