'''
class Student:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+ other.pages
b1=Student(100)
b2=Student(200)
print("The total no. of pages id is : ",b1+b2)
'''

# output : The total no. of pages id is :  300  

# Q. Calculate monthly salary using operator overloading 
'''
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
    def __mul__(self,other):
        return self.salary * other.days
class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
e=Employee('Farheen',1500)
t=Timesheet('Farheen',25)
print("The month Salary is : ",e*t)
'''
# output : The month Salary is :  37500
             
