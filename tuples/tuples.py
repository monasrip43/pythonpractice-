'''
tuple:collection of ordered elements
#immutable:
#tuple:more faster then list
#allows duplicates
t=(1,2,3)
feature    list   tuple
mutable    yes    no
duplicates yes     yes
ordered     yes    yes
performance slow   fast
syntax       []     ()
#indexing:
t=(1,2,3,4)
t[0]-->accessing
'''
'''
t=(1,2,3,3.12)
print(t)
print(t[0])
'''
#check the mutability
#t[0] = 9
#tuple pack and unpack
#packing:

t=(10,20,30)

#unpacking:

a,b,c= t
print(a)
print(b)
print(c)

#Tuple methods:

t.count(10)

t.index(20)
'''
why use tuple ? instead of list
1.if fixed data
list:dynamic data

can tuple consist of a list?
yes

what  is the difference between append and extend?
append:individual elements
extend:multiple elements

i

'''
t=([1,2,3],10,3.14)

t[0].append(20)
print(t)