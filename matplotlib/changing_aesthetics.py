import numpy as np
from matplotlib import pyplot as plt
p1 = np.array([0,6])
p2 = np.array([0,10])
plt.plot(p1,p2,color = 'g',linestyle = ":",linewidth = 2)
plt.title("Changed color,linestyle and linewidth.",color = "r")
plt.xlabel("X- Axis",color = 'y')
plt.ylabel("Y- Axis",color = 'y')
plt.grid(True)
plt.show()