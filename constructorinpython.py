class parent:
    def __init__(self):
        print("This is the init functions in parent class..")
    def feature1(self):
        print("This is the feature1 of the parent class")
    def feature2(self):
        print("This is the feature2 of the parent class")
    
class son:        
    def __init__(self):
        print("This is the init functions in subclass..")
    def feature3(self):
        print("This is the feature3 of child class")
    def feature4(self):
        print("This is the feature4 of child class")
    
class daughter(parent, son):
            
    def __init__(self):
        super().__init__()  #This is the method resolution order (MRO), after this super()- constructor we can access the parent functions.
        print("This is the init functions in super-subclass..")
    
    def feature5(self):
        print("This is the feature3 of subchild class")
    

# p = parent() 
# p.feature1()
# p.__init__()
# s = son()
# s.feature3() #if __init__ is not available in subclass so that we can access the superclass details.
# s.__init__() #if __init__ is available in subclass so the first output will be the subclass may called first priority will be the in same function.
d = daughter()
d.feature2      #we can't access __init__ of parent and child class, we only access subchild class.