# __init__ (it is a special function/method)

class Employee():
    def __init__(self, name, salary): #this will print first 
        self.name = name
        self.salary = salary
    def getDetails(self):
        print(f"The employee name is {self.name} and salary is {self.salary}.")
farheen = Employee("Farheen", 200000)
Mini = Employee("Mini Riyazi", 100000)
farheen.getDetails()
Mini.getDetails()
        