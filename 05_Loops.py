
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
    #print(i)
    i +=1

#Print 100 to 1
i = 100
while( i >= 1):
    #print(i)
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
    #print(i)
    pass

# print 1 to 100
for i in range(1,100,1):
    #print("1 to 100->",i)
    pass

# print 100 to 1
for i in range(100,0,-1):
    #print("100 to 1->",i)
    pass

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

def countDigit(n):        
        count = 0
        if(n == 0):
            print("count is:", 1)
            return
        while(n > 0):
            n= n//10
            count +=1            
        print("count is:",count)

countDigit(0)

def RNumber(n):
    Tmp = 0
    while(n>0):
        Tmp = Tmp*10 + n % 10
        n = n // 10
    return Tmp

n = RNumber(123456789) 
print("Reversed Number: ",n)


#Implementing Binary Search in a sorter list 
def BinarySearch(list,n):
    start_index = 0
    end_index = len(list) - 1
    mid_index = (start_index + end_index) // 2

    while (start_index < end_index):
        if(n == list[mid_index]):
            return mid_index
        elif(n < list[mid_index]):
            end_index = mid_index - 1
            mid_index = (start_index + end_index) // 2
        else:
            start_index = mid_index + 1
            mid_index = (start_index + end_index) // 2
    return -1

sorted_list = [1,5,9,18,79,89,98]
n = 100
Find_Index = BinarySearch(sorted_list,n)
if(Find_Index >= 0):
    print(n,"Found at Index in list :",Find_Index)
else:
    print(n," Does Not Exist in list")


def Selection_Sort(list):
    for i in range(0,len(list),1):
        index = i
        for j in range(i,len(list)-1,1):
            if(list[index] >= list[j+1]):
                index = j+1
        tmp = list[i]
        list[i] = list[index]
        list[index] = tmp

list = [5,4,6,7,0,3,23,43,34,64,75,75,68,2,3,4,7,1,0]
Selection_Sort(list)
print('Using Selection Sort',list)

def Bubble_Sort(list):
    n = len(list)
    for i in range(0,n,1):
        for j in range(0,n-i-1,1):
            if(list[j] > list[j+1]):
                tmp = list[j]
                list[j] =list[j+1]
                list[j+1] = tmp

list = [5,4,6,7,0,3,23,43,34,64,75,75,68,2,3,4,7,1,0]
Bubble_Sort(list)
print("Using Bubble Sort :-",list)

