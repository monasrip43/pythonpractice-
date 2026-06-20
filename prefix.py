'''
prefix sum:
one of the most important technique
used to solve the subarray problems
1.fast range sub queries
2.optimization
3.sliding window's alternative
4.subarray problems
5.competitive programming

it reduces the repeated calculations
improves the time complexity

what is prefix sum?
stores the cumulative sum of the elements from the beginning of the array to every index

arr = [a0,a1,a2,a3.....]
 
then:
prefix[i]=arr[0]+arr[1]+arr[2]+.....arr[i]


problem:

arr=[2,4,1,7,3]
     0 1 2 3 4
Find the sum from index 1-3
'''
# arr = [2,4,1,7,3]
# sum =0
# for i in range(1,4):
#     sum+=arr[i]
# print(sum)

#brute force method:by using pointers
# arr = [2,4,1,7,3]
# l=1
# r=3
# total=0
# for i in range(l,r+1):
#     total+=arr[i]
# print(total)

'''
i=1 total=4 ---> O(n)
i=2 total=5 ---> O(n)
i=3 total=12

sum(1,3)
sum(0,3)
sum(2,3) ---> complexity increases
prefix sum --->

arr = [2,4,1,7,3]

calculate the prefix:
index         arr[i]          prefix[i]
  0             2                2
  1             4              2+4=6
  2             1              6+1=7
  3             7              7+7=14
  4             3              14+3=17

prefix[i] = [2,6,7,14,17]
prefix[0] = 2 sum from 0 to 0
prefix[1] = 6 sum from 0 to 1
prefix[2] = 7 sum from 0 to 2
prefix[3] = 14 sum from 0 to 3
prefix[4] = 17 sum from 0 to 4


prefix sum formula:
sum = prefix[R]-prefix[L-1]

Special case:
if L==0 then directly the sum becomes prefix[R]

#find the sum from 1 t0 3

R=3
L=1

sum = prefix[3]-prefix[0]
sum = 14-2 = 12
'''
# arr = [2,4,1,7,3]
# n=len(arr)
# prefix=[0]*n
# prefix[0]=arr[0]
# for i in range(1,n):
#     prefix[i]=prefix[i-1]+arr[i]
# print(prefix)

# L=1
# R=3
# #range sum
# if L==0:
#       answer=prefix[R]
# else:
#     answer=prefix[R] - prefix[L-1]
# print(answer)

'''
find the multiple range queries


'''
# arr = [2,4,1,7,3,9]
# n=len(arr)
# prefix=[0]*n
# prefix[0]=arr[0]
# for i in range(1,n):
#     prefix[i]=prefix[i-1]+arr[i]
# print(prefix)
# QUERIES= [(1,4),(2,5),(0,3)]
# for L,R in QUERIES:
# #range sum
#     if L==0:
#       answer=prefix[R]
#     else:
#       answer=prefix[R] - prefix[L-1]
#     print(answer)


'''
problem 3:
find the equilibrium index using prefix sum

arr=[1,3,5,2,2]

'''
# arr = [1,3,5,2,2]
# n=len(arr)
# prefix=[0]*n
# prefix[0]=arr[0]
# for i in range(1,n):
#     prefix[i]=prefix[i-1]+arr[i]
# total_sum=prefix[-1]

# for i in range(n):
#     if i==0:
#         left_sum=0
#     else:
#         left_sum=prefix[i-1]
#     right_sum = total_sum - prefix[i]
#     if left_sum==right_sum:
#         print("equilibrium index",i)


