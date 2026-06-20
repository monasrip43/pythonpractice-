'''
two pointers:
one pointer is start
one pointer is end
it is used to write the code in an optimal way

operations:
swapping
moves towards center 
arr=[1,2,3,5,7,10,11,15]


'''
# n=int(input())
# l=list(map(int,input().split()))
# target=15
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             print(l[i],l[j])
'''
arr =[1,2,3,5,7,10,11,15]
n=len(arr)
target = 15
for i in range(n):
    for j in range(i+1,n):
        current_sum=arr[i]+arr[j]
        if current_sum == target:
            print("pair found:",current_sum)
'''
# arr =[1,2,3,5,7,10,11,15]
# target = 15
# left=0
# right=len(arr)-1
# while left<right:
#     current_sum = arr[left] + arr[right]
#     if current_sum == target:
#         print("pair is found:",arr[left],arr[right])
#         break
#     elif current_sum < target:
#         left+=1
#     else:
#         right-=1
'''
problem: Reverse a list
Note: use two pointers approach
example:
input:[1,2,3,4,5]
output:[5,4,3,2,1]
'''
# l=list(map(int,input().split()))
# left=0
# right=len(l)-1
# while left<right:
#   l[left],l[right]=l[right],l[left]
#   left+=1
#   right-=1 
# print(l)
'''
problem-2:chech an array is palindrome using two pointers
'''
# l=list(map(int,input().split()))
# left=0
# right=len(l)-1
# palindrome=True
# while left<right:
#     if l[left]!=l[right]:
#         palindrome=False
#         break
#     left+=1
#     right-=1
# if palindrome:
#     print("palindrome")
# else:
#     print("Not palindrome")
'''
problem-3:moves zeroes to the end of the list
input:[1,0,4,-2,0]
output:[1,4,-2,0,0]

'''
# l=list(map(int,input().split()))
# left=0
# for right in range(len(l)):
#     if l[right]!=0:
#         l[left],l[right]=l[right],l[left]
#         left+=1
'''
problem 4:
sort the binary array:
input:[1,0,0,1,1,0,1]
'''
l=list(map(int,input().split()))
left = 0
right = len(l)-1
