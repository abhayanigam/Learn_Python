# List is an ordered sequence of items. 
# It is one of the most used datatype in Python and is very flexible. 
# All the items in a list do not need to be of the same type.

# Declaring a list is pretty straight forward. 
# Items separated by commas are enclosed within brackets [ ].

# For Integers
a = [5,10,15,20,25,30,35,40]

# or  

# For Strings
a1 = ['Apple', 'Kiwi','Banana', 'Pinapple','Orange']

print("a[2] = ", a[2])

print("a1[2] = ", a1[2])

print("a[0:3] = ", a[0:3])

print("a1[0:3] = ", a1[0:3])

print("a[5:] = ", a[5:])

print("a1[5:] = ", a1[5:])


# User Define List 

arr = []

n = int(input("Enter the size of arr : "))

for i in range (0,n):
    element = int(input("Enter the element No. %d : " %(i+1)))
    arr.append(element)

print(arr)