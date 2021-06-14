# Q. input a string and print index and positive and negative index 
'''
n=input("Enter a string : ")
i = 0
for j in n:
    print(" +ve index {} and -ve index {} is : {}".format(i,i-len(n),j))
    i += 1

output : 
Enter a string : Mini
 +ve index 0 and -ve index -4 is : M
 +ve index 1 and -ve index -3 is : i
 +ve index 2 and -ve index -2 is : n
 +ve index 3 and -ve index -1 is : i
 '''
########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q. Enter a string and print into forward or backward directions..

# forward - farheen backward - neehraf 

# s=input("enter a string : ")
# n= len(s)
# i=0
# print("Forward direction : ")
# while i<n:
#     print(s[i],end='')
#     i += 1
# print()
# print("backward direction : ")
# i=n-1
# while i>=0:
#     print(s[i],end='')
#     i -= 1
# print()
'''
s=input("Enter a string : ")
n=len(s)
i=0
while i<n:
    print(s[i],end='')
    i += 1
print()
i=-1
print("Backward direction....")
while i>=-n:
    print(s[i],end='')  
    i -= 1

Enter a string : farheen
farheen
Backward direction....
neehraf
'''

# Q.enter string and substring value, check the  substring is available in string or not.
'''
main = input("Enter String Value : ")
sub = input("Enter Sunstring Value : ")
if sub in main:
    print("Yes available") 
else:
    print("Not available")

output : 
Enter String Value : as simple as that
Enter Sunstring Value : simple
Yes available
'''

# Q. Enter a string and print the even and odd value 
'''
n= input("Enter a String : ")
print("Even value is : ",n[::2])
print("Odd value is : ",n[1::2])

output : 
Enter a String : farheen
Even value is :  fren
Odd value is :  ahe
'''
# Q. Enter alphanumeric value and sort  like , input : a45sh24bj9d1 then output : abdjhs124459

'''
n = input("Enter a alphanumeric value : ")
s1=s2=''
res = ''
for i in n:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i
print(s1+s2)
for i in sorted(s1):
    res=res+i
for i in sorted(s2):
    res=res+i
print(res)

output : 
Enter a alphanumeric value : z3b5n1
zbn351
bnz135
'''
# Q. input like a3b2 and output like aaabb

'''
n=input("Enter a value : ")
output=''
for i in n:
    if i.isalpha():
        output= output+i
        store = i
    else:
        output = output + store* (int(i)-1)
print(output)

output : 
Enter a value : a2v3
aavvv
'''

# Q. input like a3b4 then output : adbf

'''
n = input("Enter a value : ")
output=''
for i in n:
    if i.isalpha():
        output=output+i
        previous=i
    else:
        newchr = chr(ord(previous)+ int(i))
        output=output+newchr
print(output)

output :
Enter a value : b3n2
benp
'''
# Q. make a list value and searching the value from this list and also print it's index

'''
l = [2,55,6,3,5,77,86,23]
n=int(input("Enter a no. you want to search ? : "))
if n in l:
    print(n,"Target is available at position of : ",l.index(n))
else:
    print("Not available")

output :
Enter a no. you want to search ? : 86
86 Target is available at position of :  6
'''

# Q,program of list comprehension, calculate sqare of the number
'''
list = [x*x for x in range(1,11)]
print("Sqare of the no's is : ",list)
output : 
Sqare of the no's is :  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# Q.Calculate sqare  of the number and calculate even no's in previous list.

'''
list1=[x*x for x in range(1,11)]
list2=[x for x in range(1,11) if x%2==0 ]
print("Square of the no's : ",list1)
print("Even No's : ",list2)

output : 
Square of the no's :  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Even No's :  [2, 4, 6, 8, 10]
'''
# Q.Enter a list value and remove the duplicate value 
'''
n = eval(input("Enter a list value : "))
list=[]
for i in n:
    if i not in list:
        list.append(i)
print(list)
n=sorted(list)
print(n)

