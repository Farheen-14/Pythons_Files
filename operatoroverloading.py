# a = 3
# b = 6

# print(a+b)
# print(int.__add__(a,b))

# Operator overloading

# class student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
# #if the operator simply not calculated the value so we are generating different function/method __add__, which is called operator overloading 
#     def __add__(self, other):   #when the operator doesn't work easily with '+' or any other operators, then we are adding new function/method i.e, called operator overloading..
#         m1 = self.m1 + other.m1 
#         m2 = self.m2 + other.m2 
#         s3 = student(m1,m2)
#         return s3
# s1 = student(30,55)
# s2 = student(40,50)

# s3 = s1+s2
# print(s3.m1)


class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __mul__(self,other):
       return self.m1*other.m1 , self.m2*other.m2  
    def __truediv__(self, other):
        return self.m1/other.m1, self.m2/other.m2

s1 = student(60,10)
s2 = student(55, 5)

s3 = s1*s2
s4 = s1/s2

print(s3)
print(s4)