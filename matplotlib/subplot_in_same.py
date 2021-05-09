import numpy as np
from matplotlib import pyplot as plt
p = np.array([0,10])
p2 = p*2
p3 = p*3
#       row,colomn,index  
plt.subplot(1,2,1)
plt.plot(p,p2,color = 'b',ls = '-.',linewidth = 2)
plt.title("Line Plot 1",color = "r")
plt.xlabel("X- Axis",color = 'r')
plt.ylabel("Y- Axis",color = 'r')
plt.grid(True)

#       row,colomn,index  
plt.subplot(1,2,2)
plt.plot(p,p3,color = 'y',ls = '-',linewidth = 3)
plt.title("Line Plot 2",color = "r")
plt.xlabel("X- Axis",color = 'r')
plt.ylabel("Y- Axis",color = 'r')
plt.grid(True)
plt.show()