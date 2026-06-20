'''
File Handling:
files helps to store the data permanently.

it is aprocess of :
creating files
reading files
writing files
updating files

why file handling?
1.store data permanently
2.data sharing is possible
3.reports/logs can be generated

Types of files???
text files:
1. .txt
2. .py
3. .csv
4. .json
Binary files
images
videos
pdf's

#opening the files:
syntax:
file = open("Filename","mode")

'''
#r: will tell the python that line doesn't have any escaping characters
# file = open(r"C:\Users\Lenovo\OneDrive\Desktop\pythoncrt\recursion\recursion.py","r")
# print(file)

'''
file modes:
Mode         Meaning
r            Read
w            write
a            append
x            create
r+           read+write
w+           write+read
a+           append+read
rb           read binary
wb           write binary

'''
#write mode ---> w

# file = open(r"C:\Users\Lenovo\OneDrive\Desktop\pythoncrt\recursion\recursion.py","w")
# file.write("Hello Students")
# file.close()

#creates file if not exist
#deletes the old and add the new content

#append mode ---> adds the data at the end
# file = open(r"C:\Users\Lenovo\OneDrive\Desktop\pythoncrt\recursion\recursion.py","a")
# file.write("\nHow are you?")
# file.close()

#create mode --> x
# file = open("newfile.txt","x")
# file = open("newfile.txt","r")
# print(file.read())
# file.close()
# #readline()
# file = open("newfile.txt","r")
# print(file.readline())
# file.close()
#3.read lines() --> reads the multiple lines
# file = open("newfile.txt","r")
# lines = file .readlines()
# print(lines)
# file.close()
#readlines ---> converts to list
#write() ---> writes the data to file
# file = open("newfile.txt","w")
# file.write("Mona\n")
# file.close()

#writelines(): writes the list data
# names=["rahul\n",
#        "anjali\n",
#        "mona"]
# file = open("newfiles.txt","w")
# file.writelines(names)
# file.close()
#pointermethods
#returns the current cursor position
#tell()
# file = open("newfile.txt","r")
# print(file.tell())
# file.read(5)
# print(file.tell())
# file.close()

#seek(): Moves the cursor position
# file=open("newfile.txt","r")
# file.seek(3)
# print(file.read())
# file.close()

#with open()
# with open("newfile.txt","r") as file:
#     print(file.read())
#automatic closing

#student record system:
# name = input("enter the student name:")
# marks=input("enter the marks:")
# with open("newfile.txt","a") as file:
#     file.write(name+""+marks+"\n")
# print("record saved")


#list----> employee details
# employees=[
#     "rahul 50000",
#     "anjali 60000",
#     "sanjana 55000"
# ]
# with open("newfile.txt","w") as file:
#     for emp in employees:
#         file.write(emp + "\n")
# print("report generated")

'''
#problem 3:
A company wants to create a file analyzer tools
the programm should accept:
accept the filename from the user
handle:
file not found
permission denied
empty file
display:
no.of lines : len(file.splitlines())
no.of words : len(file.split())
no.of characters : len(file)
'''
# class EmptyFileError(Exception):
#     pass
# class FileAnalyzer:
#     def analyze(self,filename):
#         try:
#             file=open(filename)
#             content=file.read()
            
#             if content.strip()=="":
#                 raise EmptyFileError("file is empty")
#             lines=len(content.splitlines())
#             words=len(content)
#             characters=len(content)
#             #display the outputs
#             print("Lines:",lines)
#             print("Words",words)
#             print("Characters:",characters)
#             file.close()
#         except FileNotFoundError as e:
#             print(e)
#         except PermissionError as e:
#             print(e)
#         except EmptyFileError as e:
#             print(e)  
#         finally:
#             print("analysis completed")  
# filename=input("Enter the file name")
# obj=FileAnalyzer()
# obj.analyze(filename)

'''
CSV-->Comma Separated Values
used:excel,reports,databases

Example:
name,age,branch
meghana,20,cse
rahul,22,cse
'''
# import csv
# with open("students.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Age","Branch"])
#     writer.writerow(["Rahul",23,"CSE"])
#     writer.writerow(["Sravani",24,"CSE"])

# #read CSV
# with open("students.csv","r") as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)
        
# #binary file handling
# file=open("Image.jpeg","rb")
# data=file.read()
# print(data)
# file.close()


#count the words in the file:
# file=open("newfile.txt","r")
# content=file.read()
# words=len(content.split())
# print("Words",words)

