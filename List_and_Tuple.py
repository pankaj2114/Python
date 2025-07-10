#list is a mutable datatype

list = [5,5,1,4,5]
print(list[-2])
print(list)
# list[2] = "Chopada"
print(list)

###### List Methods  ##############

list.append(5)
print(list)
# list.clear()
print(list)
list1 = list.copy()
print("List1",list1)

list.sort()
print(list)

# print(list.count())
list.reverse()
print(list)
print(list.index(1))
print(list.insert(1,0))
print(list )

print(list.remove(0)) #remove value return None
print(list)
print(list.pop(3)) #remove from index and return value
print(list)

####tuples
#tuples are immutable data type in python like string

tuple = (1,2,3,4,4,"pankaj")
print(tuple)
tuple1 = (1)
print(type(tuple1)) #will be treated as integer
tuple1 = (1,)
print(type(tuple1))
print(tuple[0:4])

print(tuple.index(4))
print(tuple.count(0))

### WAP to take input of three fav movie name from user and store this into a list

movie = input("Enter first movie name: ")
list = [movie]
movie = input("Enter second movie name: ")
list.append(movie)
movie = input("Enter third movie name: ")
list.append(movie)
print(list)

## WAP to check the list contains palindrom of elements or not
list_oof_elements = [1,"4",1]
palindrom  = list_oof_elements.copy()
palindrom.reverse()

if(list_oof_elements == palindrom ):
    print("Yes")
else:
    print("No")
