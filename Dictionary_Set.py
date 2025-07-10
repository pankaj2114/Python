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