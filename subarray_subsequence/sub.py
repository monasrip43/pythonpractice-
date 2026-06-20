'''
s="college"
[c]
[co]
[col]
[coll]
[colle]
arr=[1,4,5,6,8,9]
#sub array: it should have a continunity
#derived from continuous part
[1]
[1,4]-->not a sub array
[4,5,6]-->correct sub array
subsequence:
#elements are skipped
#any selected items
[1,4]
concept        subarray          subsequence
continuity        yes               no
skipping allowed   no               yes
order             yes                no
derived from     continuous         selected from any
        
example:
arr=[1,2,4,5,6,7,9,11]
subarray:[1,2,4]X
subarray:[4,5,6,7]correct

subsequence:[1,2,4,5]correct

problem-1:print max sum while the size of the window is taken as input
arr=[2,1,5,1,3,2]
k=3
brute force approach        sliding window approach
1.2 1 5-->8                   previous_sum-outgoing+incoming
2.1 5 1-->7
3.5 1 3-->9
4.1 3 2-->6   time complexityO(n^2)
#sliding window approach
arr[2,1,5,1,3,2]
window 1
2 1 5=8
outgoing=2
incoming=1
next window=8-2+1=7
          =previous_sum+(-outgoing)+incoming
window 2
1 5 1=7   
window=3
5 1 3 =9
next_window=7-1+3=9


'''
#brute force method
# arr=list(map(int,input().split()))
# k=int(input())
# max_sum=0
# #looping for each possible window
# for i in range(len(arr)-k+1):
#   current_sum=0
# #adding the elements
#   for j in range(i,i+k):
#     current_sum+=arr[j]
#   if current_sum>max_sum:
#     max_sum=current_sum
# print(max_sum)
#sliding window approach
# arr=[2,1,5,1,3,2]
# k=int(input())
# window_sum=sum(arr[:k])
# max_sum=window_sum
# for i in range(k,len(arr)):
#     outgoing=arr[i-k]
#     incoming=arr[i]
#     window_sum=window_sum-outgoing+incoming
#     if window_sum>max_sum:
#         max_sum=window_sum
# print(max_sum)
#subarrays
'''
problem-2:find the first continuous subarray whose sum is equals to the target
arr=[1,4,20,3,10,5]
target=33
output:20,3,10
constraint:continous subarray
1.elements should not skipped
2.elements should be adjacent
'''
#brute force
# arr=[1,4,20,3,10]
# target=33
# found=False
# for i in range(len(arr)):
#     current_sum=0
#     for j in range(i,len(arr)):
#       current_sum=current_sum+arr[j]
#       #check for target
#       if current_sum==target:
#         print(arr[i:j+1])
#         found=True
#         break
#       if found:
#          break
#sliding window 
arr = [1, 4, 20, 3, 10, 5]
target = 33
left = 0
right = 0
current_sum = 0
while right < len(arr):
    current_sum += arr[right]
    while current_sum > target:
        current_sum -= arr[left]
        left += 1
    if current_sum == target:
        print(arr[left:right+1])
        break
    right += 1
    '''
arr = [1,4,20,3,10,5]
# R = 0                           r = expand the window
                                  l = shrinking the window
# window                   sum         r increased 
[1] = 1             sum<taget
[1,4] = 5          s<t
1,4,20 = 25         s<t
1,4,20,3 = 28       s<t
1,4,20,3,10 =38     s>t
4,20,3,10 = 37      s>t
20 3 10 = 33      s==t


'''

arr = [1, 4, 20, 3, 10, 5]
target = 33
left = 0
current_sum = 0
for i  in range(len(arr)):
    current_sum = current_sum+arr[i]
    while current_sum > target:
            current_sum = current_sum - arr[left]
            left = left + 1

            if current_sum ==target:
                print(arr[left:i+1])


'''
probem : 3 
find the lengt longest continuous   subarray
that contains no repeating elements

example :
 input : [1,2,3,1,2,3,4]
 output : 4

 keep adding the elements until duplicate found
 brute force
 i = 0
 [1] = unique
 [1,2] = unique
 [1,2,3] = unique
 [1,2,3,1]= duplicate
 


 i = 1
 [2]= unique
[2,3] = unique
[2,3,1] = unique


'''
arr = [1, 2, 3, 1, 2, 3, 4]
max_length = 0
for i in range(len(arr)):
     seen = set()
     for j in range(i,len(arr)):
          if arr[j] in seen:
               break
          seen.add(arr[j])

          max_length = max(max_length,j-i+1)
print(max_length)
           

'''

# window sliding window approach

arr = [1, 2, 3, 1, 2, 3, 4]
l=0
r=0
         L 
         R
[1] = unique
[1,2] = unique
[1,2,3]= unique
[1,2,3,1]= duplicate      r== duplicate(shrink)
[2,3,1]= unique  r =r+1
[3,1,2]= shrinked(unique)
[1,2,3]= shrink(left)-unique
[1,2,3,4] = unique
'''
# arr = [1. 2, 3, 1,2, 3, 4]
# left = 0
# max_length = 0
# seen =set()
# for right in range(len(arr))
# # remove te duplicates
# whie arr[right] in sees
#      seen.remove(arr[left])
#      left = left+1
# seen.add(arr[right])
# max_length = max(max_length)
# print(max_length)

'''

Example  : find the longest substring
without repeating any character

Example 
input: "abcabcbb"
output : 3  --> abc
'''