import numpy as np
from matplotlib import pyplot as plt
p = np.array([0,10])
p2 = p*2
p3 = p*3
plt.plot(p,p2,color = 'b',ls = '-.',linewidth = 2)
plt.plot(p,p3,color = 'y',ls = '-',linewidth = 3)
plt.title("Two line in same plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()