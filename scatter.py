import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,])
y = np.array([3,5,7,8,9,])

plt.scatter(x,y, color='hotpink')

x = np.array([10,11,12,13,14,])
y = np.array([20,21,22,23,24,])

plt.scatter(x,y, color='green')

plt.show()
