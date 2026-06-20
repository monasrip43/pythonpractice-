'''
what is a set?

collection of unordered unique elements
unordered
unique(never allow duplicates)
why?
1.fast searching
2.duplicates removal

we store the values directly in the sets
if we have an element in the set the comma(,) is mandatory

how to create a set?

numbers={1,2,3,4}
print(numbers)
'''
#creation of a set
# numbers={1,2,3,4}
# print(numbers)
# numbers={1,2,2,3,5,3,4} #removes the duplicates and prints the output as {1,2,3,4,5}
# print(numbers)
'''
numbers={1,2,3,4,3,4}
unique=set(numbers)
print(unique)

#checks the mutability of the sets
# numbers[0] =3
# print(numbers)

#set is unordered ---> fixed indexing(no)
numbers.add(10)
print(numbers)

#first way to create:
num={1,2,3,4}

#second way to create:
s=set([1,2,3,4,5])
#freq={} ---> empty dictionary

#empty set creation:
s=set()
s.add(1)
print(s)

#adding multiple elements:
s.update([2,3,4,5])
print(s)

#remove the element from the set:
s.remove(2)
print(s)

#discard: removing the element without having any error
s.discard(1)
print(s)

#pop:deletes the random element
s.pop()
print(s)

#clear:clears all the elements
print(20 in s)
'''
'''
what is hashing?
hashing will convert the data into unique hash values

python uses:
1.hash tables
2.hash functions
target = 10
set = {1,2,3,4,10}

unlike linear search it directly jumps intoo location/target
ex: hash(10)

search,insert,delete : O(1) : time complexity
time complexity of list is O(n)

set operations:
operation                symbol
1.Union                     |
2.intersection              &
3.differnce                 -
4.symmetric difference      ^
'''
'''
a={1,2,3,4}
b={5,6,3,7,8}
# print(a|b)
# a.union(b)

# #intersection:
# print(a&b)
# a.intersection(b)

#differnce:
print(a-b)
print(a.difference(b))

#symmeteric difference
print(a^b)
print(a.symmetric_difference(b))
'''
#subset and superset:
# a={1,2}
# b={1,2,3,4}
# print(a.issubset(b))
# print(b.issuperset(a))

# #frozenset:
# fs=frozenset([1,2,3,4,5])
# print(fs)

'''
feature           list        tuple        dictionary           set
ordered           yes           yes            no                no
mutability        yes           no             yes               yes
duplicates        yes           yes        key:no values:yes      no
indexing          yes           yes             no                no

can i store a list inside a set?
1.list
2.dict
3.set


'''

#task: create a list with squares of a numbers
#convert the list with squares of a number to set
#repeat the squares twotimes
#add multiples of 2 to the same set at a single time
# ---> separate the set with 2 different sets multiples of 2
#squares :now perform all the set operations on both sets
'''
s= [1, 4, 9, 16, 25]
s_set = set(s)
s_set.add(4)
s_set.add(9)
multiples = {2, 4, 6, 8, 10}
print("S:", s_set)
print("Multiples:", multiples)
print("Union:", s_set | multiples)
print("Intersection:", s_set & multiples)
print("Difference:", s_set - multiples)
print("Symmetric Difference:", s_set ^ multiples)
'''

#problem:
'''
find the length of longest consecutive sequence
input: [100,4,200,1,3,2]
output: [4] --> 1,2,3,4
'''
s=[100,4,200,1,3,2]
a=set(s)
longest = 0
for i in a:
    if i-1 not in a:
        length=1
    while i+length in a:
        length+=1
    longest=max(longest,length)
print(longest)
