#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:31:48 2019

@author: nada
"""


#Exercises DAY Eight
print('-------------Exercise 1------------------')
import numpy as np
import pandas as pd

data=[2,4,6,8,10]

e1=pd.Series(data)
print(e1)

print('-------------Exercise 2------------------')

d1={'a':100,'b':200,'c':300,'d':400,'e':800}

e2=pd.Series(d1)
print(e2)


print('-------------Exercise 3------------------')
data=[20,10,150,110,100,50]

e3=pd.Series(data)
print( e3.describe())
e3.plot(kind="bar",color=['red','black','green','blue','yellow','blue'])

print('-------------Exercise 4------------------')


Data={
      'd1':[100,200,5,400,700,100,200,50,400,700],
      'd2':[140,0,300,400,200,140,0,700,400,200]
      }
e4=pd.DataFrame(Data)
print( e4.describe())
df4= pd.DataFrame(e4,columns=["d1", "d2"])
df4.plot()
#print(Data)


print('-------------Exercise 5------------------')
sampleData={
        'X':[78,82,96,80,86],
        'Y':[84,94,89,83,86],
        'Z':[86,97,96,72,83]
        }

e5=pd.DataFrame(sampleData )
print(e5)

print('-------------Exercise 6------------------')
'''
names=['Bob','Jessica','Mary','John','Mel']
birth=[968,155,77,578,973]
data=list(zip(names,birth))
df6=pd.DataFrame(data = data, columns=['Names', 'Births'])
print(df6)
plot =df6.plot.pie(y='birth', figsize=(5, 5))
'''

data={
      'names':['Bob','Jessica','Mary','John','Mel'],
      'birth':[968,155,77,578,973]
      }

df6=pd.DataFrame(data)
print(df6)
plot =df6.plot.pie(y='birth', figsize=(5, 5))

print('-------------Exercise 7------------------')
df7=pd.read_csv('ex8.csv',index_col=0)
print(df7)


print('-------------Exercise 8------------------')
dates=pd.date_range('20000101',periods=4)
df= pd.DataFrame(np.random.randn(4, 2), index=dates, columns=['A','B'])
print(df)
print(df.head(2))
print(df[['A']])
print(df[0:1])
print(df['20000102':'20000104'])
print(df.loc['20000102':'20000104',['A']])
print(df.iloc[:,1:2])
print(df[df>0])
print(df[df.B>0])
df['A']=[100,200,300,100]
print(df)
print(df[df['A'].isin([200,300])])
