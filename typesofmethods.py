class Student:
    school = "Annamalai"  #Static/class variable 

    def __init__(self, m1, m2, m3): #it is called function/constructor (m1,m2,m3 is passing the arguments)
        self.m1 = m1
        self.m2 = m2     #m1 ,m2 ,m3 are instance variables, which we are creating..
        self.m3 = m3
    #Now calling a method..
    def avg(self):       #it is instance method, because here is mentioned (self), when its mentioned self so that we can say it, its a instance method.
        return(self.m1 + self.m2 + self.m3)/3
    @classmethod
    def info(cls):
        return cls.school

s1 = Student(67,44,56) #creating objects and passing the values
s2 = Student(78,88,98) #creating objects and passing the values

print(s1.avg())
print(s2.avg())
# print(s1.m1, s2.m2)
Student.info()