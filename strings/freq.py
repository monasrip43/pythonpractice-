'''
find the frequency of the characters
s="banana"
target = 'a'
frequency = 3
'''
# s= "banana"
# a = s.count("a")
# print(a)
    #or

s=input()
target = input()
count=0
for ch in s:
    if ch == target:
        count=count+1
print(count)