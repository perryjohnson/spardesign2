import numpy as np
import matplotlib.pyplot as plt

dtype = [('x', 'f8'), ('y', 'f8')]

c1 = np.loadtxt('Cylinder.txt', comments='<', dtype=dtype)
c2 = np.loadtxt('SNL-100m-0pt007.txt', comments='<', dtype=dtype)
c3 = np.loadtxt('SNL-100m-0pt009.txt', comments='<', dtype=dtype)
c4 = np.loadtxt('SNL-100m-0pt011.txt', comments='<', dtype=dtype)

plt.figure()
plt.axes().set_aspect('equal')

plt.plot(c1['x'],c1['y'],label='c1')
plt.plot(c2['x'],c2['y'],label='c2')
plt.plot(c3['x'],c3['y'],label='c3')
plt.plot(c4['x'],c4['y'],label='c4')

plt.legend()
plt.show()