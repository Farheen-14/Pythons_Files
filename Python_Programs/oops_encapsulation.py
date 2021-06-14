class RailwayForm:  # they are in one class RailwayForm so it is in encapsulations.
    formType= "RailwayForm"
    def printData(self):
        print(f"The Name is {self.name}")
        print(f"The Train is {self.Train}")
farheenApplication = RailwayForm()  #creating object intensiatiion  and we don't know how they work and need only output so in this requirement is called abstraction.
farheenApplication.name = "Farheen"
farheenApplication.Train = "Rajdhani Express"
farheenApplication.printData()