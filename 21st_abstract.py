# Q. Difference between interface abstract and concrete class
'''
from abc import *
class Interface(ABC):
    @abstractmethod
    def m1(self): pass
    @abstractmethod
    def m2(self): pass 
    @abstractmethod
    def m3(self): pass
class Abstract(Interface):
    def m1(self):
        print("Trying m1..")
    def m2(self):
        print("Trying m2..")
class Conncrete(Abstract):
    def m3(self):
        print("Finally m3...")
        
c=Conncrete()
c.m1()
c.m2()
c.m3()
'''
# output : 

# Trying m1..
# Trying m2..
# Finally m3...

# Q.Some other example, input from user and conver the user input to class name..

from abc import *

class DbInteface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class Oracle(DbInteface):
    def connect(self):
        print("Connect with Oracle database...")
    def disconnect(self):
        print("Disconnect with Oracle database...")
class Postgresql(DbInteface):
    def connect(self):
        print("Connect with PostgreSQL database...")
    def disconnect(self):
        print("Disconnect with PostgreSQL database...")
dbname = input("Enter Database Name : ")
classname = globals()[dbname]
x=classname()
x.connect()
x.disconnect() 
 
