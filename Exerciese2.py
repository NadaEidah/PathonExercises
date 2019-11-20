#Exercises DAY TWO

#Exercise 

nub1 = int(input(" What is number one? "))
nub2 = int(input(" What is number tow? "))

if nub1>nub2:
    print(nub1,nub2)
else:
    print(nub2,nub1)
    
#Exercise 2
nub = int(input(" Input a number: "))
for x in range(1,11):
    if nub>0:
        print(nub*x)
 


#Exercise 3
for x in range(6):
    for y in range(x):
             print("*",end="")
    print()   
for z in range(5 -1):
    for f in range(4 -z):
        print("*",end="")
    print()     

         
#Exercise 4
letters =["x","y","z","a","b","c"]
for i in letters:
    if i=="a":
        continue
    elif i=="c":
        break
    print(i)
# the output is x y z b
    
#Exercise 5
for x in range (12,25,3):
    print(x)
# the output is 12 15 18 21 24 
    
 #Exercise 6
i=1
while i<6:
    print(i)
    if i == 3:
        break
    i +=1
# the output is 1 2 3 


 #Exercise 7
gg = int(input(" What is number to sum? "))
s=0
for x in range(0,gg+1):
    s=x+s
print(s)
 
 #Exercise 8 
e8= int(input(" What is number? "))

if e8%2==0:
    print("even")
else:
    print("odd")

 #Exercise 9 
for t in range(17):
    for s in range(17-t):
        print(' ',end='')
    for v in range(t):
            print("*",end=' ')
    print(" ") 
for z in range(18-1):
    for f in range(17 -z):
        print("*",end=" ")
    print() 
for x in range(-16):
    for y in range(x+1):
             print("*",end=" ")
    print("")   


#Exercise 10
#e9= int(input(" What is number? "))
while True:
    try:
        e9 = input("Please enter an integer: ")
        e9= int(e9)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")

#Exercise 11

'''
try :
   a=3
   if a<4:
       b=a/(a-3)
       print ("value of b= ",b)
except ZeroDivisionError:
       print(NameError)
print("/nError Occured and Handled")
'''
