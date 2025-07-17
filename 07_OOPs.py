#Object Oriented Programming
"""
Class and Objects (Instance of class)
"""
class Engineer:
    Name = "Ankit Kumar"

E1 = Engineer()
print(E1.Name)

####  Cunstructor (__init__ function)
""" It is call bydefault when we initialize/crate an object of a class  """

#default constructor
class Student:
    def __init__(self): # self is a reference of current object
        print(self) #Output:<__main__.Student object at 0x000002154D973770>
        print("Crating object")
        self.Name = "Hello"  #varialbles are called attributes
        

s = Student()
print(s.Name)

#parameterized constructor
class Transcend:
    def __init__(self,Empcount,yearold):
        self.Empcount = Empcount
        self.yearold = yearold

Tran = Transcend(35,10)
print("Tran emp count: ",Tran.Empcount)
print("Tran Age: ",Tran.yearold)

 ## Class instance and Object Instance 
 # the Instance that has common/same value for all objects is called class instance and
 # then Instance that has different value for all objects is called Object Instance
 # Example is below

class Learner:
    #this is class instance value of institute_name will be same for all objects 
    #Class attribute can be accessed using class name  also(No need to crate instance)
    institute_name = "S.P. Institute of Technology and Management."

    def __init__(self,Learner_Name,Learner_Course,Learner_Cduration):
        #following instances are object instance because value can be varry for all Objects
        self.Learner_Name = Learner_Name
        self.Learner_Course = Learner_Course
        self.Learner_Cduration = Learner_Cduration




Learner1 = Learner("Divyansh","B.Tech",4)
Learner2 = Learner("Divyanshi","B.Tech",4)
Learner3 = Learner("Divya","B. Com",3)
Learner4 = Learner("Divy","BCA",3)
Learner5 = Learner("Ankita","MCA",2)
#Class attribute can be accessed using class name  also
print("Class attribute can be accessed using class name  also: ",Learner.institute_name)

print("---------------------------------------------------")
print("institute_name: ",Learner1.institute_name,"\nLearner_Name: ",
      Learner1.Learner_Name,"\nLearner_Course: ",Learner1.Learner_Course,
      "\nLearner_Cduration: ",Learner1.Learner_Cduration)
print("---------------------------------------------------")
print("institute_name: ",Learner2.institute_name,"\nLearner_Name: ",
      Learner2.Learner_Name,"\nLearner_Course: ",Learner2.Learner_Course,
      "\nLearner_Cduration: ",Learner2.Learner_Cduration)
print("---------------------------------------------------")
print("institute_name: ",Learner3.institute_name,"\nLearner_Name: ",
      Learner3.Learner_Name,"\nLearner_Course: ",Learner3.Learner_Course,
      "\nLearner_Cduration: ",Learner3.Learner_Cduration)

##### Methods
# Methods are functions that belong to objects

class Learners:
    #this is class instance value of institute_name will be same for all objects 
    #Class attribute can be accessed using class name  also(No need to crate instance)
    institute_name = "S.P. Institute of Technology and Management."

    def __init__(self,Learner_Name,Learner_Course,Learner_Cduration):
        #following instances are object instance because value can be varry for all Objects
        self.Learner_Name = Learner_Name
        self.Learner_Course = Learner_Course
        self.Learner_Cduration = Learner_Cduration

    #Method 
    def printLearnersDetails(self):
        print("\n--------Printing Learners Details----------------\n")
        print("institute_name: ",self.institute_name,"\nLearner_Name: ",
                self.Learner_Name,"\nLearner_Course: ",self.Learner_Course,
                "\nLearner_Cduration: ",self.Learner_Cduration)
        print("\n-------Learners Details Printed Successfully-------")

Learner1 = Learners("Divyansh","B.Tech",4)
Learner2 = Learners("Divyanshi","B.Tech",4)
Learner3 = Learners("Divya","B. Com",3)
Learner4 = Learners("Divy","BCA",3)
Learner5 = Learners("Ankita","MCA",2)
#using Methods
Learner1.printLearnersDetails()
Learner2.printLearnersDetails()
Learner3.printLearnersDetails()
Learner4.printLearnersDetails()
Learner5.printLearnersDetails()


######### Static Methods
# Methods that don't use the self parameter (work at class level) 
# we use decorator @staticmethod to create a static methods

class DivyansClass:
    @staticmethod
    def printHello():
        print("Hello Divyansh Class")

Div = DivyansClass()
Div.printHello()        
DivyansClass.printHello() #statics Methods can be access through class name directly

print("oops concepts")

## del keyword

del Learner1.Learner_Name #delete name attribute of Learner1
#print(Learner1.Learner_Name) #Now I cann't access Learner_Name attribute

""" 
Access Modifier
attribute Name -> Public
          _Name -> Protected
          __Name -> Private
"""
#Inheritance
"""
Single Inheritance Toyota(Car) -->Car is parent class
Multi-level Inheritance Fortuner(Toyota)
Multiple Inheritance(Inherite more than one class) Fortuner(Car,Toyota)
"""

# Using Super() method to set the value of parent class attribute 

class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def  stop():
        print("Car stopped..")

class Toyota(Car):
    def __init__(self,name ,type):
        super().__init__(type)
        self.name = name

toy = Toyota("fortuner","electric")
print(toy.name)
print(toy.type)
print(toy.start)
print(toy.stop)



