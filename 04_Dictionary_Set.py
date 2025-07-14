#Dictionary is Used to store data in the form of key value pair
#It is mutable we can modify Dic
#Key must be unique

Dic ={
    "Name":"Unknown",
    "Age":5,
    "Subjects":["Hindi","English","Math","Science"],
    "isvalid":False,
    "topics":("datatype","variables")
}
print(type(Dic))
print(Dic)
print(Dic["Subjects"])
print(Dic["topics"])
Dic["Name"] = "Pankaj"
Dic["SName"] = "Verma"
print(Dic)
print(Dic["Age"])

#Nested Dictionary
Students = {
    "Name":"Arjun",
    "Age":23,
    "Marks":{
        "Hindi":95,
        "English":98,
        "Math": 100,
        "Science":88
    }
}

print("Marks in hindi",Students["Marks"]["Hindi"])

#Doctionary functions
print(Students.keys())
print(Students.values())
print(Students.items()) #will return each key and value means all Item of dictionary
print(Students.get("Name"))#It will return value of passed key
                           #if not exist then it will return none
print(Students.pop("Name"))
print(Students)

print(~(~2))
print( (1 + 2j) * (3 + 4j))

Students.update({"Name":"Arjun"})
Students.update({"Name":"Karan"})
Students.update({"City":"Delhi"})
print(Students)



#Set in python
#set is the collection of the unordered items.
#Each element in the set must be unique and immutable but set is Mutable

Set_collection = {1,5,6,3,2,1}  #will ignore duplicate values will not raise error
print(Set_collection)

Set_collection1 = {"Pankaj","Verma",4.54,True,6}
print(Set_collection1)

#To Create empty set
Set_empty = set()

#Set Methods
Set_empty.add("Kumar")
print(Set_empty)

#Union Intersection