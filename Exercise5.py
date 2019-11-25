#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:25:46 2019

@author: nada
"""

#Exercises DAY Five

#Exercise 1

class Employee:
    def __init__(self,employeeNumber,name,address,salary,jobTitle):
        self.employeeNumber=int(employeeNumber)
        self.__name=str(name)
        self.__address=str(address)
        self.__salary=float(salary)
        self.__jobTitle=str(jobTitle)
    def getName (self):
        return self.__name
    def getAddress (self):
        return self.__address
    def setAddhress(self,address):
        self.__address=address
    def getSalary (self):
        return self.__salary
    def getJobTitle (self):
        return self.__jobTitle
    def __del__(self):
        print(self.__name+" has been deleted")
    def getemployeeNumber (self):
        return self.employeeNumber

e1=Employee(15,"nada","zarq alhesen blo:125",1500,"BD")
print(e1.getName())
print(e1.getAddress())
e1.setAddhress("my new address")
print(e1.getAddress())
print(e1.getSalary())
print(e1.getJobTitle())

print('-------------------------------')

#Exercise 2

Employee1=Employee(1,"Mohammad Khalid","Amman, Jordan",500,"Consultant")
Employee2=Employee(2,"Hala Rana","Aqaba, Jordan",750,"Manger")
#Exercise 3
print("Employee1 information:")
print("Employee Number:"+str(Employee1.getemployeeNumber()))
print("Name:"+str(Employee1.getName()))
print("Address:" + str(Employee1.getAddress()))
print("Salary:" + str(Employee1.getSalary()))
print("Job Title:" + str(Employee1.getJobTitle()))

print('-------------------------------')

print("Employee1 information:",end="")
print("Employee Number:"+str(Employee2.getemployeeNumber()),end="")
print("Name:"+str(Employee2.getName()),end="")
print("Address:" + str(Employee2.getAddress()),end="")
print("Salary:" + str(Employee2.getSalary()),end="")
print("Job Title:" + str(Employee2.getJobTitle()))


Employee1.setAddhress("USA")
print("Employee1 New Address:"+str(Employee1.getAddress()))


del Employee1
del Employee2