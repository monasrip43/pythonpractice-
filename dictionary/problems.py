'''
text = "apple banana pineapple strawberry banana apple"
find the frequency of the words in the dictionary

'''
# text = "apple banana pineapple strawberry banana apple"
# words=text.split()
# dict={}
# for i in words:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
# #shallow copy:

# student={
#          "name":"mona",
#            "rollno":6
#            }
# b=student.copy()
# print(b)
# student["rollno"]=9
# print(b)
# c=student
# print(c)
# student["rollno"]=10
# print(c)

# #why dict is faster?
# #hashing  --> dict stores the data in hashtable
# #time complexity : O(1)
# #searching:O(1)
# #inserting,deleting:O(1)
# data = {
#     "a":1,"a":2
# }
# print(data)
'''
create a dict with employee details
now add branch and phone num at a time
fetch all the key and values using loop
make sure to copy before deleting any pair
pop the last added pair
print the pairs before deleting

addon:make the employee a nested dictionary with multiple employee
'''

# employee={"Name":"Monasri","emp_id":234}
# employee.update({"Branch":"ece","Phno":7896745326})
# for key,value in employee.items():
#     print(key,value)
# emp=employee.copy()
# print(emp)
# employee.popitem()
# print(employee)


'''
problem 2:
Group anagram:
input:["eat","tea","tan","ate","nat","bat"]
output:[[eat,tea,ate],[tan,nat],[bat]]

'''
# a=["eat","tea","tan","ate","nat","bat"]
# dict ={}
# for words in a:
#     key="".join(sorted(words))
#     if key in dict:
#         dict[key].append(words)
#     else:
#         dict[key]=[words]
# print(list(dict.values()))
 
nums=[1,1,1,2,2,3]
k=2
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
result=sorted(freq,key=freq.get,reverse = True)
print(result[:k])