Enter a list value : [3,5,2,4,5,6,7,8]
[3, 5, 2, 4, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
'''
# Q. Enter a string and check the character, how many times it's occured 

'''
word= input("Enter a string : ")
d={}
for i in word:
    d[i]=d.get(i,0)+1
for k,v in d.items():
    print(k,"occured : ",v)

output  :

Enter a string : hello miss farheen ansari
h occured :  2
e occured :  3
l occured :  2
o occured :  1
  occured :  3
m occured :  1
i occured :  2
s occured :  3
f occured :  1
a occured :  3
r occured :  2
n occured :  2  
'''

# Q.Enter toal no. of student, input name and marks, search the student name to get the marks, if available then shown otherwise not available 
# or choose option want search again or not ?

'''
rec={}
total=int(input("Enter total no. of student : "))
i=1
while i<= total:
    name = input("Student name : ")
    marks = input("Student marks :  ")
    rec[name]=marks
    i += 1
print(rec)
while True:
    name = input("Enter name for marks : ")
    marks = rec.get(name,-1)
    if marks == -1:
        print("Student not available ....")
    else:
        print("Student name : {} and marks : {} ".format(name,marks))
    option = input("Do you want to search again Yes|No : ")
    if option == "No":
        break
print("Thanks for visiting..")

output : 
Enter total no. of student : 2
Student name : mini
Student marks :  90
Student name : riya
Student marks :  99
{'mini': '90', 'riya': '99'}
Enter name for marks : riya
Student name : riya and marks : 99 
Do you want to search again Yes|No : yes
Enter name for marks : hj
Student not available ....
Do you want to search again Yes|No : No
Thanks for visiting..
'''

# Q.calculate factorial for a no. using recursive function 
'''
def factorial(n):
    if n==0:
        return 1
    else:
        result = n*factorial(n-1)
        return result
print(factorial(5))

output : 120 
'''
# Q. calculate square of the no. using anonymus function 

# n = lambda a,b : a+b
# print(n(2,5))

# and 

# n= lambda a,b : a if a>b else b
# print(n(4,3))

# Q.calculate  even no. using filter and anonymus funtion 
'''
l=[1,2,3,4,5,6,6,7,8]
e  = list(filter(lambda n : n%2==0,l))
print(e)

output : 
[2, 4, 6, 6, 8]
'''
# Q.calculate square of the number using map function 

# l=[1,2,3,4,5]
# n= list(map(lambda n: n*n,l))
# print(n)

# def square(n):
#     return n*n
# l = [1,2,3,4,5,6]
# a= list(map(square,l))
# print(a)
'''
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
square = list(map(lambda x,y: x*y,l1,l2))
print(square)
output : [1, 4, 9, 16, 25]
'''

# Q. Calculate the sum of the numbers using reduce function
'''
from functools import *
l = [1,2,3,4,5,4]
n = reduce(lambda x,y : x+y, l)
print(n)

output: 19
''' 

# Q.example of decorator function 
'''
def decorate1(func):
    def inner(name):
       print("decor1  is starting")
       func(name)
       print("decor1 is ending")
    return inner
def decorate2(func):
    def inner(name):
       print("decor2 starting")
       func(name)
       print("decor2 ending")
    return inner
@decorate2
@decorate1
def wish(name):
    print("Hello",name, "Good Morning...")
wish('farheen')

output :
decor2 starting
decor1  is starting
Hello farheen Good Morning...
decor1 is ending
decor2 ending
'''

# Q.Generator using yield function , program is  fibonacchi series 
'''
def fibonacchi(n):
    a,b=0,1
    while True:
        yield a
        a,b = b, a+b
f = fibonacchi(25)
for i in f:
    if i>25:
        break
    print(i)
output : 
0
1
1
2
3
5
8
13
21
'''

# Q.Random module programs 
'''
import random
for i in range(5):
    print(random.randint(100000,999999))
'''
# Q. print like a password using random module
'''
from random import *
for i in range(5):
    print(chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9))
