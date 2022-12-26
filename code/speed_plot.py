import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = (60, 120, 180, 240, 300, 360)
y = (170, 752, 1340, 1778, 2344, 2352)

plt.title('Зависимость скорости от времени до орбиты Земли')
plt.xlabel('Время, с')
plt.ylabel('Скорость, м/c')

ax.plot(x, y, color='grey', linestyle='-', marker='o')
plt.show()
