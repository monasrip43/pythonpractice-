'''
OOPS:
Object oriented programming(paradigm)

programs are organized using objects
objects contains:
1.data(variables)
2.behaviour(functions/methods)

OOPS not only focuses on functions but also on real world entities.

car --> object
student --> object

each object here:
will have properties and actions
       |                |
    variable          methods

earlier the programming was written without OOPS:
1.difficult to manage the large level projects
2.code duplication
3.less security
4.difficult maintenance

OOPs solve the above problems:
1.Objects 
2.Classes
3.encapsulation
4.Inheritance
5.Abstraction
6.polymorphism

'''
#Procedural programming:
# name="Mona"
# marks = 50
# def display():
#     print(names,marks)
# display()

#OOPs approach:
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print(self.name,self.marks)
# #object:
# s1=student("Mona",50)
# s1.display()
'''
Advantages:
1.code reusability
2.better organisation --> modular and structure
3.security --> encapsulation
4.easy maintenance: update,debug
5.real world modelling
6.scalability: large applications

'''
'''
class: Blueprint of an object
collection of variables and methods??

class: keyword that creates class
classname:identifiers
pass :empty block

'''

# class Employee:
#     comp_name="CIET"
#     emp_name="sanjana"
#     def name(self):
#         print("the company name is :",self.comp_name)
#     def emp(self):
#         print("the employee name is:",self.emp_name)
# e= Employee()
# e1=Employee()
# print(e.comp_name)
# print(e1.emp_name)
# e.name()
# e1.emp()
# print(e)
# print(e1)

'''
constructor: __init__()
special method
automatically called when object is created

used: intializing the object data

'''
# class Student:
#     def __init__(self):
#         print("constructor is called")

# s1=Student()

'''
student()
|
object created
|
__init__ automatically called

if no constructor
manually assigns the value

if yes
automatic initialization

'''
# if no constructor
# manually assigns the value
# class Student:
#     pass
# s1=Student()
# s1.name="megha"
# s1.branch="CSE"

# #example with constructor:
# class Student:
#     def __init__(self):
#         self.name="Mona"
#         self.age=20
# obj1=Student()
# print(obj1.name)
# print(obj1.age)

'''
Instance variables:
variables that belong to an object
seperate copy created for every object

they store:
object_specific data

student  | name |  marks
s1        manish    98
s2        rajesh    99

each object stores its own data

'''
# class student:
#     def __init__(self,name,marks):
#         #instance variables:name,marks(to store the object specific data)
#         self.name=name
#         self.marks=marks
# s1=student("Manish",98)
# s2=student("Rajesh",99)
# print(s1.marks)
# print(s2.marks)
'''
s1 object
------------
name="Manish"
marks=98

s2 object
-------------
name="Rajesh"
marks=99

objects do not share the instance variables
'''
#instance methods
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     #instance methods:
#     def display(self):
#         print(self.name)
#         print(self.marks)
# s1=Student("Rajesh",98)
# s1.display()
'''
s1.display()

Student.display(self)
|
self--> s1
'''

'''
#Dynamic object properties
adding the variables dynamically

class student:
    pass
s1=student()
s1.name="Mona"-->dynamically adding variables

'''
# class student:
#     pass
# s1=student()
# s1.name="Mona"
# s1.marks=99
# print(s1.name)
# print(s1.marks)
'''
class variables:shared among all the objects
'''
# class Student:
#     #class Variable
#     college_name  = "CITY"
#     def __init__(self,Branch):
#         #Instance variable
#         self.Branch=Branch
# #Normal Method
#     def display(self):
#       print(self.college_name)
# s1=Student("cse")
# s2=Student("csd")
# print(s2.college_name)
# print(s1.college_name)
'''
self:refers to current object 
            or
reference variable pointing to current object 

'''
# class Student:
#     def display(self):
#         print("hello")
# s1=Student()
# s1.display()
'''
s1.display()
|
student.display(s1)
|
self-s1(self points to s1)

'''
# class Student:
#     def show(self):
#         print(self)
# s1=Student()
# s2=Student()
# print(s1)
# print(s2)
# s1.show()

#task:


class employee:
    name="SBI"
    @classmethod
    def comp_name(self):
        print(employee.name)
e=employee()
e2=employee()
e.comp_name()
e2.comp_name()

 

#TASK:
# class student:
#     college="CITY"
#     def __init__(self,name,marks):
#         self.name="Mona"
#         self.marks=99
#     def display(self):
#         print(self.name)
#         print(self.marks)
#     @staticmethod
#     def static_method():
    