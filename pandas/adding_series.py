import pandas as pd
p1 = pd.Series([1,2,3,4,5,6,7,8,9])
print(p1+5)

print("Adding two Series :")
p2 = pd.Series([10,20,30,40])
p3 = pd.Series([20,30,40,50])
print(p2+p3)