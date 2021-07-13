# perfomr slicing on data and display age of client 5
import pandas as pd

df1=pd.DataFrame([['ms',21,'lkn'],['stw',20,'lkn'],['dr',19,'hmr'],['ms',21,'lkn'],['stw',20,'lkn'],['dr',19,'hmr']],index=['client1','client2','client3','client4','client5','client6'],columns=['name','age','city'],dtype=int)
# above is data frame
print(df1)
print(df1.iloc[4:5]["age"])
