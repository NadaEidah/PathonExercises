#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:10:30 2019

@author: nada
"""

#Exercises DAY Four

#Exercise 1

o=lambda x=1,y=2,z=3:x+y+z
print(o())
print(o(10))
print(o(10,20))


#output is 
#like i put input in the print
"""
6
15
33
"""

#Exercise 2
#240
"""
def multiplyList (w):
    mul=1
    for x in w:
        mul=mul*x
    return mul
e2=[5,8,1,2,3]
print(multiplyList((e2)))
"""

from functools import reduce
e2=[5,8,1,2,3]
zz= reduce(lambda r,t: r*t,e2)
print(zz)


#Exercise 3

lambdaFan = lambda a,b: a*b
print(lambdaFan(5,5))


#Exercise 4

q4 = list(filter(lambda x: x<0,range(-5,5)))
print(q4)


#Exercise 5

x= lambda a,b,c:a+b+c
print(x(5,6,2))

#output is 

"""
13 
"""

#Exercise 6

x=("Joey","Monica","Ross")
y=("Chandler","Pheobe")
z=("David","Rachel","Courtney")
result = list(zip(x,y,z))
print(result)

#output is 

"""
[('Joey', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]
"""
#Exercise 7

coin=("Bitcoin","Ether","Ripple","Litecion")
code=('BTC','ETH','XRP','LTC')
d=dict(zip(coin,code))
print(d)

#output is 

"""
{'Bitcoin': 'BTC', 
'Ether': 'ETH', 
'Ripple': 'XRP', 
'Litecion': 'LTC'}
"""
#Exercise 8

def fun(variable):
    letter=["a","e","i","o","u"]
    if(variable in letter):
        return True
    else:
        return False
    
sequence=['g','j','e','j','k','o','p','r','a']
filtered=list(filter(fun,sequence))
print(filtered)

#output is 
"""
['e', 'o']
"""

#Exercise 9

x=list(map(int,input("Enter a multiple Value:").split()))
print("List of students::",x)

#output is 
#splits that string into a list of parts. If you don't give any arguments, it splits on any whitespace.
"""
Enter a multiple Value:1 20 10
List of students:: [1, 20, 10]
"""

#Exercise 10

def newfun(a):
    return a*a
x=list(map(newfun,(1,2,3,4)))
print(x)

#output is 
"""
[1, 4, 9, 16]
"""

#Exercise 11

def func(a,b):
    return a+b 
a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)

#output is 
"""
[3, 6, 8]
"""

#Exercise 12
c=map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3,4)))
print(list(c))

#output is 
"""
[6, 8]
"""

#Exercise 13
c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
print(list(c))

#output is 
"""
[4, 6, 8]
"""

#Exercise 14
from functools import reduce
e14=[5,7,4,8,9]
print (reduce(lambda a,b : a if a < b else b,e14))

#output is 
"""
4
"""
#Exercise 15

number=[1,2,3]
letters=['a','b','c']

e15=list(zip(number,letters))

print(e15)


