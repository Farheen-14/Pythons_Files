# import cal
# print("Hello", __name__) #if we are importing the cal then the __name__ will print __main__ 
#and the other file : cal.py will print the __name__ to its file name module.. it will print ---cal
from cal import add
def new():
    add()
    print("We are using a new value")

def new2():
    print("We are using a new 2nd value")

def main():
    new()
    new2()
main()