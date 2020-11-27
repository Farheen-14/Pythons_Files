# try catch exception handling
print("Enter 1st number.")
a = input()
print("Enter 2nd number.")
b = input()
try:
    print("The total number is.", int(a+b))
except Exception as e:
    print(e)

print("This line is working, whenever the try or except are running")
