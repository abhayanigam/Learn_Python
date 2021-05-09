import numpy as np 
from matplotlib import pyplot as plt

fruit = ['apple','orange','mango','guava']
quatity = [100,67,34,29]

# plt.pie(quatity,labels = fruit)

# Adding Colour and percentage in pie plot.
plt.pie(quatity,labels = fruit,colors = ['yellow','grey','blue','black'],startangle = 90)

#pull the apple "wedge 0.2 from the center of the pie".
myexplode = [0.2,0,0,0]
plt.pie(quatity,labels = fruit,explode = myexplode,shadow = True)

# Adding list of explanation of each wedge.
plt.legend(title = "Four Fruit")
# plt.legend()

plt.show()