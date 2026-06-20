#check whether a charcter is a alphabet or not
'''
logic flow:

read the character -->
ASCII ---> chr(ch)/ord(ch)
A-Z ---> 65-90
a-z ---> 97-122
'''
# ch  = input()
# asci = ord(ch)

# if (65<= asci <=90) or (97<=asci<=122):
#     print("alphabet")
'''
find the length of the string
without using len()
Logic:
1. intialize a count = 0
            |
    traverse the string
            |
    increment the counter for each char
            |
    Print(counter)

'''

# s= input()
# length = 0
# for i in s:
#     length+=1
# print(length)

#Toggle each character
'''
pytHON---> PYThon

Logic flow:
traverse each character
        |
if uppercase -> convert to lower
        |
else lowercase -> upper

'''

# string = input()
# r=string.swapcase()
# print(r)

'''
remove the vowels from the string

example: input : hello
output:
      hll
'''

# s=input()
# result =""
# for i in s:
#     if i.lower() not in ['a','e','i','o','u']:
#         result=result+i
# print(result)


#example-5
'''
remove all characters except alphabets

ex:
i/p : "he123@lo"
o/p : "hello"

'''
# s= input()
# result=""
# for i in s:
#     if i.isalpha():
#         result+=i
# print(result)

#remove spaces from the givenstring without using strip
'''
#s=input()
result=""
for ch in s:
    if ch != " ":
        result+=ch
print(result)
'''
#removing the brackets from algebraic expressions
'''
s=input()
result=""
for ch in s:
    if ch not in ["(",")" ,"{","}","[","]"]:
        result+=ch
print(result)
'''
#sum of numbers in a string
'''
logic:
traverse string --> identify digits-->do sum and print
input:hel123o
output: 6

'''
'''
s=input()
result=0
for ch in s:
    if ch.isdigit():
        result=result+int(ch)
print(result)
'''
#capitalize the first and last character of the string
'''
i/p: hello world   
o/p: HellO WorlD
'''
'''
s = input().split()
result=""
for i in s:
    word=i[0].upper()+i[1:-1]+i[-1].upper()
    result=result+word+" "
print(result)
'''
