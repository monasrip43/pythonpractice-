'''
what is dictionary?
dictionary is unordered
list --> collection of orered elements
mutable ---> can be modified
tuple---> collection of ordered elements
immutable---> cannot be modified

dictionary: collection of key-value pairs
              key:value
              06:"Mona"
              dict:{}

              
dictionary is mutable ,where it can be modified
#where as the keys are immutable and values are mutable
it doesnot allow the duplicates in keys whereas in values they can have the duplicates
no fixed indexing
searching is very efficient :O(1) of time complexity
it uses the hashing technique to search hence O(1)


why dictionary?
1.labels
2.properties
3.mapping the relationships

list=["mona","06",20]
#creation of dictionary:
student={
          "name":"mona",
          "rollno":06,
          "age":20
          }

'''
# student={
#           "name":"mona",
#           "rollno":6,
#           "age":20
#           }
# print(student)

# #2nd method:
# student = dict(name="mona",age=20,branch="cse")
# print(student)

# #3rd method:
# data={}
# print(data)

# #we can access the data using the keys
# #list=[1,2,3,4]
# #list[0]
# #example:
# print(student["name"])

'''
feature                   list            dict
ordered                    yes             no
access(indexing)           yes             no ---->use keys
arr[0](works in)           yes             no ---->student["keys"]

'''
# employee = {}
# employee["name"] = "mona"
# employee["age"] = 20
# print (employee)
# employee["age"] = 21
# print (employee)
# #delete the value:
# employee.pop("age")
# print (employee)


# #dictionary methods:
# #keys(): returns all the keys in the dictionary
# print(student.keys())
# #values() : returns all the valuesin the dictionary
# print(student.values())
# #items(): returns all the items with keys and values in the dictionary
# print(student.items())
# #print(student["Branch"])
# #when i use this-->key error
# #access the elements
# print(student.get("Name"))
# print(student.get("Branch"))
# #None
# #update()-->add multiple elements
# student.update({"Branch":"CSE","College":"CITY"})
# print(student)

# #popitem:removes the last inserted pair
# student.popitem()
# print(student)

# #looping on dictionary
# for i in student:
#     print(i)

# #iterating on values
# for value in student.values():
#     print(value)

# for key,value in student.items():
#     print(key,value) 

# #nested dictionary: dict inside dict
# students={"s1":{"Name":"Rajesh","Branch":"AI"},"s2":{ "Name":"Ravi","Branch":"AIML"}}
# print(students)
# print(students["s1"]["Name"])

# #can i store a list in a dictionary?
# student={
#           "Name": "Monasri",
#           "Marks": [95,99,96,92,95]
# }
# print(student)

#you can also store multiple dictionaries in a list:
students=[
    {"Name":"Rajesh","Branch":"AI"},
    { "Name":"Ravi","Branch":"AIML"}
    ]
print(students[0]["Name"])

#dictionary comprehension: shortcuts for the dictionary
#{key:value for variable in iterable}
squares ={x:x*x for x in range(1,11)}
print(squares)

#rules for Keys:
'''
int
strings
tuple
list --> no (because the list is mutable)
dictionary: no
student={
       1:"meghana",
       "Roll":8,
       (1,2):"tuple",
       [1,2,3]:"list",#mutable
       {"Name":"meghana"}:"hello" #cant use bcz it is both mutable and immutable
       }
'''

