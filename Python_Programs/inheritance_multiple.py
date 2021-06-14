class Employee:
    company = "Microsoft"
    
    def upgradeVersion(self):
        print("This is upgrade version")
class Student:
    school = "DAV"

class form(Employee,Student):
    salary = 200000
    # company = "IBM"

f = form()
print(f.company)
f.upgradeVersion()

