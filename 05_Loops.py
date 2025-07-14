
#Loops in Python
#While Loop
str = "Pankaj"
i = 5
while(i):
    print(str)
    i = i-1

#Print number from 1  to 100
i=1
while( i <= 100):
    print(i)
    i +=1

#Print 100 to 1
i = 100
while( i >= 1):
    print(i)
    i -=1

#print table of a number entered by the user
# n = int(input("Enter Number "))
n = 5
i = 1
while(i<=10):
    print(n*i)
    i+=1

#Print list items using while loop
list = [4,6,"pankaj",False,"Hero","Honda","Bajazre"]
print(type(list))
i = 0
while i < len(list):
    print(i,' Item of list',list[i])
    i+=1

## Search Items in a tuple
i = 0
x = 0
tuple = (1,3,4,5,6,3,4,7,8,9,0)
while(i < len(tuple)):
    if(tuple[i] == x):
        print(x," Find at index=> ",i)
        break
    else:
        print("finding.....")
    i+=1
print('End of finding loop')


##For loop
##print tuples element using for loops

tuple = (1,3,4,5,6,3,4,7,8,9,0)
for elements in tuple:
    print('tuple elements using for loops-> ',elements)

#printing list using for loops
for elements in list:
    print("Elements of the loop using the for loop-> ",elements)

## Use of For else

##Search element in tuple using for else
n = 22
for elements in tuple:
    if(elements == n):  
        print(n,"found")
        break
    print("Finding...")
else:
    print('No. not found')

## Print 1 to 100 using for loop
for i in range(101): #start from 0 bydefault
    print(i)

# print 1 to 100
for i in range(1,100,1):
    print("1 to 100->",i)

# print 100 to 1
for i in range(100,0,-1):
    print("100 to 1->",i)

# pass in loop 
#If we do not want to perform any task inside the loop then we use pass
#otherwise it will raise an error

for i in range(100):
    pass


#Write a program to find the sum of first N natural numbers
#Use while loop

sum = 0
n = 2
for i in range(n+1):
    sum += i
print("sum of first n natural numbers: ",sum)

sum = 0
i = 1
while i <= n:
    sum+= i
    i+=1

print("sum of first n numbers using while loop:",sum) 


## Find factorial of a natural number 
fact = 1
n = 5
#using for  loop
for i in range (n,0,-1):
    fact *=i
print("Factorial of " ,n," = ",fact)

#using while loop
while n <= 1:
    fact *= n
    n -=1
print("factorial of ",n,"is ",fact,"using for loop")