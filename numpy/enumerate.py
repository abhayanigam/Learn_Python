import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print("Enumerating the array :-")
for index,x in np.ndenumerate(arr):
    print(index,x)