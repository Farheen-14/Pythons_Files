# Method Overloading 
#     if we are passing 2 argument in function/method like __init__(self , a, b):
#     or we are passing 3 value in object like print(s1.sum(3,5,6)), then we will receive an error.
#     so these types of error handling we are using method Overloading like none or if else statement...

class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        s= 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s
s1 = student(24,30)
print(s1.sum(5,6,8))
