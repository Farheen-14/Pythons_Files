# Q.1 Print the below format ... 

# *
# **
# ***
# ****
# *****

for i in range(5):  
    for j in range(i+1):
        print("*", end=" ") #end=""- don't go in other line- we are using this end="" for one line printinng
    print()  #this is for new line

# Q.2 Print the below format 

# *****
# ****
# ***
# **
# *

for i in range(6):
    for j in range(6-i):
        print("*", end=" ")
    print() 

# Q.3 Print the below format ...

#     *
#    **
#   ***  
#  ****
# *****

n= int(input("Enter a number"))
for i in range(1, n):
    for j in range(n):
        print(" " + "*", end=" ")
    print()





# for i in range(1,6):
#     str = ((5-i)* " ")+ ("*" *i)
#     print(str)
    
    




# for i in range(5):
#     for j in range(5-i):
#         print(end=" ")
#     for j in range(i+1):
#         print("*", end="")
#     print()





# Q.3 print the below format..
  
#    *
#   ***  
#  *****
# *******     


# Q.4 priint the sum : 1+2+3+4 = 10

total = 0
num = input("Enter a number : ")
for i in range(0, len(num)):
    total = total + int(num[i])
print(total)    





