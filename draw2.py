import numpy as np
from math import cos, sin, pi, atan
import matplotlib.pyplot as plt
from matplotlib import colors
import six
from draw3 import *

def func(t):
    k = 2
    return cos(k*t)*cos(t), cos(k*t)*sin(t)

point = []
r = 0.6
N = 100

colors = linear_gradient("#00FFFF", "#FFA500", n=N/4)["hex"]
print colors

for i in range(N):
    p = np.array(func(2 * pi/N * i))
    if np.linalg.norm(p, 2) < r:
        p = p / np.linalg.norm(p, 2) * r
    angle = atan(p[1]/p[0])
    if p[0] < 0.0:
        angle += pi
    
    point.append([p[0], p[1], angle])

point = sorted(point, key = lambda x : x[2] )

point = np.array(point)

plt.xlim(-1.05, 1.05)
plt.ylim(-1.05, 1.05)
plt.axis('off')

#for i in range(N):
#    plt.plot(point[i, 0], point[i, 1], color=colors[i % (N/4)], marker='o')
#plt.savefig('middle.eps')



#"""left partial"""
#for i in range(N/4, N*2/4):
#    plt.plot(point[i, 0], point[i, 1], color=colors[i % (N/4)], marker='o')
#plt.savefig('left.eps')

#"""right partial"""
#for i in range(N*2/4, N):
#    plt.plot(point[i, 0], point[i, 1], color=colors[i % (N/4)], marker='o')
#plt.savefig('right.eps')


plt.figure()
plt.xlim(-1.05, 1.05)
plt.ylim(-1.05, 1.05)
plt.axis('off')
for i in range(N*0/4, N*1/4):
    plt.plot(point[i, 0], point[i, 1], color=colors[i % (N/4)], marker='o')
plt.savefig('1.eps')

plt.figure()
plt.xlim(-1.05, 1.05)
plt.ylim(-1.05, 1.05)
plt.axis('off')
for i in range(N*1/4, N*2/4):
    plt.plot(point[i, 0], point[i, 1], color=colors[i % (N/4)], marker='o')
plt.savefig('2.eps')

plt.figure()
plt.xlim(-1.05, 1.05)
plt.ylim(-1.05, 1.05)
plt.axis('off')
for i in range(N*2/4, N*3/4):
    plt.plot(point[i, 0], point[i, 1], color=colors[i % (N/4)], marker='o')
plt.savefig('3.eps')

plt.figure()
plt.xlim(-1.05, 1.05)
plt.ylim(-1.05, 1.05)
plt.axis('off')
for i in range(N*3/4, N):
    plt.plot(point[i, 0], point[i, 1], color=colors[i % (N/4)], marker='o')
plt.savefig('4.eps')
