import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = (93, 4000, 22200, 45300, 53300, 52600)
y = (0, 14.65, 21.34, 7.5, 8.7, 0.81)

plt.title('Зависимость ускорения от высоты над уровнем моря до орбиты Земли')
plt.xlabel('Высота, м')
plt.ylabel('Ускорение, м/c^2')

ax.plot(x, y, color='red', linestyle='-', marker='o')
plt.show()
