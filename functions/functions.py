'''
what is a function?
it is a block of reusable code.performs specific tasks
it is easy to debug the code.

why functions?
1. avoid repetition 
2.improves reusability
3.easy debug
4.modular programming

How to define a function?

def function_name(Parameters):
    """Doc strings"""  --->type of comments used in functions.
    statements
    return value

def -->  it is a keyword 
function_name --> identifiers
parameters ---> passed inside the function (i/p for a function)
return --> output

function calling:
executing the code

function_name()

Functions are       two types
                     /     \
        built in functions  user defined

Built in functions:
which are already defined
example:
print()
input()
sum()
mean()
max()

user defined:
we will create our logic as per our requirement
'''

#create a function :
# def hello():
#     print("hello world")
# #call the function :
# hello()

#parameters: variable passed during the function definition

# def add(a,b): #here a,b are parameters
#     print(a+b)
# #arguments:values passed during the 
# #calling the function:
# add(2,3)


'''
2.keyword arguments:
task:
create a function to calculate simple interest using positional args(ptr/100)

'''
#keyword arguments:
# def sub(a,b): #here a,b are parameters
#     print(a-b)
# sub(b=5,a=10)

# def interest(p,t,r):
#     print( (p*t*r)/100)
# interest(10,2,3)

'''
3.default arguments:
used when value is not provided

example:
def student(name="Mona"):
     print(f"student name is {name}")
'''
# def student(name="Mona",branch="CSE"):
#      print(f"student name is {name} and branch is {branch}")
# student()

'''
create a function to calculate squares by using default parameters:

'''
# def squares(a,b=2):
#      print(a**b)
# squares(5)

'''
4.variable length arguments:

def total(*args):
   print(sum(args))

#call the function:
total(10,20,30,40)
'''

'''
task: create a function to find sum of any number of values
'''
# def total(*args):
#    print(sum(args))
# total(10,20,30,40)

# #keyword length arguments:
# def student_details(**kwargs):
#    print(kwargs)
# student_details(name="rajesh",branch="cse",rollno="9")

#create a function to print employee details
# def emp_details(**kwargs):
#    print(kwargs)
# emp_details(name="rajesh",dept="production",id="9")


#write a function with args and kwargs
# def total(*args,**kwargs):
#     print(args,kwargs)
# total(10,20,30,40,name="rajesh",dept="production",id="9")

'''
difference between the return and print statement

return statement: send the values back to the caller

def add(a,b):
    return a+b
result=add(10,20)
print(result)

print                         |                return
display the output                          sends the value
cannot reuse                                can reuse

multiple return values:
 def calculate(a,b):
     return a+b,a-b,a/b
# it returns the value in the form of tuple

s,sub,div=calculate(20,30)
'''
# def calculate(a,b):
#      return a+b,a-b,a/b
# # it returns the value in the form of tuple

# s,sub,div=calculate(20,30)
# print(s,sub,div)

#create a function which will return multiple values 
# 1.min
# 2.max
# 3.avg
# def function(a,b):
#      return min(a,b),max(a,b),((a+b)/2)
# a,b,c=function(45,50)
# print(a,b,c)
'''
doc strings describes:
1.what function does
2.parameters
3.return value

def add(a,b):
    """This function add two numbers and returns results"""
    return a+b


#def add(a,b):
#     """This function add two numbers and returns results"""
#     return a+b
# print(add._doc_)
# print(help(add))

#task: write a docstring for the simple interest program
# def interest(p,t,r):
#     """ this function will find the interest and return results"""
#     print((p*t*r)/100)
#     print(interest._doc_)
#     print(help(interest))
# interest(2,3,5)
'''
#variable scope:

# def test(): 
#      x=100    --> local variable
#      print(x)
# test()

# x=200  --> global variable
# def show():
#      print(x)
# show()

# x=0
# def update():
#     global x
#     x=x+5
# update()
# print(x)

#task: try without using global and tell the error
# x=0
# def update():
#     x=x+5
# update()
# print(x)

'''
task: create a function bank_transaction()
which accepts:
1.account holder
2.balance
3.transaction type(deposit/withdraw)
4.amount

use: 
default arguments
return statement
global balance

print updated balance
'''
# balance=40000
# def bank_transaction(account_holder,transaction_type,amount,bank_name="SBI"):
#     global balance
#     if balance==0:
#         print("insufficient funds")
#     else:
#         if transaction_type=="withdraw":
#             print(f"{account_holder} updated balance:",balance-amount)
#         else:
#             print(f"{account_holder} updated balance:",balance+amount)
# bank_transaction("rajesh","deposit",34000)

                       #(or)

# balance = 1000
# def bank_transaction(account_holder,transaction_type,amount=0):
#     global balance
#     if transaction_type=="deposit":
#         balance+=amount
#         print(f"{account_holder} deposited{amount}")
#     elif transaction_type=="withdraw":
#         if amount<=balance:
#             balance-=amount
#             print(f"{account_holder} withdraw {amount}")
#         else:
#             print(f"insufficient balance for { account_holder}")
#     else:
#         print("invalid transaction type")
#     print(f"updated balance {balance}")
#     return balance
# bank_transaction("nani","deposit",500)
'''



lambda function: is a small and anonymous function 
# function without name
# defined using lambda
can pass any number of args
can have only one expression 
return the value automatically(no return keyword)

normal function:
def add(a,b):
    return a+b
add(10,20)

#write using lambda 
add =lambda a,b:a+b
#calling the function
add(10,20)

#task: write a normal function to square of num convert the normal fun to lambda

''' 
#using normal function   
# def squares(a,b=2):
#     print(a**b)
# squares(3)

#using lambda function
# print((lambda x:x*x)(5))

# max number in 2
# c-programming
# ternary:?:
# python : if a >b else b
# max_num = lambda a,b:a if a>b else b
'''
arr = list(map(int(input().split())))
#map(): applies the function each element or iterable

map(function,iterable)
example:
def square(x):
     return x*x
num = [1,2,3,4]
result = list(map(square,num))
print(result)

'''
# def square(x):
#      return x*x
# num = [1,2,3,4]
# result = list(map(square,num))
# print(result)

#using lambda function:
# num = [1,2,3,4]
# result=list((map(lambda x:x*x,num)))
# print(result)

'''
task: given list of numbers
convert each number into cubes
using map and lambda

'''
# num = [1,2,3,4]
# result=list((map(lambda x:x**3,num)))
# print(result)

'''
what is a filter?
selects the elements based upon the function
syntax:
filter(function,iterable)

example:
def is_even(x):
    return x%2==0
list=[1,2,3,4,5]
result= filter(is_even,list)
print(result)

'''
# def is_even(x):
#     return x%2==0
# list=[1,2,3,4,5]
# result= list(filter(is_even,list))
# print(result)

#task:given with a list with frnds names
#filter the names letter starting with A
#use filter with lambda
# names=["Akanksha","Anu","Rajesh"]
# result=list(filter(lambda x:x.startswith("A"),names))
# print(result)

'''
what is reduce()?
repeatedly applies the function
reduces the iterable to single value

syntax:
reduce(function,iterable)


'''
#function tools ---> module
from functools import reduce
nums=[1,2,3,4,5]
result=reduce(lambda a,b:a+b,nums)
print(result)
