import numpy as np
arr = np.array([1,2,3,4,5,4,4])
newArr = np.where(arr == 4)
print("Printing the index no. of 4 in array.")
print(newArr)

arr_2 = np.array([1,2,3,4,5,6,7,8,9])

print("Printing The Even Number from the array")
newArr_2 = np.where(arr_2%2 == 0)
print(newArr_2)

print("Printing The Odd Number from the array")
newArr_3 = np.where(arr_2%2 == 1)
print(newArr_3)

arr_3 = np.array([6,7,8,9])
newArr_4= np.searchsorted(arr_3,7,side ='right') #counting starts from right to left.
print(newArr_4)