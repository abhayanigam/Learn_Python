import numpy as np
n1 = np.array([10,20,30,40])
n2 = np.array([50,60,70,80])

newArr_1 = np.stack((n1,n2))
print(newArr_1)

newArr_2 = np.dtack((n1,n2))
print(newArr_2)

newArr_3 = np.vtack((n1,n2))
print(newArr_3)

newArr_4 = np.htack((n1,n2))
print(newArr_4)