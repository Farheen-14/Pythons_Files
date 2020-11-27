# Fuctions

def function1(a, b):
    print("We are in functions1", a+b)
print(function1(7,3))
   
def function2(a,b):
    """This is a different function, there is two type of fuction - function1 and function2
    i am checking this doc file using this statement"""
    average = (a+b)/2
    print(average)
    return average
v= function2(4, 8) #value is stored in v and provide the return value using return fuction.
print(v)
print(function2.__doc__) 


