#def greet(name= "Stranger"): #this is deafult  argument passing in function
def greet(name):
    print("Hello, "+ name)

def mysum(n1,n2):
    n= n1 + n2
    return n
#or return n1+ n2
add = mysum(2, 4)
add1 = mysum(4,6)
add2 = mysum(6,6)
print(add)
print(add1)
print(add2)
 
greet("Farheen")

#greet() # if we empty the value here so it will shown an error 
#and once we declare the value is def function it will take as deafult parameter passing the value automatiocally.

