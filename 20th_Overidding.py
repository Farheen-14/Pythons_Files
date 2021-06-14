# Method overiding example
'''
class Parent:
    def property(self):
        print("Family provides : Cash + Gold + Benifits")
    def marry(self):
        print("Family choice is : Lata")
class Child(Parent):
    def marry(self):
        super().marry()
        print("Child choice is : Sheela")
c=Child()
c.property()
c.marry()
'''
# output 

# Family provides : Cash + Gold + Benifits
# Family choice is : Lata
# Child choice is : Sheela

# Constructor Overiding 
'''
class Parent:
    def __init__(self):
        print("Parent Constructor Overiding")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Overiding")
c=Child()
'''
# output : 
# Parent Constructor Overiding
# Child Overiding

# Q. Another example of constructor overiding

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Employee name is {}, age is {} , employee no. is {} and salary is  {}".format(self.name,self.age,self.eno,self.salary))
        
class Employee(Person):
    def __init__(self, name, age,eno,salary):
        super().__init__(name, age)
        self.eno=eno
        self.salary=salary
e=Employee('Farheen0',26,8584,35000)
e.display()

# output : Employee name is Farheen, age is 26 , employee no. is 8584 and salary is  35000
