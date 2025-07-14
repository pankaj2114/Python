print("This lecture about strings and conditional statements")
#######  Strings

str1 = "Hello this is trascend infosystems"
str2 = 'Hello this is my company'
str3 = """Hello this is an IT Company"""

print(str1,str2,str3)
#######   escape sequence character
str4 = "Hello this is transcend \nThis is my company"
print(str4)

#######  string concatinate 
final_string = str1+' '+str2
print(final_string)

#######  Length of a string

print("Length of '",final_string,"' is ",len(final_string))

#######  Indexing of the string
"""
string [Pankaj]
Index  [012345]

in python string can not be modified using indexes
"""

#######  String Slicing 
#accessing the part of the string
"""
Example:
str = "Pankaj"
slice_str = str[startIndex : EndIndex] --always less than EndIndex 
"""
strforslice = "Divyansh"
slice_str = strforslice[0:4]
slice_str1 = strforslice[0:] #if missed endIndex it means last index of string
slice_str2 = strforslice[:5] #if missed startIndex it means start with 0th index of string
print(slice_str) #Output--> Divy
print(slice_str1)
print(slice_str2)

#######  Negative Indexing (It start from last index of the string and start from -1)
"""
[P  a  n   k  a  j]
[-6 -5 -4 -3 -2 -1]
"""
negative_indexing = "Pankaj"
print(negative_indexing[-1])


#######  String Functions  #########

Str_function = "i am Pankaj Kumar Verma. I am learing Python"
print(Str_function.endswith("Python")) #return boolean values
print(Str_function.capitalize()) #create a new capitalize string do not modify original strings
                                 #first letter will be capital and rest all will be in small
print(Str_function.replace("P","S")) 
print(Str_function.find("Python")) #will return Index of first letter
print(Str_function.find("Ankit"))#if not exits then it will return -1

print(Str_function.count("P")) #How many times P exist

        #Read all string functions from google

#WAP to take string Input from user and print its length
# name = input('Enter something: ')
# print(len(name))


############# Conditional statements #############################

#WAP to check eligibility for DL
age = 21
if(age >= 18):
    print("You are eligible")
else:
    print("You are not eligible")

light   = "Red"

if(light == "Red"):
    print("Stop")
elif(light == "Green"):
    print("Go")
elif(light == "Yellow"):
    print("Ready")