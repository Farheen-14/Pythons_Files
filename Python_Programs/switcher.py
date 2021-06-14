"""def xyz(x):
    switcher={
        0:"Sweeets",
        1:"Snacks",
        2:"South Indian",
        3:"North Indian",
    }
    return switcher.get(x,"Option not available and choose another")
n=int(input("Enter your choise in digit :"))
a= xyz(n)
print(a)"""

def a():
    return "Hello farheen...Welcome to my resturant"
def b():
    return "Thanks for coming"
def xyz(x):
    switcher={
        0: a(),
        1: b(),
        #2:"South Indian",
        #3:"North Indian",
    }
    return switcher.get(x,"Option not available and choose another")
n=int(input("Enter your choise in digit :"))
z= xyz(n)
print(z)