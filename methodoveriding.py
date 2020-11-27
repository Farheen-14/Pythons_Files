# Method Overiding

#     simply we can say.. we are overiding the method which is def show(self) 
#     ex- 1st is father phone is our phone ..after my new phone become my phone so this is called method overiding...

class parent:
    def show(self):
        print("Fathers phone befor child phone")

class child(parent):
    def show(self):
        print("Child phone now available")
    

# p = parent()
# p.show()

c = child()
c.show()