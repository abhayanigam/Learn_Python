import numpy as np 
n1 = np.array([10,20])
n2 = np.array([30,40])

print("Sum of n1 and n2:-")
new = np.sum([n1,n2])
print(new)

print("Sum of n1 and n2 row wise :-")
new_2 = np.sum([n1,n2],axis = 0) #axis = 0 (Row / Vertically adding), axis = 1 (Colunm / horizontally adding).
print(new_2)

#Basic adding,substracting,multiplication and division.
n3 = np.array([10,20,30])
n3 = n3+1
print("Adding 1 in n3:-")
print(n3)

n4 = n3-1
print("Substracting 1 in n3:-")
print(n4)

n5 = n3*2
print("Multipling 2 in n3:-")
print(n5)

n6 = n3/2
print("Dividing 2 in n3:-")
print(n6)

#mean 
n7 = np.array([10,20,30,40,50,60])
new_3 = np.mean(n1)
print("Printing the mean value:-")
print(new_3)

#Standard Division.
print("Printing standard division value.")
new_4 = np.std(n7)
print(new_4)