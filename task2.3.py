
import matplotlib.pyplot as plt
from random import *


y = [randint(2, 5) for _ in range(10)]
y1 = [randint(2, 5) for _ in range(10)]
y2 = [randint(2, 5) for _ in range(10)]
y3 = [randint(2, 5) for _ in range(10)]

fig = plt.figure(layout="constrained")
ax_array = fig.subplots(2, 2, squeeze=False)
#
# plt.title('matan')
ax_array[0,0].stairs(y, linewidth = 3, color = 'b')
ax_array[0,1].stairs(y1, linewidth = 3, color = 'r')
ax_array[1,0].stairs(y2, linewidth = 3, color = 'g')
ax_array[1,1].stairs(y3, linewidth = 3, color = 'purple')

ax_array[0,0].set_ylim([2, 5])
ax_array[0,1].set_ylim([2, 5])
ax_array[1,0].set_ylim([2, 5])
ax_array[1,1].set_ylim([2, 5])

ax_array[0,0].set_title('Линейная алгебра')
ax_array[0,1].set_title('Химия')
ax_array[1,0].set_title('Матанализ')
ax_array[1,1].set_title('ВвАРКТ')

plt.show()
