'''class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("Parent eating biryani..")
class Child(Parent):
    def __init__(self, name, age,cname,cage):
        super().__init__(name, age)
        self.cname=cname
        self.cage=cage
    def dring(self):
        print("Child drinking water...")
c=Child('Riya',38,'Faru',27)
print(c.name,c.age,c.cname,c.cage)
c.eat()
c.dring()

output :
Riya 38 Faru 27
Parent eating biryani..
Child drinking water...'''



'''
class A:
    x=34
    def __init__(self):
        self.y=39
    def m1(self):
        self.b=17
class B(A):
    def __init__(self):
        self.y=76
        print("before :",self.y)
        super().__init__()
        print("After :",self.y)
        super().m1()
        print(self.b)
d=B()

before : 76
After : 39
17
'''

                

        