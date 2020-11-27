# from array import *
# arr = array('i', [])

# n = int(input("Enter a value of array : "))

# for i in range(n):
#     x = int(input("Enter the next value : "))
#     arr.append(x)
# print(arr)

# val = int(input("Enter a value you want to search : "))

# k=0
# for e in arr:
#     if e == val:
#         print("The position of array is : " , k)
#         break
#     k+=1
# else :
#     print("Invalid Input")



# Numpy examples....

# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones()

from numpy import * 

arr = array([1,2,3,5,8.3,6,3.6]) #After mentioning the float value 3.6 or 8.3, the all value will print as a float value like --1. 2. 3. 8. etc...


print(arr)
# print(arr.dtype) #  dtype to define the type of array, which we are mentioned .. like int , float etc..

arr = linspace(1, 15, 15) 
print(arr)

arr1 = linspace(2, 10, 3) # it will start from 2 to 10 and difference between third value i.e, 3 and output are mentioned below.. 
print(arr1)

# arr2 = linspace(0,10) # if we are not mentioning the 3rd value, it means .. it will calculate 50 value, and distribute in 50 digits.
# print(arr2)

a = arange(1,15,2)  # the third value is called step value, it means it will print after 2 steps, like 1 skip 2 and print 3, skip 4 and print 5 etc.. 
print(a)

b= zeros(3) #zeroes will print in 3 times..
print(b)

c= ones(5) #  1 will print in 5 times...
print(c)

