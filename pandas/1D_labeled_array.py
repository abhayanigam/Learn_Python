import pandas as pd
p1 = pd.Series([10,20,30,40])
print(p1)
print(p1[0])
print(p1[2])
print(p1[-3:]) #p1[:4]

print("Changing Index.")
p2 = pd.Series([10,20,30,40],index = ['a','b','c','d'])
print(p2)