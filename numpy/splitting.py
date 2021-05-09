import numpy as np
n1 = np.array([1,2,3,4,5,6])
newArr = np.array_split(n1,3)
print(newArr)
print(newArr[0])
print(newArr[1])
print(newArr[2])