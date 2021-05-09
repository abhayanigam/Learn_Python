import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)
y = x*2
# x = np.array([0,6])
# y = np.array([0,10])
plt.plot(x,y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()