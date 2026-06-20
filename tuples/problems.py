'''
problem-1: sum of the elements
given list of integers,find the sum

'''
# a=[1,2,3]
# total=0
# for i in a :
#     total+=i
# print(total)  #time complexity:O(n)
'''
problem-2: find the max element in a list
'''
# a=[2,3,4,5,6]
# max=a[0]
# for i in a:
#     if i>max:
#        max=i
# print(max)
'''
 problem-3: count the even string in the list  


'''
# a=[1,2,3,4,5,6]
# count=0
# for i in a:
#     if i%2==0:
#         count+=1
# print(count)
'''
proble-4:reverse the list
'''
# a=[1,2,3,4]
# print(a[::-1])
'''
problem-5: remove duplicates
input:[5,6,1,7,7,8]
output:[5,6,1,7,8]
'''
# a=[5,6,1,7,7,8]
# result=[]
# for i in a:
#     if i not in result:
#         result.append(i)
# print(result)
'''
problem-6: find the second largest number in a list

'''
'''
a=[10,40,80,90,30]
largest=float('-inf')
second_largest=float('-inf')
for i in a:
   if i>largest:
      second_largest=largest #-inf
      largest=i
   elif i>second_largest and i!=largest :
      second_largest=i
print(largest)
print(second_largest)

# a.sort()
# print(a[-2])
#for i in a:
'''
'''
problem-7:check if the list is sorted with out using built in keywords   
    
'''

# a=[1,5,6,4,8]
# sorted_list = True
# for i in range(len(a) - 1):
#     if a[i] > a[i + 1]:
#         sorted_list = False
#         break
# if sorted_list:
#     print("List is sorted")
# else:
#     print("List is not sorted")
'''
problem-8:
find the largest odd number in the list.
input =[1,2,4,5,6,9]
output = 9
'''
# s=int(input())
# l=list(map(int,input().split()))
# largest_num = 0
# for i in range(s):
#     if l[i]%2!=0:
#         l[i]<largest_num
#         largest_num=l[i]
# print(largest_num)

'''
problem - 9:
create the list of squares

'''
# a=[1,2,3,4]
# n = []
# for i in a:
#    n.append(i*i)
# print(n)

'''
problem 10:
check whether the given key exist in the list:
b= [10,20,30,40]
key = 30 
output :
element is found

'''
'''
a=[10,20,30,40]
b=int(input())
if b in a:
    print("element found")
else:
    print("element not found")



'''
#problem :11
#find the common elements in the existing lists
# a= [1,2,3,4,5]
# b= [3,4,5,6,7]
#common elements : 3,4,5
'''
a= [1,2,3,4,5]
b= [3,4,5,6,7]
for i in a:
    if i in b:
     print(i,end=" ")
'''
'''
problem 11:
swap the first and last elements in the list
input = 1 2 3 4 5 6
output = [6, 2, 3, 4, 5, 1]
'''
# s=list(map(int,input().split()))
# s[0],s[-1]=s[-1],s[0]
# print(s)

#problem 12:
#find the maximum in a tuple
# t= (10,20,30,40)
# output = 40
'''
t= (10,20,30,40)
max = 0
for i in  t :
    i>max
    max=i
print(max)
'''

#problem - 13: convert the tuple into the list
# t= (10,20,30,40)
# a=(list(t))
# print(a)
'''
problem - 14
find the avg of numbers in the list

Note : take the input from the user in a list.
'''
# n= int(input())
# l=list(map(int,input().split()))
# sum= 0
# for i in l:
#     sum+=i
# avg = sum/n
# print(avg)

'''
problem 15:
find all the odd numbers in the list
note: take the input from the user

'''
# l=list(map(int,input().split()))
# for i in l:
#     if i%2!=0:
#         print(i,end=" ")
'''
problem - 16
sum of the digits of each element in the list
input:[10,20,30,44]
output:[1,2,3,8]
'''
# n=int(input())
# a=list(map(int,input().split()))
# for num in a:
#    temp=num
#    digit_sum=0
#    while temp>0:
#       digit_sum=digit_sum+temp%10
#       temp=temp//10
#    print(digit_sum)


