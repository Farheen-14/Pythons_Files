class Employee:
    company = "Google"
    def showDetails(self):
        print("This is an Employee class")
class Programmer:
    company = "Microsoft"
    language = "Python"
    def getLanguage(self):
        print("This is an Programmer child class")
# e = Employee()
# e.showDetails()
p = Programmer()
print(p.company) #if we want, we can change the company name in child class or we can update in child class.
p.getLanguage()
