# def decor(func):
#     def inner(name):
#         if name=="Riyazi":
#             print("Hello Riyazi Good Evening...")
#         else:
#             return func(name)
#     return inner

# @decor
# def wish(name):
#     print("Hello", name, "Good Morning")
# wish("Farheen")
# wish("Riyazi")
# wish("Mini")

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q. Adding numbers and do some changes using decorator

'''def sub(func):
    def inner(a,b):
        if a>b:
            return a-b
        else:
            return func(a,b)
    return inner
@sub
def sum(a,b):
    return a+b

print("Sum value is :",sum(2,4))
print("The sub value is :",sum(10,6))
print(sum(2,7))'''

# output :

# Sum value is : 6
# The sub value is : 4
# 9

def change(func):
    def inner(any):
        print("change start ..Don't worry...Farheen")
        func(any)
        print("1st end...I belive on you")
    return inner

def extra(func):
    def inner(any):
        print("Extra changes required on you farheen...")
        func(any)
        print("Extra..you know naa...")
    return inner
def third(func):
    def inner(any):
        print("third start..")
        func(any)
        print("third..ending...")
    return inner
@extra
@third
@change
def intro(any):
    print("Farheen! You are next prime minister...")
intro(any)

# run : start with top to bottom and after main function call, it will go with bottom to top 
# 1st start ..Don't worry...Farheen
# Extra changes required on you farheen...
# Farheen! You are next prime minister...
# Extra..you know naa...
# 1st end...I belive on you