#Bitwise &
#if both the bits are 1 then the result will be 1
'''
A  B    A&B
0  0     0
0  1     0
1  1     1
1  0     0
'''
#print(5&3)
#print(6&2)
'''
real life applications of bitwise operators are in permission systems
masking operations and checking flags
'''

#Bitwise OR
#if any of the input is 1 then the output is 1
'''
A  B   A|B
0  0    0
0  1    1
1  1    1
1  0    1
'''
#example
# print(5|3)
# print(12|4)



#Bitwise XOR
# if we have different inputs then the output is 1
'''
A B A^B
0 0 0
0 1 1
1 1 0
1 0 1
'''
#print(6^2)

#swap the numbers without using the 3rd variable
'''
a = 10
b = 15
a,b = b,a
print(a)
print(b)
'''
#swap the numbers without using the 3rd variable with the help of arithmetic operators
'''
a = 5
b = 3
a=a+b
b=a-b
a=a-b
print(a,b)
'''
#swap the numbers without using the 3rd variable with the help of Bitwise XOR
'''
a=5
b=3
a= a^b
b=a^b
a=a^b
print(a,b)
'''
#Bitwise NOT
'''
if i/p is 1 o/p is 0
if i/p is 0 o/p is 1
'''
#print(~5)# ~n = -(n+1) output is -6
'''
low level memory operations
<< left shift operator
rule --> shift the bits to the left
print(5<<1) ---> output is 10
formula ==> n<<k = n*2^k
'''
#Right shift : shift the bits to the right

#print(8>>1)
#formula: n>>k: n/2^k

