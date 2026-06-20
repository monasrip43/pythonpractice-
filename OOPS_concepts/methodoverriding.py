'''
what is method overriding?
redefining a parent class method inside the child class

-same method name
-same parameters

child class method changes the behaviour of the parent class method

speak()

'''
# class animal:
#     def sound(self):
#         print("animal makes sound")
# class dog(animal):
#     #same method name as parent class
#     def sound(self):
#         print("dog barks")
# d1=dog()
# d1.sound()

'''
dog object calls sound()
  |
python will search inside the dog class
  |
method found
  |
parent ignored

Animal
sound()
   | overriding by
  dog
    sound()

important rule: method names should be same

'''
'''
super():super function

accessing the parent class methods

'''
# class parent:
#     def show(self):
#         print("parent method")
# class child(parent):
#     def show(self):
#         #calls the parent method
#         super().show()
#         print("child method")
# class grandchild(child):
#     def show(self):
#         #calls the parent method
#         super().show()
#         print("grandchild method")        
# c1=grandchild()
# c1.show()

# is it possible to override the constructor
# class parent:
#     def __init__(self):
#         print("parent constuctor")
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("child constructor")
# c1= child()

# class parent:
#     def __init__(self,name):
#         self.name=name
# class child(parent):
#     def __init__(self,name):
#         super().__init__(name)
#         print(self.name)
#         print("child constructor")
# c1= child("mona")
# print(c1.name)

'''
MRO:
Method resolution order
order in which python searches method
'''
class A :
    def show(self):
        print("class A")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
d=D()
d.show()
print(D.mro())
