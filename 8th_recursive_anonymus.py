# Q.Calculate factorial using recursive function 
# def factorial(n):
#     if n==0:
#         result = 1
#     else:
#         result = n*factorial(n-1)
#     return result
# print(factorial(0))
# print(factorial(4))

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q.Calculate sum of 2 number using anonymus function 

# s = lambda a,b:a+b
# print("The sum of the number of {} and {} is : {}".format(2,4,s(2,4)))
# print("The sum of the number of {} and {} is : {}".format(20,40,s(20,40)))

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q.input 2 number and calculate the bigger number.
# s= lambda a,b : a if a>b else b
# print("The bigger number of {} and {} is : {}".format(3,5,s(3,5)))

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q.Calculate the even no. using filter inbuild function

# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# l = [0,5,10,15,20,25,30]
# l1 = list(filter(even,l))
# print(l1)

########### ########### ########### ########### ########### ########### ########### ########### ###########

# using lambda inbuild function 

# l = [0,5,10,15,20,25,30]
# l1 = list(filter(lambda x : x%2==0,l))
# print("Even no. : ",l1)
# l2 = list(filter(lambda x : x%2!=0,l))
# print("Odd no. : ",l2)

# output :
# Even no. :  [0, 10, 20, 30]
# Odd no. :  [5, 15, 25]

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q.square of the number using map function.. 

# def square(n):
#     return n*n
# l = [0,2,4,6,8,10]
# l1 = list(map(square,l))
# print(l1)

# l=[0,2,4,6,8,10,12]
# l1=list(map(lambda n: n*n ,l))
# print(l1)

# output : [0, 4, 16, 36, 64, 100, 144]

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q. Using 2 list, make a program to multiply the numbers 

# l= [0,5]
# l1=[0,1,2,3]
# l2 = list(map(lambda x,y:x*y,l,l1))
# print(l2)

# output : [0, 5, 20, 45]

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Nested Function : Function inside the function 

# Q. Calculate the sum of the number and also calculate the average of the numbers

# def f1():
#     def inner(a,b):
#         print("The sum of the number is : ",(a+b))
#         print("The average of the number is : ", (a+b)/2)
#     inner(2,4)
#     inner(10,20)
#     inner(20,30)
# f1()

print("Hey Farheen You are next Prime Minister...")



