import numpy as np
from matplotlib import pyplot as plt 
student = {"bob":87,"Mad":55,"Sam":27}
names = list(student.keys())
value = list(student.values())
plt.bar(names,value,color = 'r')

#Horizontal bar plot.
# plt.barh(names,value,color = 'r') 

plt.title("Bar Plot")
plt.xlabel("Names")
plt.ylabel("Value")
plt.grid(True)
plt.show()