class Employee:
    salary = 5500
    salarybonus = 1000
    # totalSalary = --
    
    @property #getter method, using this we set the property and it is behave like a property.
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val-self.salary
    
    
e = Employee()
print("The total salary is : ",e.totalSalary)
e.totalSalary = 6500
print("The salary is : ", e.salary)
print("The total Salary Bonus is: " ,e.salarybonus)