'''
kadane's algorithm: max sub arrays problems: (it chooses from the previous algorithm or starts a new algorithm)
arr=[2,-1,3,-2,4]

find the contigious subarrays with max sum

sub_array: [-1,3,-2] right
         [2,3] invalid

index i=0
subarrays              sum
[2]                     2
[2,-1]                  1
[2,-1,3]                4
[2,-1,3,-2]             2
[2,-1,3,-2,4]           6

i=1
[-1]                    1
[-1,3]                  2
[-1,3,-2]               0

kadanes algorithm main idea 

at every element we decide

Two choices:
1.continue previous subarray
        (or)
2.start a new subarray

current_sum=-5
next_element=10

-5+10=5
next==10

arr=[2,-1,3,-2,4]

current_sum = 2
max_sum = 2
index : 1
    -1
    choice 1: extend the array
    2+(-1) = 1

    choice 2: start a new array
    -1

current_sum = 1
max_sum = 2

index : 2
      3
choice 1: extend the array
    2+(-1) = 1+3

    choice 2: start a new array
    3

current_sum = 4
max_sum = max(2,4) = 4

index : 3
      -2
choice 1: extend the array
    2+(-1) = 1+3-2=2

    choice 2: start a new array
    -2

current_sum = max(4,2)=4
max_sum = max(4,2) = 4

index : 4
      4
choice 1: extend the array
    2+(-1) = 1+3+(-2)+4=6

    choice 2: start a new array
    4

current_sum = max(4,6)=6
max_sum = max(4,6) = 6


current_sum= max(arr[i],current_sum+arr[i])
max_sum=max(max_sum,current_sum)


'''
#arr=[2,-1,3,-2,4]
# current_sum=arr[0]
# max_sum=arr[0]
# for i in range(1,len(arr)):
#     #either continue with old subarr
#     #or start a new sub arr
#     current_sum=max(arr[i],current_sum+arr[i])
#     max_sum=max(max_sum,current_sum)
# print(max_sum)


'''
problem: maximmum winning streak
a cricket player gains or loses points in each match

positive ---> won points
negative ---> lost points

the coach wants to find the continuous winning streak with maximum performance

but instead of returning the sum ,return the:
maximum score
starting index
ending index

example:

input:
scores = [-2,4,-1,5,-3,2]

output:

maximum score =8
start index = 1
end index = 3

subarray:
[4,-1,5]

'''
# arr=[-2,4,-1,5,-3,2,]
# current_score=arr[0]
# max_score=arr[0]
# start = 0
# end = 0
# temp_start=0
# for i in range(1,len(arr)):
#     if arr[i]>current_score+arr[i]:
#        current_score=arr[i]
#        temp_start = i
#     else:
#         current_score=current_score+arr[i]
#     if current_score>max_score:
#         max_score=current_score
#         start=temp_start
#         end=i
# print(max_score)
# print(start)
# print(end)
# print(arr[start:end+1])

arr=[2,3,-2,4]
