import numpy as np
#using copy will the array to x and then we can change the original one.
arr = np.array([1,2,3,4])
x = arr.copy()
arr[0] = 42
print(arr) 
print(x)

#using view the array will change the view and display both.
arr_2 = np.array([1,2,3,4])
x = arr_2.view()
x[2] = 100
print(arr)
print(x)