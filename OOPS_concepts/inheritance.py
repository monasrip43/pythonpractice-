'''
what is inheritance?
a mechanism where one class acquires the properties and methods of another class
                              or
one class reuses the features of another class

simple understanding
a child class can

use variables
use methods
of parent class without rewriting the code

example:
vehicles:
car bus bike

all vehicles have start(),stop()
no need to write repeated code

write code once
|
use nums of times

advantages or why?
1.code reusability
2.reducing the code duplication
3.better organisation of code
4.easy maintenance

terms:
parent:base or super class
child:sub class /derived

                    parent
                      |
                    child


'''
#syntax:
# class Parent:
#     pass

# class Child(Parent):
#     pass

# #basic example:
# #parent class
# class Animal:
#     def eat (self):
#         print("animal is eating")
    
# #child class
# class Dog(Animal):
#     pass

# d1=Dog()
# d1.eat()
'''
Dog class doesnot contains eat()
               |
python searches in animal class
                |
method is found and executed
'''

#no inheritance
# class dog:
#     def eat(self):
#         print("eating")
# class cat:
#     def eat(self):
#         print("eating")

# #with inheritance:
# class animal:
#     def eat(self):
#         print("eating")
# class dog(animal):
#     pass
# class cat(animal):
#     pass
# c1=cat()
# c1.eat()
# #accessing the parent variables:
# class person:
#     def __init__(self):
#        self.name="glory"
# class student(person):
#     pass
# s1=student()
# print(s1.name)
'''
Type of inheritance in python
1.Single inheritance
2.Multiple inheritance
3.Multilevel inheritance
4.Hierarichal inheritance
5.Hybrid Inheritance

1.Single inheritance:
one child class inherits from one parent class
         parent
           |
        child
'''
#example:
# class Animal:
#      def eat(self):
#           print("eating")
# class Dog(Animal):
#      def bark(self):
#           print("Barking")
# d1=Dog()
# d1.eat()
# d1.bark()
'''
2.Multiple inheritance:

one child class inherits from multiple parents

             parent 1              parent 2
                |                    |
                       child

'''

#example:
# class father:
#     def money(self):
#         print("fathers money")
# class mother:
#     def gold(self):
#         print("mothers gold")

# class child(father,mother):
#     pass
# c1 = child()
# c1.gold()
# c1.money()

'''
3.multilevel inheritance:
 
inheritance chain of multiple levels
                  Grandparent
                       |
                     parent
                       |
                     child

'''
# class grandparent:
#     def house(self):
#         print("grandparents house")
# class parent(grandparent):
#     def car(self):
#         print("parents car")
# class child(parent):
#     def bike(self):
#         print("childs bike")

# c1=child()
# c1.house()
# c1.car()
# c1.bike()

'''
4.hierarchical inheritance:

multiple child classes inherit from ne parent
             parent
             /\
     child 1   child 2
'''

# class Animal:
#     def eat(self):
#         print("eating")
# class dog(Animal) :
    


# class A:
#     def show_a(self):
#         print("class A")
# class B(A):
#     def show_b(self):
#         print("class B")
# class C(A):
#     def show_c(self):
#         print("class C")
# class D(B,C):
#     def show_d(self):
#         print("class D")
# d1=D()
# d1.show_a()
# d1.show_b()
# d1.show_c()
# d1.show_d()

'''
problem 1:
create a parent class Animal
with method sound()
that should print animal makes sound

'''
# class Animal:
#     def sound(self):
#         print("animal makes sounds")
# class dog(Animal):
#     def show(self):
#         print("dog barks")
# c1=dog()
# c1.sound()



#problem 2:

# class college:
#     college_name="CITY"
# class student(college):
#     def __init__(self,student_name):
#         self.student_name=student_name
#     def display(self):
#         print(self.college_name)
#         print(self.student_name)
# s=student("Mona")
# s.display()      

'''
problem 3:
create:
vehicle class with method start()
car class inheriting the vehicle
sportscar inheriting the car
add method:
speed()
'''
# class vehicle:
#     def start(self):
#         print("start")
# class car(vehicle):
#     pass
# class sportscar(car):
#     def speed(self):
#         print("spaortscar is too good")
# s=sportscar()
# s.speed()
# s.start()

'''
problem 4:
employee  skillsystem 
create:
class programmer with method coding()
class designer with method designing()

create a child class employee inheriting both classes
call both methods using employee objects
'''
# class programmer:
#     def coding(self):
#         print("coding")
# class designer:
#     def designing(self):
#         print("designer")
# class employee(programmer,designer):
#     pass
# e=employee()
# e.designing()
# e.coding()

'''
problem - 5:
employee bonus management:
A company wants to calculate the yearly bonuses for 
different types of employees
create a base class employee
with 
name , salary
create method:
calculate bonus()

then create two child classes 
developer
bonus = 20%of salary
manager
bonus = 35% of salary

write a program to :
take employee details as input
create objects base on employee type
display:
employee name
role 
bonus amount

input:
role,name,salary

output:
name:<name>
role:<role>
bonus:<bonus>

sample:
3
developer  rahul 50000
manager    sneha 80000
developer  arjun 60000

output:
Name:Rahul
Role:Developer
Bonus:10000.00

'''
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def calculate_bonus(self):
#         return 0
# class Developer(Employee):
#     def calculate_bonus(self):
#         return self.salary*0.20
# class Manager(Employee):
#     def calculate_bonus(self):
#         return self.salary*0.35
# n=int(input())
# employees=[]
# for _  in range(n):
#     role,name,salary=input().split()
#     salary=int(salary)
#     if role=="Developer":
#         emp=Developer(name,salary)
#     elif role=="Manager":
#         emp=Manager(name,salary)
#     employees.append((role,emp))
# for role,emp in employees:
#     print(f"Name:{emp.name}")
#     print(f"Role:{role}")
#     print(f"Bonus:{emp.calculate_bonus()}")
#     print()


'''
#PROBLEM 6:
Online course Access System
An online learning platform provides 
different levels of course access
create a parent class Course: with
-> Student_name 
create a method:
access_level():
Then create two child classes 
->FreeCourse
Access Level = "Limited Access"
->Premium Course 
Acess Level = "Full ACcess"
write a program:
1.Accept student details 
2.Create objects using inheritance 
3.Print Student access information

input:course_type,student_name

sample:
4
Free Amit
Premium Neha
Free Rohan
Premium Rakesh

output:
Student:Amit
Course_type:Free
Access:Limited Access
'''
class course:
    def __init__(self,student_name):
        self.name=student_name
    def Access_level(self):
        return "no access"
class freecourse(course):
    def Access_level(self):
        return "limited access"
class premiumcourse(course):
    def Access_level(self):
        return "full access"
n=int(input())
students=[]
for _  in range(n):
    student_name,course_type=input().split()
    if course_type=="free":
        student=freecourse(student_name)
    elif course_type=="premium":
        student=premiumcourse(student_name)
    students.append((course_type,student_name))
for student in students:
    print(f"Name:{student.student_name}")
    print(f"course_type:{course_type}")
    print(f"Access:{student.Access_level()}")
    print()