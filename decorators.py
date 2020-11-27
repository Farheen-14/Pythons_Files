def first():
    print("Hello Farheen! This is first function..")
first()

def second(func):

    def inner(a,b):
        a= 3
        b= 4
        c = a + b
        return func(c)
    # inner(3,5)
    return inner
div = second(first)


# Decorator meaning : we can use the fucntion under funcetion, decorate the functions, what we want to print as function in series