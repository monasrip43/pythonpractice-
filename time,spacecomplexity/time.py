'''
Analogy:
you are given with 2 programs where it is generating the same output

how will you decide which one to use:
1.faster program
2. less memory
3. efficient

#algorithemic complexity == efficient
two types:
1.Time complexity: faster results in google

2.Space complexity:
                            Mark-zukerberg --->CSS 20kb
                              /         \
                            A = 19kb    B = 18kb
                             10LPA        30LPA
                    
                users=200cr
                saves 70 lakhs per year

Time complexity?
timecomplexity measures how the running time grows as the size of input

Three techniques are used to measure the time complexity

'''
'''
#stopwatch method
import time
start = time.time()
for i in range(1,1001):
    print(i)
print(time.time()-start)
'''
'''
problems in the above technique
1.diff sys diff time
2.different compiler/interpreters
3.backgrondapps effect time
4.internet/cpu/gpu affect the performance

'''

#technique-2 counting the number of operations
#not measures the time in seconds but counts operation
def c_to_f(c):
    return c*9/5+32
#mul = 1
#div = 1
#add = 1    operations = 3
def mysum(x):
    total = 0
    for i in range(x+1):
        total=total+i
    return total

'''
Notations:
asymptotic notations
1.Big O():calc the upper bound(worst time complexity)
2.omega notation: Best case complexity
3.Theta:avg case complexity

#example:linear search

arr=[1,2,3,4,5,6,7]
arr[0]==target #best case
arr[4]==target #avg case
arr[last]==target #worst case complexity

Big oh:worst Time growth 
Focus:
1.Measuring the scalability
2.Machine Independent
3.focuses on growth
4.ingnores the hardware


def mysum(n):
    total=0  #-->1 op
    for i in range(n+1):
      total=total+i #2 op
    return total
#n--->input
  #num operations 1+2n n=10-->21 operations
Big oh(rules)
1.additive constants(remove)
    #1+2n--->2n
2.multiplicative constans(remove)
   #2n-->n
   time complexity-->O(n)
a=10
b=20
c=a+b
for i in range(1,101):

Nested loops:
for i in range(1,n+1):
    for j in range(i):
        print(i)



equation : n^2+n+10 ---> n^2+n --> O(n^2)
for i in range(1,100):
    print(i)
for j in range(1,50):
        print(j)

n+n ---> 2n  ---> O(n)

#practice:

1. n^2+100000n+3^1000
O(n^2)

2.log(n)+n+4
O(n)

3. 0.0001*n*log(n) + 300n
O(nlog(n))



#complexity classes
1. constant time --> O(1)

_> same time always

arr = [10,20,20]
arr[i]

--> input increase and time stays constant
 
2. Linear time ---> O(n)
 for i in arr:
  print(i)
#grows along with input

3.Quadratic time  ---> O(n^2)
Nested loops:
for i in range(1,n+1):
    for j in range(i):
        print(i)

#outerloop runs n times and inner loop runs n time with outerloops

4.logarithamic time  ---> O(log(n))
Best example:
1.Binary search:
arr = [1,6,8,3,7,10]
arr = [1,6,8,3,7,10]
n/2

#large input : smaller growth
#very efficient

5.linearithmic --> O(n log(n))
#used in industry

6. Exponential: ----> O(2^n)
very slow,not much used
example:recursive fibonacci
dngerous for large input

while n>1:
 n= n//2
#loop dividing   ---> O(log(n))


#space complexity:
measures memory used by the  algorithm
1.input space
2.auxillary space

example:
 a=10
 b=20

 constant space ---> O(1)

example -- 2
arr = [0]*n

linear space  ---> O(n)
 '''