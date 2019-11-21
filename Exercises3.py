#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:50:36 2019

@author: nada
"""

#Exercises DAY Third

#Exercise 1

E3= [1,5,9,"nada","mai"]

for item in E3:
    print (item)
    
#Exercise 2

E3= [1,5,9,8,7,5]

print(sum(E3))

#Exercise 3

E3= [1,5,9,8,7,5]

print(max(E3))

#Exercise 4

a = [10,20,30,20,10,50,60,40,80,50,40]
print(list(set(a)))

#Exercise 5

E31= [1,5,9,8,7,5]

if len(E31)>0:
    print("yes have item")
else:
    print("no do not have item")


#Exercise 6

E6= {1,5,9,"nada","mai"}

for item in E6:
    print (item)
   
#Exercise 7

num_set = set([0, 1, 2, 3, 4, 5])

for x in num_set:
    print(x)


#Exercise 8
E7={1,2,1,3,4,5,"nada"}
E3= {1,5,9,"nada","mai"}

print(E7&E3)

#Exercise 9 

setx =set(["green","blue"])
sety =set(["blue","yellow"])
seta=setx|sety
print(seta)

#the output is {'green', 'yellow', 'blue'}

#Exercise 10

seta=set([5,10,3,15,2,20])
print(len(seta))

#the output is 6

#Exercise 11

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}

for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)

#the output is {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


#Exercise 12

a="Hello, World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("H","J"))

#the output is
"""
e
llo
orl
13
hello, world!
Jello, World!
"""


