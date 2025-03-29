import numpy as np
import matplotlib.pyplot as plt
from random import *
points=[[randint(-100,100),randint(-100,100)] for _ in range(5)]
pointsdif=[]
plt.figure(figsize=(15, 8))

for x in range(5):
    per=[]
    for i in range(10):
        per.append([points[x][0]+randint(-10,10),points[x][1]+randint(-10,10)])
    pointsdif.append(per)
midpoints=[[sum([x[i][0] for i in range(10)])/10,sum([x[i][1] for i in range(10)])/10] for x in pointsdif]
colors = ['blue', 'red', 'green', 'orange', 'purple']
for x in range(5):
    plt.scatter([pointsdif[x][i][0] for i in range(10)], [pointsdif[x][i][1] for i in range(10)], color=colors[x], alpha=0.6, label='Группа точек ' + str(x + 1))
for x in points:
    plt.scatter(x[0],x[1],color='black', marker='X', s=100, label='Начальные точки')
for i in range(len(midpoints)):
    plt.errorbar(midpoints[i][0],midpoints[i][1],xerr=5, yerr=5, fmt='o', color='black',capsize=5, label='Центральная точка ' + str(i + 1))
print(points)
plt.title('График смещенных точек')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.legend()
plt.axis('equal')

plt.show()