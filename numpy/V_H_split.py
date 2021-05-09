import numpy as np
n1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newArr = np.hsplit(n1,3)
newArr_2 = np.vsplit(n1,3)

print(newArr)
print(newArr_2)