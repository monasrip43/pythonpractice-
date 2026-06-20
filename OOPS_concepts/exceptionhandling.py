'''
Error:
an error is a problem in the program causing abnormal termination
1.Syntax error
2.Run tine error---->exception
--->occurs while executing the program

Example:
a=10
b=0
c=1a/b --->ZeroDivisionError

3.logic error:
program runs but gives wrong ouput
Example:
print(2*(3+5))

What  is exception handling?
Exception handling is a mechanism to handle run time errors gracefully without stopping the program

without exception:
1.program may crashes
2. poor user experince
3. data loss possible

with exception:
1.program will execute normally
2.proper error message
3.safer application

#Basic xception:
syntax:
keywords:try,catch,finally,raise,else

try:
    risky code
except:
    handling code        
'''
#lets write our first program

# try:
#     num=int(input("Enter a number:"))
#     print(10/num)
# except:
#     print("Some error occcured")    
    
#Risky code will be inside try
#if exception occurs --->except exception
#above is not a good practice
#Hides actual problem
#diificulty to debug
# try:
#     num=int(input("Enter a number:"))
#     print(10/num)
# except ZeroDivisionError:
#     print("cannot divide with 0")
# except ValueError:
#     print("Input should not be string")
            
'''
Common python exceptions:
1.ZeroDivisionError--->Divide with 0
2.ValueError--->Invaild input
3.TypeError--->wrong datatype
4.IndexError--->Invaild Index
5.KeyError--->Ivaild dictionary key
6.FileNotFoundError--->File Missing
7.AttributeError--->Invaild Attribute
8.NameError--->Variable is not defined
'''
#Example:
# try:
#     lst=[10,20,30]
#     index=int(input("Enter the index:"))
#     print(lst[index])
# except IndexError:
#     print("Index out of range") 
# except ValueError:
#     print("Please enter integer")       
    
#Else: if no exception occurs 
'''
try:
    code
except:
    handling
else:
    success block        
'''
                
# try:
#     lst=[10,20,30]
#     index=int(input("Enter the index:"))
#     print(lst[index])
# except IndexError:
#     print("Index out of range") 
# except ValueError:
#     print("Please enter integer")    
# else:
#     print("No exception occured")       

#another example by using else

# try:
#     num=int(input("Enter number:"))
#     result=100/num
# except ZeroDivisionError:
#     print("Zero")
# else:
#     print(result)    
    
'''
finally block executes always
used for:
1.closing files
2.closing database connections
3.cleanup activities

try:
    code
except:
    handling
finally:
    cleanup code
'''
# try:
#     file=open("data.txt")
# except FileNotFoundError:
#     print("File not found") 
# finally:
#     print("Execution completed")           
        
#ATM Machine
# try:
#     print("transaction is processing")
# except:
#     print("transaction failed")
# finally:
#     print("Thanks for using atm")              

# try:
#     a=10/0
# except ZeroDivisionError as e:
#     print("error:",e)   
    
#Nested try blocks
# try:
#     print("outer try")
#     try:
#         num=int(input("Enter number:"))     
#         print(10/num)
#     except ZeroDivisionError as e:
#         print("Error:",e)
# except:
#     print("Outer Exception")       
    
#raise: used to manually
#generate exceptions

# age=int(input("Enter the age:"))
# if age<18:
#     raise ValueError("Age should be 18 or greater")
# print("Eligible")       

#why custom exceptions;

# class MyException(Exception):
#     pass

#Bank application:
# class  InsufficientBalance(Exception):
#     pass
# balance=5000
# withdraw=int(input("Enter the amount"))
# if withdraw > balance:
#     raise InsufficientBalance ("Not enough balance")
# print("Withraw succesful") 

#Task:
# class Panner(Exception):
#     pass
# panner=140
# eat=int(input("Enter the amount"))
# if eat>panner:
#     raise Panner("Not enough")
# print("Panner is avaliable")

#Student Result System
# class Student:
#     def __init__(self,marks):
#         self.marks=marks
#     def calculate_result(self):
#         try:
#             average=sum(self.marks)/len(self.marks)
#             print(average)
#         except ZeroDivisionError as e:
#             print("Error:",e)  
# s1=Student([])  
# s1.calculate_result()

#login system
# class loginsystem:
#     def login(self,username,password):
#         try:
#             if username!="admin":
#                 raise ValueError("invalid username")
#             if password!="admin123":
#                 raise ValueError("invalid password")
#             print("login successful")
#         except ValueError as e:
#             print("error:",e)

#generic exceptions: with the generic exceptions python automatically finds which exception it is 
#without defining them
# try:
#     print(10/0)
# except Exception as e:
#      print(e)
'''
Accept amount balance and withdrawl amount
raise exception if:
1.withdrawl amount is -ve
2.withdrawl amount exceeds balance
3.withdrawl amount exceeds daily limit of 25000
4.display remianing balance if transaction is successful
'''
'''
problem - 2:
An ecommerce company wants to validate the order processing
the system should acccept:
1.product stock
2.payment status
3.delivery address

raise exception if:
1.stock unavilable
2.payment failed
3.address is empty
if all validation pass:
print("order successfully placed")

'''
# class OutOfStockError(Exception):
#     pass
# class PaymentFailedError(Exception):
#     pass
# class InvalidAddressError(Exception):
#     pass
# class Order:
#     def __init__(self,stock,payment_status,address):
#         self.stock = stock
#         self.payment_status = payment_status
#         self.address = address
#     def place_order(self):
#         try:
#             if self.stock <= 0:
#                 raise OutOfStockError("product unavailable")
#             if not self.payment_status:
#                 raise PaymentFailedError("payment failed")
#             if self.address.strip()=="":
#                 raise InvalidAddressError("Address cannot be empty")
#             print("Order placed successfully")
#         except OutOfStockError as e:
#             print(e)
#         except PaymentFailedError as e:
#             print(e)
#         except InvalidAddressError as e:
#             print(e)
# stock = int(input("enter the stock"))
# payment_status = input("payment successful(yes/no)".lower())
# address =input("enter the address")
# payment_status = payment="yes"
# obj= Order(stock,payment_status,address)
# obj.place_order()


            