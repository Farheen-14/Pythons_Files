"""class Employee:
    company = "Google"
    salary = 5000
farheenInformation = Employee()
miniInformation = Employee()
print(Employee.company)
print(Employee.salary)

# There is no instance attributes are available so it will check in class, not its found and it run.
"""

"""
#Instance Attributes Example 
class Employee:
    company = "Google"
    salary = 5000
farheenInformation = Employee() 
miniInformation = Employee()
farheenInformation.salary = 100000 #this is instance attributes, once it will available here then print from here otherwise it will check in class instance attributes.
miniInformation.salary = 200000
farheenInformation.company = "MS"
print(farheenInformation.salary)
print(farheenInformation.company)
print(miniInformation.salary)
"""

# Self meaning and why we use?

class Employee:
    company = "MicroSoft"
    def getSalary(self):
        print(f" The Employee salary is {self.salary} and company name is {self.company}")
    @staticmethod #it's a decorator we can say
    def greet(): #if we are not using self here so we will got an error and if we want to run without selg argument so we mention here @staticmethod
        print("Hello Farheen")
        

farheen = Employee()
farheen.salary = 100000
farheen.getSalary() #Employee.getSalary(farheen) this line meaning is same but we are using farheen.getSalary()
farheen.greet()

    