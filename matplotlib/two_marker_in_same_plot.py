import numpy as np
from matplotlib import pyplot as plt
x = [10,20,30,40,50]
a = [1,7,6,8,9]
b = [7,2,5,6,9]
plt.scatter(x,a,marker = "*",s = 200, c = "b")
plt.scatter(x,b,marker = ".",s = 100, c = "r")
plt.title("Two marker in same plot.")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()