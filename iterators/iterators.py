'''
Iterators:
gives one element at a time on demand

python refers to the iterators:
memory efficiency
controlled access

iterable: it is a object can be looped
1.list
2.tuple
3.set
4.dict
5.string

examples:
nums = [10,20,30,40]

for x in nums:
print(x)

syntax:
iterable_object=[1,2,3,4]
it = iter(iterable_object)
print(it)

'''
# iterable_object=[1,2,3,4]
# it = iter(iterable_object)
# print(it)
# print(next(it))
# print(next(it))

'''
list
|
iter()
|
iterator()

x=[1,2,3,4]
for a in x:
   print(a)

it = iter(x)
while True:
   try:
      x= next(it)
      print(x)
    except StopIteration:
         break
 

How loop works internally in python?
iterators---> will be used internally
iter(),next()

'''
# x=[1,2,3,4]
# for a in x:
#    print(a)

# it = iter(x)
# while True:
#    try:
#       a= next(it)
#       print(a)
#    except StopIteration:
#       break
   

# nums =[2,3,4]
# it = iter(nums)
# print(next(it))#2
# print(next(it))#3
# print(next(it))#4
# print(next(it))#Stops iteration

# name = "python"
# it = iter(name)
# print(next(it))

# d={"a":10,"b":20}
# it=iter(d)
# print(next(it))
# # print(it)

#Iterator No:
# nums = [i for i in range(100000)]

#huge memory
#iterator approach:
# nums=iter(range(100000))
#only the current element will be processed


#creating a custom iterator count
# class Count:
#     #constructor
#     def __init__(self,limit):
#         self.num=1
#         self.limit=limit

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num>self.limit:
#             raise StopIteration
#         x= self.num
#         self.num+=1
#         return x
# #object creation:
# c=Count(5)
# for i in c:
#     print(i)
'''
class evennumbers:
    #constructor
    def __init__(self,limit):
        self.num=2
        self.limit=limit
#this method makes the object iterable
#it returns the iterator object itself
    def __iter__(self):
       return self
    #next value during the iteration
    def __next__(self):
        if self.num>self.limit:
            raise StopIteration
        x= self.num
        self.num+=2
        return x
#object creation:
c=evennumbers(15)
for i in c:
    print(i)
'''
