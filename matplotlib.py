# https://www.w3schools.com/python/matplotlib_intro.asp 

# type this in turnminal pip install matplotlib
#import matplotlib
#print(matplotlib.__version__)


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6, 8])
ypoints = np.array([0, 250, 300])
plt.plot(xpoints, ypoints)

plt.plot(ypoints, marker = 'o')

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')

plt.show()



#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()



x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
