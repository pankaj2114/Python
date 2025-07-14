 #Functions and Recursion in Python 
def fact(n):
    f = 1
    for i in range (1,n+1,1):
        f *= i
    print(f)

fact(5)

def fact_ret(n):
    f = 1
    for i in range(1, n+1,1):
        f *=i
    return f

fact = fact_ret(6)
print(fact)

##Recursion

def facts(n):
    fact = 1
    if(n == 1):
        return 1
    print("fact :",fact)
    fact = n*facts(n-1)
    return fact 
   
print(facts(5))

def print1_n(n):
    if(n == 0):
        return 
    print("Printing n to 1",n)
    print1_n(n - 1)
    print("Printing 1 to n",n)

print1_n(10)