'''
what is abstraction?
hiding the internal implementation details
showing the essential features to the user
              (or)
what operation is done?
but not:
how operation is working internally
-->complexity is hidden form the user

what use abstraction?
1.reduces the complexity
2.improvers the security
3.better maintenance
4.cleaner code 
5.standardization 

#abstraction in python
python supports abs using:
abstract classes
abstract methods

#ABC Module
ABC-- Abstract Base Class

abstract class
blueprint of a class
cannot create objects directly

#defins basic common structure 

abstract can have:
1.abs methods
2.normal methods

#abs method
Methods declared but:
     implementation not provided

child class must implement it
Example:
vehicle

->start()



'''
#ABC -->Abstract Base Class
from abc import ABC,abstractmethod
# #abstract class
# class Vehicle(ABC):
#     #abstract method
#     @abstractmethod
#     def start(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("Car started")
# c1=Car()
# c1.start()

#example-2:
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class dog(Animal):
#     print("dog barks")
# d1=dog()
# d1.sound()

#multiple abstract methods

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class rectangle(shape):
#     def area(self):
#         print("area formula")
#     def perimeter(self):
#         print("perimeter formula")
# r=rectangle()
# r.area()
# r.perimeter()

# class paymentgateway(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     @abstractmethod
#     def refund(self,refund):
#         pass
# #child1 
# # class creditcardpay(paymentgateway):
# #     def pay(self, amount):
# #         print(f"pay {amount} using credit card")
# #     def refund(self, refund):
# #         print(f"refund {amount} using UPI")
# # class Upipay(paymentgateway):
# #     def pay(self,amount):
# #         print(f"paid {amount} using upi")
# #     def refund(self,amount):
#         print(f"refund {amount} to upi")
# cc = creditcardpay()
# upi = Upipay()
# c1=creditcardpay()
# c2=Upipay()

# c1.pay(5000)
# c2.refund(6000)