# polymorphism - many forms to execute...
# poly = many,  morph = forms
class visualstudiio:
    def execute(self):
        print("Compiling the code")
        print("Running the code")

class myeditor:
    def execute(self):
        print("Checking the code")
        print("Error handling")
        print("Another way to check")
        print("Execute and get the output")
class myeditor2:
    def execute(self):
        print("getting the output")
        print("output is here")
        
class laptop:
    def code(self,ide):
        ide.execute()   #execute method is matter, its like duck walking,qauking, swimming like a duck.

ide = visualstudiio() #it doesn't matter, which class and objects are passing like (self,ide), (ide = myeditor).its matter is execute method (ide.execute())
# ide = myeditor()
# ide = myeditor2()
lap = laptop()
lap.code(ide)