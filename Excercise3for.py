# Q.1 print the below format...   
   
#      *   
#     **
#    ***
#   ****
#  *****
# ****** 

# n= int(input("Enter a number : "))
# for i in range(n):
#     for l in range(n-i):
#         print(end=" ")
#     for l in range(i):
#         print("*", end="")
#     print()    

# Q.2 Print the below format...


#   *********
#    *******
#     *****
#      ***
#       *     

# n = int(input("Enter a number : "))
# for i in range(n):
#     for l in range(i):
#         print(end=" ")
#     for l in range(n-i):
#         print("*", end=" ")
#     print()

# Q.3 Print the below format....

#     *****
#      ****
#       ***
#        **
#         *

n = int(input("Enter a number : "))
for i in range(n):
    # for l in range():
    for l in range(i):
        print(end=" ")
    # print()
for a in range(n):
    for b in range(n-a):
        print("*", end=" ")
    print()

  






