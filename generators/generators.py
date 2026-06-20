'''
youtube: doesnt load the whole video
loads by small chunks
when needed

simply generators work in the same format

problem with list:
list=[1,2,3,4,5]
entire list is stored in memory
nums = [i for i in range(100000)]

python consumes:
high memory
slower

generator:
produces the values one at a time
only when it is needed
saves memory

yield keyword;
yield process the function and remembers the state

return:
ends the function
yield:pauses the function
where yield knows where to stop and where to perform

'''

#example 1:
'''
def numbers():
    yield 1
    yield 2
    yield 3
x=numbers()
print(x)#generators object

#access the numbers
print(next(x))
print(next(x))
print(next(x))
print(next(x))#iteration stops
'''
'''
numbers() #call
|
generator created
|
1. first next()
yield 1-->1
function paused

2.second next()
resume from previous position
yield 2-->2
function pause

3.third next()
resume from previous position
yield 3-->3
pause again

generators:
remembers the variables
remember line position
continue from the same place

#diff between return and yield
return                       yield
ends the function      pauses the funtion 
returns single value   will return multiple values
by one value
no state memory         remembers the state
'''
# def test():
#     return 1
#     return 2

# print(test())

#with yield
# def numbers():
#     yield 1
#     yield 2
# for i in numbers():
#     print(i)

#for loop uses iter(),next() internally
#create a generator for even numbers

def evennumbers(limit):
    num = 2
    while num<= limit:
        yield num
        num+=2
x=evennumbers(10)
for i in x:
    print(i)
'''
num = 2 ---> yield 4 --> 4
pause

resume
num = 4 ---> yield 4-->4
pause

resume
num=6 ---> yield 6 --->
pause

#memory efficiency
nums-[i for i in range(100000)]

Generator:


'''    