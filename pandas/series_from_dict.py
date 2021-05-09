import pandas as pd
p1 = pd.Series({'a':10,'b':20,'c':30})
print(p1)

print("Changing Index position in a Dictionary.")
p2 = pd.Series({'a':10,'b':20,'c':30},index = ['b','c','d','a'])
print(p2)