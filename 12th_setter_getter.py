'''class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name    
    
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n = int(input("Enter the total no. of Student : "))
for i in range(n):
    s=Student()
    name=input("Enter Student Name : ")
    s.setName(name)
    marks=int(input("Enter Marks : "))
    s.setMarks(marks)
    print("Hi ",s.getName())
    print("Your Marks Is : ",s.getMarks())
    print()'''

'''output 

Enter the total no. of Student : 3
Enter Student Name : Farheen
Enter Marks : 90
Hi  Farheen
Your Marks Is :  90

Enter Student Name : Mini
Enter Marks : 98
Hi  Mini
Your Marks Is :  98

Enter Student Name : Hima
Enter Marks : 89
Hi  Hima
Your Marks Is :  89'''

#####################################################################################################################################################################

# using class method and class variable
'''class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} having {} legs".format(name,cls.legs))      
Animal.walk('Dog')
'''
# output : Dog having 4 legs

####################################################################################################################################

# Static method using 

'''class miniMath:

    def add(a,b):
        print("The sum of the value is :",a+b)
    
    def sub(a,b):
        print("The sum of the value is :",a-b)

    def mul(a,b):
        print("The sum of the value is :",a*b)
miniMath.add(10,20)
miniMath.sub(40,20)
miniMath.mul(5,2)

output :

The sum of the value is : 30
The sum of the value is : 20
The sum of the value is : 10 
'''
####################################################################################################################################

'''
class Person:
    def __init__(self,name):
        self.name='Farheen'
        self.db=self.Dob()
    def display(self):
        print("Name : ",self.name)
    class Dob:
        def __init__(self):
            self.dd=14
            self.mm=2
            self.yy=1995
        def display(self):
            print("Dob = {}/{}/{}".format(self.dd,self.mm,self.yy))
p=Person('name')
p.display()
p.db.display()

output : 
Name :  Farheen
Dob = 14/2/1995
'''

            
            

        
        