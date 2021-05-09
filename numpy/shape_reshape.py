import numpy as np
n1 = np.array([[1,2,3],[2,3,4]])
print(n1.shape)

#reshape the array.
n1.shape = (3,2)
print(n1.shape)

n2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr = n2.reshape(4,3)
print(newArr)

#Converting a multidimensional array into 1D array.
n3 = np.array([[1,2,3,4],[0,9,8,7,6]])
newArr_2 = n3.reshape(-1)
print(newArr_2)