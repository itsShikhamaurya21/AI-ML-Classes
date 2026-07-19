import pandas as pd
import numpy as np

# Series is a one labeled data structure means it returns elements as well as their index
arr=[1,2,3,4]
s=pd.Series(arr)
print(s)


# custom index

b=[1,2,3,4]
sd=pd.Series(b,index=['a','b','c','d'])
print(sd)

# access element by using custom indec=xing
print(sd['a'])
# access element by using position
print(sd.iloc[1])

# Dataframe is two dimensional dat structure that have both row and column labeled

# c=[[1,2,3],[5,6,7],[8,9,0]]
# d=pd.DataFrame(c)
# print(d)

# custom 

c=[[1,2,3],[5,6,7],[8,9,0]]
d=pd.DataFrame(c,index=['a','b','c'])
print(d)

# dictionary

data={
  "name":["shikha","sahil","shital"],
  "age":[22,21,32]
}
d=pd.DataFrame(data,index=["A","B","C"])
print(d)

# d=pd.DataFrame(data)
# print(d.loc[0])

# arr=np.array([2,4,6,7],ndmin=4)
# print(arr)

d=pd.DataFrame(data)
print(d.iloc[[0,1]])

data1={
  "name":["Shikha","Sahil","Mahesh"],
  "age":[21,22,23],
  "city":["Noida","GB","Rajasthan"]
}
print(data1)
d=pd.DataFrame(data1)
print(d.iloc[0])

print(d.iloc[2,2])