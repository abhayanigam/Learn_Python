import numpy as np 
from matplotlib import pyplot as plt

fruit = ['apple','orange','mango','guava']
quatity = [67,34,100,29]

plt.pie(quatity,labels = fruit,radius = 1) #radius of outer circle.
plt.pie([1],colors = ['w'],radius = 0.5) #radius of inner circle and colour of inner circle, 1 for one value with wwhite color.

plt.show()