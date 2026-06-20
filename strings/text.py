'''
Strings are the sequence of characters
enclosed in ---> "",'',''''''
string is always immutable.
                             mutability
                            /         \
                         mutable   immutable
                            |          |
                      can chanage   cannot change

example:
  name = "Manish "
  name[0] = "A" ----> shows error

 #memory space:
 str = S T R I N G
       0 1 2 3 4 5
    #accessing the elements
      str[0] = S ---> as the output
      string slicing:
      str[start,end,step]
    when we have spaces in the string value the index value also counts the spaces

'''
'''
name= "Mona Sri"
print (name)
print(name[1])
print(name[0:5])
'''
'''
str = "college"
       0123456
      -7....-1

str[-1:-4] ---> prints output as "ege"
str[-1] --->  prints last character
str[-2]  ---> prints the second last character
str[10] ----> give the index error / string index out of range
#ommiting start
str[:3] ---> prints the starting three characters
#
str[3:] ---> starts from the 3rd index number upto the end
#step slicing:
str[0:6:2] --->output is "cle"
#reverse your name:
name = "Monasri"
print[::] --> prints fron the end to the starting character

#string traversal:
 name = "Monasri"
         0123456
for i in name():
print(i) # print the characters in the vertical form

name = "Monasri"
for i in range(len(name)):
    print(i,name[i])
#output:
0 M
1 o
2 n
3 a
4 s
5 r
6 i


'''
'''
ch = "monasri"
for i in range(len(ch)):
    print(i,ch[i])
print(ch.upper())#prints all the characters in upper case
print(ch.lower())#prints all the characters in lower case
print(ch.title())#prints the starting letter of each word in upperr case
print(ch.capitalize())#prints the first character in upper case
print(ch.strip())#removes the extra spaces
'''
'''
text = "i love programming"
print(text)
print(text.replace("love","Hate"))
'''
'''
text = "i love programming"
print(text)
replaced_text = text.replace("love","Hate")
print(replaced_text)
'''
'''
fruit="banana"
#find the frequency of "a"
print(fruit.count("a"))

#startswith--->checks if starting with "letter" 
# print(fruit.startswith("M"))
# #endswith-->
# print(fruit.endswith("na"))
# #split()
#text="Python C Java"

#separated=text.split()
# print(separated)
# print(type(separated))
# #Use join
# #python-C-Java
#new="-".join(separated)
# print(new)

# #searching inside the strings
# #find()--->
 #print(new.find("Python"))
# #using membership operator
# print("Python" in new)
# #index()
# text="Python"
# print(text.index("z"))
# #which is safe find() or index?
# #find() is safe to use 
# #string farmatting
name="Vijay"
age=20
#f-string
print(f"My name is {name} and age is {age}")
#old college
print("Name:",name ,"and age is :",age)
#format()
print("Welcom {}",format(name))
#Escaping characters or sequence 
print("hello \n world")
print("Hello \t world")
#R-strings(Regex-regular expressions)
path=r"c://downloads/photos/pic.jpeg"
print(path)
'''
#r--> tells to your interpreter that there are no escaping characters in path

'''
#swapcase()---?
text="PyThon"
print(text.swapcase())
#casefold()-->stronger lower conversion
print(text.casefold())

#center--?
print(text.center(40))
#task:creat a string with your friends 
#name=mounika mona harika
#split the name to store in the list
#join the string "_"
#Traverse over the string and find the index
#of the person name starting with "A"
#print the person name
#count the len of the name & check "a" occurances
#print the frnd name with 30 space in center

'''





#string with your friends names

#name= megha mouni harika

'''
name="Meghana Mounika Harika"
a=name.split()
print(a)
b= "_" .join(a)
print(b)
for i in range(len(b)):
    print(i,b[i])
    if b.startswith("A"):
        print
'''

# #task : print the name in reverse
# #slicing
# name="meghana"
# print(name[::-1])#-->anahgem
# #without using slicing
'''
                            logic
                              |
                  read the characters from the end of the string       (traverse)    
                            |
                        start adding each char(from end) to a string   
                            |
                        print the var
'''
'''
s="HELLO"
#start=4  
#end=-1
#step=-1
reverse=""
for i in range(len(s)-1,-1,-1):
    reverse=reverse+s[i]
    #print("step:",i,"character:",s[i],"Reverse:",reverse)
    print (reverse)
'''
#Problem 2
#Palindrome
n= input()
reverse=""
for i in range(len(n)-1,-1,-1):
    reverse=reverse+n[i]
if reverse == n:
        print("palindrome")
else:
        print("not a palindrome")
print(reverse)
'''
Logic
  |
input a word
   |
reverse the word
    |
compare original and reversed
    |
palindrome or not

'''




