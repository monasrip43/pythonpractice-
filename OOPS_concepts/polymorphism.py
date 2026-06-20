'''
what is polymorphism?
poly-->many
morphism ---> forms

same methods / operators will behave different behaviour

example:
print(5+3)#8
print("hello"+"world")#helloworld

same operator
          |
    But different behaviours
types of polymirphism:
1.compliw time 
2.Run time polymorphism

#complie time-- method overloading
#No method overloading in python 
Method overloading:
same method names
     +
different parameters
defaultarguments

# *args ----> var len arguments

# java --> add(int,int)
#      --> add(int,int,int)

python approach:
class calculator:
    def add(self,a,b,c=0):
'''