#count the lines in a file
# file=open("newfile.txt","r")
# content=file.read()
# lines=len(content.splitlines())
# print("lines",lines)

#search the word in a file:
# word = input("enter the word:")
# with open("newfile.txt","r") as file:
#     content=file.read()
#     if word in content:
#         print("word found")
#     else:
#         print("no word")

#task 4:
#copy one file to another


#task5:
#count the characters in a file
# with open("newfile.txt","r") as file:
#  content=file.read()
#  characters=len(content)
#  print(characters)

'''
student record management:
A college wants to maintain  student
records permanently
write a python program to
1.accept student_name and marks
2.store records in a file 
named students.txt
3.dispaly all records
4.handle file exceptions properly
'''
# class StudentManager:
#     def add_student(self):
#         try:
#             name = input("Name:")
#             marks = input("Marks")
#             with open("Students.txt","a") as file:
#                 file.write(name + " "+ marks)
#             print("Records added")
#         except Exception as e:
#             print(e)
#     def dsplay_records(self):
#         try:
#             with open("students.txt","r") as file:
#                 content = file.read()
#                 print("Students Records:")
#                 print(content)
#         except FileNotFoundError as e:
#             print(e)
# obj = StudentManager()
# obj.add_student()
# obj.dsplay_records()


'''
a company wants to generate the employee salary reports
write a program to :
accept the employee details
store them in employee.txt
calculate the total salary expenditure (total=0+=salary)
display the employee report
sample input:
enter the employee name:Mona
enter the salary:90000

output:
employee report
Mona  90000
total expenditure is 90000
'''
# class EmployeeReport:

#     def add_employee(self):
#         try:

#            name = input("Enter the name:")
#            salary = float(input("Enter the salary:"))
#            with open ("newfile.txt","a") as file:
#                file.write(name + " " + str(salary)+"\n")
#            print("Employee added")
#         except ValueError as e:
#             print("Invalid input",e)
#     def generate_report(self):
#         total =0
#         try:
#             with open("newfile.txt","r") as file:
#                 for line in file:
#                     name,salary = line.split()
#                     print(name,salary)
#                     total +=float(salary)
#             print("Total Expenditure:",total)
#         except FileNotFoundError:
#             print("Employee File missing")
# obj = EmployeeReport()
# obj.add_employee()
# obj.generate_report()            

'''
word frequency analyzer:
a company wants to analyze the text
write a program to :
read the data from data.txt
count the frequency of the each word
dispaly most repeated word
handle the exceptions
'''
# class WordAnalyzer:
#     def analyzer (self):
#         try:
#           with open("newfile.txt","r") as file:
#             content = file.read().lower()
#             words = content.split()
#             frequency = {}
#             for word in words:
#                 if word in frequency:
#                     frequency[word] +=1
#                 else:
#                     frequency[word] =1
#             print("word Frequencies")
#             for key,value in frequency.items():
#                 print(key,":",value)
#             maximum = max(frequency, key=frequency.get)
#             print("Most Repeated word",maximum)
#         except FileNotFoundError as e:
#             print("File not found",e)

# obj = WordAnalyzer()
# obj.analyzer()

'''
Login Authentication System
company wants to store user credentials
wRITE A PROGRAM
1.Register users into users.txt
2.login using username and password
3.validate the credentials from file
4,handle invalid login attempts

'''
# class LoginSystem:
#     def register(self):
#         try:
#             username = input("Enter the username:")
#             password = input("Enter the password:")
#             with open("users.txt","a") as file:
#                 file.write(
#                     username + " " +password+"\n"
#                 )
#             print("Registration Successful")
#             def login(self):
#                 username = input("Enter username:")
#                 password = input("enter the password:")
#                 found = False
#                 with open("users.txt","r") as file:
#                     for line in file:
#                         u,p =line.strip().split()
#                         if(username == u and password == p):
#                             found = True
#                             break 
#                         if found:
#                           print("Login successful")
#                         else:
#                           print("Invalid Credentials")
#         except FileNotFoundError as e:
#             print(e)

# obj = LoginSystem()
# obj.register()
# obj.login()
'''
A company stores server logs in a file:
write a python program:
1.read log.txt
count:
total lines
ERROR messages
WARNING messages
INFO messages
Display analysis report

Log Format:
INFO server started
ERROR databases failed
WARNING LOW memory
'''

