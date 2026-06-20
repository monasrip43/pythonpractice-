'''
what is a program?
A program is a set of instructions stored in a disk

print("hello")

storing on a disk??

what is a process?
when a program starts executing it becomes a process

running?
python hello.py
hello

OS ---> Operating System

chrome:
VS code:
spotify:
each one is a separate process

Characteristics:
1.Independent
2.seperate memory
chrome:1.86GB, VS code:500MB
3.Heavy a weght:
memory allocations
resource allocation
cpu scheduling

what is a thread?
a thread is a smallest unit of execution inside a process

Restaurant == Process
workers inside res = threads

worker1 = taking the orders
worker2 = cooking
worker3 = billing
worker4 = cleaning

visually :
process:
Chrome : 
    +thread1
    +thread2
    +thread3

process              thread
1.independent         part of process
2.Heavy weight         Light weigth
3.separate memory     shared memory
4.slow                 Fast
5.expensive            cheap 
6.communication        difficulty easy
 
 why threads are faster ?
 threads will share the memory
 process needs separate memory allocation

 Concurrency 
 Teacher checking the  notebooks
 student A
 student B
 student C


 concurrency 
A
B
C
A
B
C
one at a time 
rapidly switching 
appears simultaneously

Parallelism:
cashier 1 --> customer 1
cashier 2 ---> customer 2
casheir 3 --->customer 3
truly simultaneous 

cPU 1 ---> Task a
cpu 2 ---> task b
cpu 3 ---> task c

A
B
A
B
A
B

parallelism :
cpu 1 --AAA
Cpu -2 - BBB


one chef cooking
soup
noodles
fried rice

parallelism:
Chef 1 - soup
chef 2 - noodles
chef 3 - fried rice
python threads will use --- Concurrency
due to GIL - Global interpreter lock
'''
#Creation of threads:
# import threading
# #function created(do's nothing)
# def display():
#     print("Hello")
# #thread object (creation)
# t=threading.Thread(target=display)
# #start thread
# t.start()

# #multiple threads
# import threading
# def task():
#     print("thread running")
# t1= threading.Thread(target=task)
# t2= threading.Thread(target=task)
# t3= threading.Thread(target=task)
# t1.start()
# t2.start()
# t3.start()
'''
Multiple thread
   +  t1
   +  t2
   +  t3
   all executes automatically
'''
#threads with loops
# import threading
# def numbers():
#     for i in numbers(5):
#         print(i)
# t=threading.Thread(target=numbers)
# t.start()

#two threads with diff tasks
# def even():
#     for i in range(0,10,2):
#         print("even:",i)
# def odd():
#     for i in range(1,10,2):
#         print("odd:",i)
# t1=threading.Thread(target=even)
# t2=threading.Thread(target=odd)
# t1.start()
# t2.start()
'''
os scheduler decides :
which thread to run first...
'''
# import threading
# print(threading.current_thread())
'''
Naming of threads:
'''
import threading
# def task():
#     print(threading.current_thread().name)
# t1=threading.Thread(target=task,name="student_name")
# t1.start()

#pass arguments to the threads:
# def square(n):
#     print(n*n)
# t=threading.Thread(target=square,args=(5,))
# t.start()

#to delay the threads:
# import time
# print("start")
# time.sleep(3)
# print("end")

#it is used in retrying mechanisms:
# import time
# def task():
#     for i in range(5):
#         print(i)
#         time.sleep(2)
# t= threading.Thread(target=task)
# t.start()
#retry mechanism:
# while True:
#     try:
#         connect()
#     except:
#         time.sleep(5)
'''
Join(): mainthread ---> owner
        workerthread ---> worker

'''
import time
def task():
    time.sleep(3)
    print("threading finished")
t= threading.Thread(target=task)
t.start()
t.join()
print("main thread ends here")
#multiple threads:
# def task(name):
#     print(name,"started")
#     time.sleep(3)
#     print(name,"finished")

# t= threading.Thread(target=task,args=("A",))
# t1= threading.Thread(target=task,args=("B",))
# t.start()
# t1.start()
# t.join()
# t1.join()
# print("All threads completed")

#example on naming threads:
import time
def task():
    print(threading.current_thread().name,"started")
    time.sleep(2)
    print(threading.current_thread().name,"finished")
t=threading.Thread(target=task,name="download thread")
t1=threading.Thread(target=task,name="upload thread")
t.start()
t1.start()