'''
problem - 17:
find the smallest even number in a list
'''
# s=[1,2,3,4]
# smallest=999
# for i in s:
#    if i%2 == 0:
#       if i<smallest:
#          smallest=i
# print(smallest)

#problem - 18:
# n= int(input())
# l=list(map(int,input().split()))
# sum = 0 
# count = 0
# for i in l:
#     sum+=i
#     avg=sum/n
# for j in l:
#     if j>avg:
#         count+=1
# print(avg)
# print(count)

#problem-19: find the difference between largest and smallest number in a list
'''
l=list(map(int,input().split()))
largest = 0
smallest=l[0]
for i in l:
    if i > largest:
        largest = i
    if i < smallest:
        smallest=i
print(largest-smallest)
'''
#problem 20: count the numbers ending with 0
# s=list(map(int,input().split()))
# count = 0
# if i in s:
#     if i%5==0:
#         count+=1
# print(count)

#problem 21: replace the negative numbers with 0's
'''
l=list(map(int,input().split()))
for i in l:
    if i<0:
        i=0
print(l)
'''
#problem 22: product of all elements in a list
# l=list(map(int,input().split()))
# product=1
# for i in l:
#     product=product*i
# print(product)


#problem:23 
'''
print the elements greater than previous element
input: 2 5 3 8 6

5>2 ---> yes
3>5 ---> no
8>3 ---> yes
6>8 ---> no
'''
# n= int(input())
# l=list(map(int,input().split()))
# for i in range(1,n):
#     if l[i]>l[i-1]:
#        print(l[i],end=" ")

'''
problem 24:
count the multiples of 3
input:
[3,5,9,12,14]
output:
3
'''
# n= int(input())
# l=list(map(int,input().split()))
# count=0
# for i in range(n):
#     if l[i]%3==0:
#         count+=1
# print(count)

'''
problem 25:
find the absolute difference between first and last element in a list
input:
[10,25,-30,-40]
output:
10-(-40) == 30

#abs () is used to get the positive values
'''
# n= int(input())
# l=list(map(int,input().split()))
# s=abs(l[0])-abs(l[-1])
# print(abs(s))
'''
problem : 26
print the unique elements
elements which appears only once
input:[1,2,2,3,4,4]
output:[1,3]
'''
# n= int(input())
# l=list(map(int,input().split()))
# count=0
# for i in l:
#     if l.count(i)==1:
#         print(i,end=" ")

'''
problem 27:
move all the negative numbers to the left
given a list of integers,move all the negative numbers to the begining of the list
note:maintain order
input:[1,-2,3,-4,5]
output=[-2,-4,1,3,5]

'''
# l=list(map(int,input().split()))
# a=[]
# b=[]
# for i in l:
#     if i<0:
#         a.append(i)
#     else:
#         b.append(i)
# print(a+b)

'''
problem 28:
find the frequency of the elements
input:[1,2,2,3,3,3]
output:[1,2,3]
'''
# n= int(input())
# l=list(map(int,input().split()))
# freq={}
# for i in l:
#     if i in freq:
#         freq[i] =  freq[i]+1
#     else:
#         freq[i] = 1
# print(*freq.values())
'''    
rotate list by k positions 
given a list and k integer, rotate the list to the left by k positions
examples:input[1,2,3,4,5]
k=2
output=[3,4,5,1,2]
'''
n=int(input())
l=list(map(int,input().split()))
k=int(input())
k=k%n
for i in range(k):
    last=l[-1]
    for j in range(n-1,0,-1):
        l[j]=l[j-1]
    l[0]=last
print(*l)
#using slicing
# n=int(input())
# l=list(map(int,input().split()))
# k=int(input())
# k=k%n
# result=l[-k:]+l[:-k]
# print(result)
#using built in function
'''
n=int(input())
l=list(map(int,input().split()))
k=int(input())
k=k%n
for i in range(k+1):
    first=l.pop(0)
    l.append(first)
print(l)
'''