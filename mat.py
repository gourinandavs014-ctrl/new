import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10, 20, 70,200])
ypoints = np.array([20, 30, 150, 200])


plt.plot(xpoints,ypoints, marker='o')


plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("simple Line Plot")


plt.grid()


plt.show()