'''class Car:
    def __init__(self,cname,cmodel,color):
        self.cname=cname
        self.cmodel=cmodel
        self.color=color
    def getInfo(self):
        print("Car Name :{}, Model : {}, Car Color : {}".format(self.cname,self.cmodel,self.color))
class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def empInfo(self):
        print("Employee name is : ",self.ename)
        print("Employee No. is : ",self.eno)
        print("Employee Car is : ")
        self.car.getInfo()
c=Car('Tarzan','AE4013','Blue')
e=Employee('Farheen','8475937033',c)
e.empInfo()
'''        
'''
class Car:
    def __init__(self,cname,model,color):
        self.cname=cname
        self.model=model
        self.color=color
    def getInfo(self):
        print("Car Name : {}, Model : {}, Color : {}".format(self.cname,self.model,self.color))
class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def empInfo(self):
        print("Employee Name : ",self.ename)
        print("Employee No. : ",self.eno)
        print("Employee Car : ",end="")
        self.car.getInfo()
c=Car('Innova','AER102','Black')
e=Employee('Riyazi','7835887484',c)
e.empInfo()    

output : 

Employee Name :  Riyazi
Employee No. :  7835887484
Employee Car : Car Name : Innova, Model : AER102, Color : Black
'''
                
        
        

        