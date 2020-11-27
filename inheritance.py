# class parent:
#     def feature1(self):
#         print("This is the feature1 of the parent class")
#     def feature2(self):
#         print("This is the feature2 of the parent class")
# class child(parent):        #it is single level inheritance, child class inherit with parent class 
#     def feature3(self):
#         print("This is the feature3 of child class")
#     def feature4(self):
#         print("This is the feature4 of child class")
# p = parent()
# c = child()
# # p.feature1()
# # p.feature2()
# c.feature4()
# c.feature2()

# Multiple inheritance

# class parent:
#     def feature1(self):
#         print("This is the feature1 of the parent class")
#     def feature2(self):
#         print("This is the feature2 of the parent class")
# class son:        
#     def feature3(self):
#         print("This is the feature3 of child class")
#     def feature4(self):
#         print("This is the feature4 of child class")
# class daughter(parent,son):     #it is multiple inheritance...       
#     def feature5(self):
#         print("This is the feature5 of sub-child class")
# c = daughter()      # c will get the details/access the values from parent and child class..
# c.feature1()
# c.feature3()
# c.feature5()

# Multilevel inheritance

class parent:
    def feature1(self):
        print("This is the feature1 of the parent class")
    def feature2(self):
        print("This is the feature2 of the parent class")
class son(parent):        
    def feature3(self):
        print("This is the feature3 of child class")
    def feature4(self):
        print("This is the feature4 of child class")
class daughter(son):     #it is multiple inheritance...       
    def feature5(self):
        print("This is the feature5 of sub-child class")
c = daughter()      # c will get the details/access the values from parent and child class..
c.feature1()
c.feature3()
c.feature5()