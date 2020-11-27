# from abc import ABC, abstractmethod

# class teamlead(ABC):
#     @abstractmethod
#     def team(self):
#         return 0

# class employee:
#     # type = "circle"

#     def __init__(self,s1,s2):
#         self.s1 = s1
#         self.s2 = s2
# # emp = employee()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod     #if we are mentioning the abstractmethod before any function/method, so it is mendatory to print the printarea function/method. otherwise we will get the error. i.e, callled abstract method.
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())
    