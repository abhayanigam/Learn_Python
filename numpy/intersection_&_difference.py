import numpy as np
n1 = np.array([10,20,30,40,50,60])
n2 = np.array([50,60,70,80,90])

#checking intersection between n1 and n2.
newArr = np.intersect1d(n1,n2)
print(newArr)

#checking difference between n1 and n2.
newArr_2 = np.setdiff1d(n1,n2)
print(newArr_2)
newArr_3 = np.setdiff1d(n2,n1)
print(newArr_3)