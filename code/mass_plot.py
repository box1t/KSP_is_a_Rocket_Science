import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = (0, 60, 180, 300, 600, 720)
y = (587, 432, 198, 145, 67, 65)

plt.title('Изменение массы ракеты')
plt.xlabel('Время, с')
plt.ylabel('Масса, тонны')

ax.plot(x, y, color='green', linestyle='-', marker='o')
plt.show()
