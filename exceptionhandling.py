#  Exceptional Handling
a = 3 
b = 8

try:
    print("Opening the program")
    print(a/b)
    k = int(input("Enter any number"))
    print(k)
#     print("Closing the program")
# except Exception as e:
#     print("Invalid Syntax")
except ValueError as g:
    print("Invalid input, please enter correct number", g)
except ZeroDivisionError as z:
    print("You can't divide any number by zero" , z)
finally:
    print("Closing the program")