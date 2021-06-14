"""def add(x,y):
    c=x+y
    print(c)
def sub(x,y):
    d=x-y
    print(d)
x= int(input("Enter value of x : "))
y= int(input("Enter value of y : "))
add(x,y)
sub(x,y)"""

def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
x= int(input("Enter a value : "))
factorial = fact(x)
print(factorial)
