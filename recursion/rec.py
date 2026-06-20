'''

def function_name(parameters):
"""Doc string"""
   statements
   return statement

def ----> keyword
function_name ----> identifier
parameters ----> input
return ----> output

def hello():
    print("hello")
#calling a function:
hello()


what is recursion?
recursion is a programming technique where a function calls itself
to solve smaller version of the same problem

function ---> calls itself ---> again ---> again

1.base case:
condition where the recursion stops

2.recursive case:
function calls itself with a smaller input

'''
# def hello(n):
#     if n==0:
#         return
#     print ("hello")
#     #recursive case/call
#     hello(n-1)
# hello(5)

'''
call stack:
LIFO: last in first out
stores function calls in memory

every function call:
gets added to stack removed after the completion

def fun1()
   print("func1")
   func2()
def func2():
    print("func2")

func1()
'''

# def count(n):
#     if n==0:
#         return
#     print("before:",n)
#     count(n-1)
#     print("after:",n)
# count(5)

'''
count(5) count(4)-->count(3)-->count(2)-->count(1)-->count(0)
fact(5)=fact(n-1)

added in stack and removed from stack if work is done
    0 count(0) #pop #base condition 
    1|count(1)|  #pop After:1
    2|count(2)|  #pop After:2
    3|count(3)|  #pop After:3
    4|count(4)|  #pop After:4
    5|count(5)|  #pop Afer:5


 Before:5 #topbtm flow(going down)
 befor:4
 before:3
 befor:2
 before:1
After:1 #returning phase
After:2
After:3
After:4
After:5

code before recursive call:
--->executes while going down
code after recursive call
--->executes whike returning


5!=5x4x3x2x1
  =(n-1)!*(n-2).........n

fact(n)=fact(n-1)*n

def factorial(n):
    if n==0 or  ==1:
      return 1
    return n*factorial(n-1)

call stack
|  fact(1)    |pop 1 
| fact(2)     |pop 1*2
| fact(3)     |pop 1*2*3
| fact(4)     |pop 1*2*3*4
| fact(5)     |pop 1*3*4*5
'''
#task: sum of n numbers
def sum(n):
    if n==1:
        return 1
        return n+sum(n-1)
sum(5)

#fibonacci series:
#5=5+4+3+2+1
#fib(n) = fib(n-1)+fib(n-2)+.............
# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# fib(5)

#reverse a string:
# def reverse(n):
#     if len(n)==0:
#         return ""
#         return(n[-1:])
# print(reverse("hello"))

'''
prolem 4:
given with n = 1234
perform the sum of all the digits
1234 = 1+2+3+4=10

1234%10---> 4

remove the last digit
1234//10 ---> 123

'''
'''
1234
|
4+digitsum(123)
then:
|

'''
def digit_sum(n):
    if n==0:
        return 0
    return(n%10)+digit_sum(n//10)
print(digit_sum(1234))