output :
Q 4 S 6 P 7
H 7 O 3 Z 4
O 2 U 5 H 5
A 0 U 0 N 3
X 2 S 8 A 0
'''

# Q. using oops concept, class, object  and variable, make a bank program, 
# we can visit and deposit, withdraw the can check the balance 


'''
class Customer:
    bank = 'ICICI Bank'
    def __init__(self,name,balance = 0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance= self.balance+amount
        print("After deposit the total amount is : {}".format(self.balance))
    def withdraw(self,amount):
        self.balance= self.balance-amount
        print("After Withdrwing the amount available in your account {} is {}".format(self.bank,self.balance))
print("Welcome to {} ".format(Customer.bank))
name = input("Enter Customer Name : ")
c= Customer(name)
while True:
    print("What you want, please choose any one\nd-Deposit \nw-Withdraw \ne-Exit")
    option = input("Enter your choise : ")
    if option=='d' or option=='D':
        amount = float(input("Enter the deposit amount : "))
        c.deposit(amount)
    elif option=='w' or option=='W':
        amount=float(input("Enter the withdraw amount : "))
        c.withdraw(amount)
    elif option=='e' or option=='E':
        print("Thanks for  visiting...")
        break
'''
# Q.Setter & Getter example ~
'''
class Customer:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setReview(self,review):
        self.review=review
    def getReview(self):
        return self.review
name = int(input("Enter no. of Customer : "))
for  i in range(name):
    c=Customer()
    name= input("Customer name : ")
    c.setName(name)
    review = input("Enter review please ... : ")
    c.setReview(review)
    print("Customer name : {} and Review : {}".format(c.getName(),c.getReview()))

output : 
Enter no. of Customer : 2
Customer name : farheen
Enter review please ... : next prime minister
Customer name : farheen and Review : next prime minister
Customer name : mini
Enter review please ... : great person even
Customer name : mini and Review : great person even
'''
# Q. using class method and class variable 
'''
class Animal:
    legs = 4
    @classmethod
    def pet1(cls,name):
        print("{} having {} legs to walk ".format(name,cls.legs))
Animal.pet1('Dog')

output  : Dog having 4 legs to walk
'''

# Q.Nested class program 
'''
class Car:
    def m1(self):
        print("Car is new")
    class Engine:
        def m2(self):
            print("Engine required..")
# c=Car()
# c.m1()
# e=c.Engine()
# e.m2()
c=Car().Engine().m2()
c= Car().m1()
'''
# Q.Compisition (Has-A-Relation)
# making a car and employee  relation
'''
class Car:
    def __init__(self,cname,cno,color):
        self.cname=cname
        self.cno=cno
        self.color=color
    def getInfo(self):
        print("The Car name is : {} \nCar No. : {} \nCar Color : {}".format(self.cname,self.cno,self.color))
class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno = eno
        self.car=car
    def EmpInfo(self):
        print("Employee name : ",self.ename)
        print("Employee no. : ",self.eno)
        print("Employee Car : ",end='')
        self.car.getInfo()
c= Car('Tarzan','AE1090','Blue')        
e =Employee('Farheen','7878789080',c)
e.EmpInfo()

output :
Employee name :  Farheen
Employee no. :  7878789080
Employee Car : The Car name is : Tarzan
Car No. : AE1090
Car Color : Blue
'''

# Q.Inheritance program (IS-A-Relationship)
# single inheritance
'''
class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Talent(self):
        print("Parent talents")
    def Apairing(self):
        print("All appearing to child")
class Child(Parent):
    def __init__(self,name,age,cname,cage):
        super().__init__(name,age)
        self.cname=cname
        self.cage=cage
    def Activity(self):
        print("Child smart..")
c=Child('Mother','40','Daughter','27')
print(c.name,c.age,c.cname,c.cage)
c.Activity()
c.Apairing()
c.Talent()

output :
Mother 40 Daughter 27
Child smart..
All appearing to child
Parent talents
'''
# multilevel inheritance
'''
class Gfather:
    def Money(self):
        print("Grand Father having  lots of money")
class Father(Gfather):
    def Struggle(self):
        print("Father Struggle lots..")
class Child(Father):
    def Success(Father):
        print("Success bcz of Parent struggles...")
c=Child()
c.Money()
c.Struggle()
c.Success()

output :

Grand Father having  lots of money
Father Struggle lots..
Success bcz of Parent struggles...
''' 

# Q.Regular Expression
'''
import re
count=0
match= re.finditer("['abc']",'ndjjabcmsa')
for m in match:
    count += 1
    print("Start....",m.start(),"End.....",m.end(),"Group.....",m.group(),"Count....",count)

output :

Start.... 4 End..... 5 Group..... a Count.... 1
Start.... 5 End..... 6 Group..... b Count.... 2
Start.... 6 End..... 7 Group..... c Count.... 3
Start.... 9 End..... 10 Group..... a Count.... 4
'''

# Q.calculate special character
''' 
import re
count = 0
match = re.finditer('[^a-z0-9A-Z]','nbcdjk93%jdhk^js0')
for i in match:
    count += 1
    print("Start :",i.start(),"End :",i.end(),"Group : ",i.group(),count)

output :

Start : 8 End : 9 Group :  % 1
Start : 13 End : 14 Group :  ^ 2
'''

# Q. Mobile no. match correct or not 
'''
import  re 
n = input("Enter 100  digit mobile no. : ")
match= re.fullmatch('[6-9]\d{9}',n)
if match !=None:
    print(n,"Correct matched")
else:
    print(n,"Not matched")

output : Enter 100  digit mobile no. : 7803840283
7803840283 Correct matched
'''
# Q. Regular expression using other file and saved in output file 

'''
import re
count= 0
f1 = open('re_input.txt','r')
f2 = open('re_output1.txt','w')
for line in f1:
    match = re.findall('are',line)
    for i in match:
        count += 1
        f2.write(i+'\n')
print("All saved in output.txt file, you can check...")
print(i,"occurse : ",count)
f1.close()
f2.close()

output :

All saved in output.txt file, you can check...
are occurse :  3
'''

# Q. Check email_id is valid or not 
'''
import re
n = input("Enter email id : ")
match = re.fullmatch('[a-zA-Z0-9_.]*@[a-zA-Z]+[.][a-zA-Z]+',n)
if match!=None:
    print("Full matched...")
else:
    print("Not Matched...")    

output :
Enter email id : riyazi.123@yahoo.in
Full matched...
'''

# Q.web scrapping using regular expression

import re, urllib
import urllib.request
site = urllib.request.urlopen('https://in.yahoo.com/')
for i in site:
    text=site.read()
    match= re.findall('<title>.*</title>',str(text),re.IGNORECASE)
    print("title is : ",match[0])

