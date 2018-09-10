import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from math import sin, cos
import math
import matplotlib.tri as mtri
import numpy as np

N = 100

print '#include "colors.inc"'
print '#include "textures.inc"'
print 'camera { \
    location <2, 2, -6>\
    look_at <0, 0, 0>\
}'
#print 'light_source { <2, 2, -3> color rgb<1, 1, 1> jitter adaptive 1}'
#print 'area_light <5, 0, 0>, <0, 0, 5>, 5, 5'
print 'light_source {\
        <2, 8, -6>\
        color White\
        area_light <1, 0, 0>, <0, 0, 1>, 3, 3\
        adaptive 1\
        jitter\
        }'

print 'background { color rgb<1, 1, 1> }'

print 'plane { <0.5, 1, -0.4>, -4\
    pigment {\
        color White\
    }\
}'


print '#declare Red = texture {\
    pigment { color rgb<0.8, 0.2, 0.2> }\
    finish { ambient 0.2 diffuse 0.5 }\
}'

print '#declare Green = texture {\
    pigment { color rgb<0.2, 0.8, 0.2> }\
    finish { ambient 0.2 diffuse 0.5 }\
}'

print '#declare Blue = texture {\
    pigment { color\
        rgb<0.2, 0.2, 0.8>\
    }\
    finish { ambient 0.2 diffuse 0.5 }\
}'

def get_point(i, j):
    r = max(i % (N / 4), N / 4 + 10 - i % (N / 4)) * 1.0 / (N / 4) + 0.3
    lat = math.pi - math.pi / N * j
    lon = 2 * math.pi / N * i
    x = sin(lat)*cos(lon) * r
    y = sin(lat)*sin(lon) * r
    z = cos(lat)
    return x, y, z 

x = []
y = []
z = []
triangles = []
point = {}
for i in range(N+1):
    for j in range(N+1):
        point[(i,j)] = get_point(i, j)


for i in range(1, N+1):
    for j in range(N+1):
        if (j != 0):
            """ (i,j) -- (i, j-1) -- (i-1, j-1) """
            triangles.append([(i,j), (i, j-1), (i-1, j-1)])
            #if i == 1 and j == 1:
            #    p1, p2, p3 = triangles[-1]
            #    x = [p1[0], p2[0], p3[0]]
            #    y = [p1[1], p2[1], p3[1]]
            #    z = [p1[2], p2[2], p3[2]]
            #    print x, y
        if (j != 0):
            """ (i,j) -- (i-1, j) -- (i-1, j-1) """
            triangles.append([(i,j), (i-1, j), (i-1, j-1)])
            #if i == 1 and j == 1:
            #    print point(i, j)
            #    print point(i-1, j)
            #    print point(i-1, j-1)
            #    p1, p2, p3 = triangles[-1]
            #    x = [p1[0], p2[0], p3[0]]
            #    y = [p1[1], p2[1], p3[1]]
            #    z = [p1[2], p2[2], p3[2]]
            #    print x, y

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
print 'mesh {'
normal = {ij:np.zeros(3) for ij in point.keys()}
for triangle in triangles:
    ij1, ij2, ij3 = triangle
    p1 = np.array(point[ij1])
    p2 = np.array(point[ij2])
    p3 = np.array(point[ij3])
    n = np.cross(p2-p1, p3-p1)
    n = n / np.linalg.norm(n, 2)
    normal[ij1] += n
    normal[ij2] += n
    normal[ij3] += n
    #xx = [p1[0], p2[0], p3[0]]
    #yy = [p1[1], p2[1], p3[1]]
    #zz = [p1[2], p2[2], p3[2]]
    #print xx, yy

for count, triangle in enumerate(triangles):
    ij1, ij2, ij3 = triangle
    p1 = np.array(point[ij1])
    p2 = np.array(point[ij2])
    p3 = np.array(point[ij3])
    n1 = normal[ij1]
    n1 = n1 / np.linalg.norm(n1, 2)
    n2 = normal[ij2]
    n2 = n2 / np.linalg.norm(n2, 2)
    n3 = normal[ij3]
    n3 = n3 / np.linalg.norm(n3, 2)

    print 'smooth_triangle {'
    print '\t<%f, %f, %f>' % (p1[0], p1[1], p1[2])
    print '\t<%f, %f, %f>' % (n1[0], n1[1], n1[2])

    print '\t<%f, %f, %f>' % (p2[0], p2[1], p2[2])
    print '\t<%f, %f, %f>' % (n2[0], n2[1], n2[2])

    print '\t<%f, %f, %f>' % (p3[0], p3[1], p3[2])
    print '\t<%f, %f, %f>' % (n3[0], n3[1], n3[2])
    print '\ttexture { Blue }'
    print '}'

    #try:
    #    ax.plot_trisurf(mtri.Triangulation(xx, yy), zz)
    #except:
    #    continue
print '}'

#ax.scatter(x, y, z, linewidth=2.0, antialiased=True)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
#plt.show()
