'''
what is list?
list:collection of ordered elements
                          mutability
                          /       \
                    can modify  cant modify
list is  mutable:
allows dublicate?
yes list allows duplicates

#list is dynamic in size
#syntax:
list_name=[elements]


'''
'''
numbers=[10,20,30,40]
print(numbers)
print(type(numbers))
data=[10,10.4,"python",True]
print(data)
#accessing the elements
a=[10,20,30,40]
print(a[0])
#check mutability
a[0]=60
print(a)
#negative indexing
a=[10,20,30,40]
print(a[-1])
#slicing:
#list[start:end:step]
print(a[0:3])
print(a[:3])
print(a[::2])
#list methods
#append:adds at the end
b=[10,20]
b.append(30)
print(b)
#extend: adds multiple values
b.extend([40,50,60])
# print(b)
# #insert-->add the elements at specific index
# b.insert(2,25)
# print(b)
# #remove:removes the elements
# b.remove(20)
# print(b)
# #pop:removes the elements with index
# b.pop(0)
# print(b)
# #clear()---->deletes all  elements
# # b.clear()
# # print(b)
# #index():returns the position
# print(b.index(25))
# #count: counts the occurances of the elements
# print(b.count(25))
# #reverse():
# b.reverse()
# print(b)
# #copy()
# c=b.copy()
# print(c)
# #sorting in list
# a=[5,0,2,4,3,1]
# #sort()--->sorts in ascending order
# a.sort()
# print(a)
# #descending order
# a.sort(reverse=True)
# print(a)
# #sort=sorts same list  vs sorted:creates a new list
# b=sorted(a)
# print(b)

'''



'''
Task:
1.create a list with 5 bestfriends
2. add a new friend just introduced
3.remove the 2 frnds just had a fght
4. add three close friends at a single time
5. delete the friend at index 5
6.copy the friends list in a new list
7. 
'''
Friends=["ramesh","somesh","ganesh","dinesh","mahesh"]
print(Friends)
Friends.append("suresh")
print(Friends)
Friends.remove("ramesh")
Friends.remove("somesh")
print(Friends)
Friends.extend(["mouni","mona","hari"])
print(Friends)
Friends.sort()
print(Friends)
Friends.pop(4)
print(Friends)


'''
nested list:
#nested list?
a=[[1,2,3],[4,5,6]]
print(a[0][0])
print(a[1][1])
#iterating over the list
a=[10,20,30,40]
for i in a:
    print(i)
#range
for i in range(len(a)):
    print(a[i])
#list comprehension:
#[expression for variable in iterable]
#example:
squares=[x*x for x in range(1,6)]
print(squares)
'''