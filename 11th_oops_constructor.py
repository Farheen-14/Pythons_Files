'''class Empl:
    def __init__(self,n,i,a):
        self.name=n
        self.id=i
        self.address=a
e=Empl('Farheen',20,90)
print(e.name,e.id,e.address)
e2=Empl('Mini',50,80)
print(e2.name,e2.id,e2.address)'''

# 2nd method 
'''
class Empl:
    def __init__(self,n,i,a):
        self.name=n
        self.id=i
        self.address=a
    def  display(self):
        print("Name : {}, Id : {}, Address : {}".format(self.name,self.id,self.address))
e=Empl('Farheen',20,90)
e.display()
e2=Empl('Mini',50,80)
e2.display()
help(Empl)'''

'''class Student:
    a=10
    def __init__(self):
        self.b=16
        self.c=45
s1=Student()
print(s1.a,s1.b,s1.c)
print(Student.a)'''

# Q.make a program for bank, customer can withdraw, deposit amount in bank.
'''
class Customer:
    bank="FarheenRiyazi"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance = self.balance+amount
        print("After Deposit the Amount is : ",self.balance)
    def withdraw(self,amount):
        self.balance = self.balance-amount
        print("After Withdrawing the Amount is : ",self.balance)
print("Welcome to",Customer.bank)
name=input("Enter Customer Name : ")
c=Customer(name)
while True:
    print('d-Deposit \nw-Withdraw \ne-Exit')
    option = input("Choose Your Option : ")
    if option=='d' or option=='D':
        amount= float(input("Enter your amount for deposit : "))
        c.deposit(amount)
    elif option=='w' or option=='W':
        amount= float(input("Enter Withdrawing Amount : "))
        c.withdraw(amount)
    elif option=='e' or option=='E':
        print("Thanks for coming! Enjoy your day...")
        break'''



        


class Customer:
    bank = "FarheenRiyazi"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("The total amount in your account is : ",self.balance)
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print("After withdrawing the amount is : ",self.balance)
print("Welcome to our bank",Customer.bank)
name=input("Enter Your Name : ")
c=Customer(name)
while True:
    print("d-Deposit \nw-Withdraw \ne-Exit")
    option = input("Enter Your Choice : ")
    if option=='d' or option=='D':
        amount = float(input("Enter the depositing amount : "))
        c.deposit(amount)
    elif option=='w' or option=='W':
        amount = float(input("Enter the Withdrawing amount : "))
        c.withdraw(amount)
    elif option=='e' or option=='E':
        print("Thanks for your Visit!!!")
        break
    else:
        print("Invalid Option, Please Try Again...")

'''
Output :

Welcome to our bank FarheenRiyazi
Enter Your Name : Jiya
d-Deposit 
w-Withdraw
e-Exit
Enter Your Choice : d
Enter the depositing amount : 3000
The total amount in your account is :  3000.0
d-Deposit
w-Withdraw
e-Exit
Enter Your Choice : d
Enter the depositing amount : 5000
The total amount in your account is :  8000.0
d-Deposit
w-Withdraw
e-Exit
Enter Your Choice : w   
Enter the Withdrawing amount : 4000
After withdrawing the amount is :  4000.0
d-Deposit
w-Withdraw
e-Exit
Enter Your Choice : w
Enter the Withdrawing amount : 4000
After withdrawing the amount is :  0.0
d-Deposit
w-Withdraw
e-Exit
Enter Your Choice : d
Enter the depositing amount : 1000
The total amount in your account is :  1000.0
d-Deposit
w-Withdraw
e-Exit
Enter Your Choice : w
Enter the Withdrawing amount : 2000 
After withdrawing the amount is :  -1000.0
d-Deposit
w-Withdraw
e-Exit
Enter Your Choice : e
Thanks for your Visit!!!'''
        
    



