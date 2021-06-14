# Q. Input a list and remove the dublicate values and print the unique value from list.
# in set .... 

# n=eval(input("Eneter a tuple list: "))
# s = set(n)
# print(s)

# output :

# Eneter a tuple list: (10,30,20,10,20,10,50)
# {10, 20, 50, 30}

########### ########### ########### ########### ########### ########### ########### ########### ###########

# in list ....
# n = eval(input("Enter a number of list : "))
# list = []
# for i in n:
#     if i not in list:
#         list.append(i)
# print(list)

# output :
# Enter a number of list : [10,30,20,30,50,60,30,20]
# [10, 30, 20, 50, 60]

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q. input a string value and checking the vowels which is available in str and count the vowels.

# n= input("Enter a string value : ")
# s= set(n)
# v = {'a','e','i','o','u'}
# unique= s.intersection(v)
# print("The unique vowels are available in this given words are : ",unique)
# print("The total vowels in this given words are : ", len(unique))

# output :

# Enter a string value : farheen
# The unique vowels are available in this given words are :  {'a', 'e'}
# The total vowels in this given words are :  2

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q.Enter name and marks in dictonary and display the info on screen

rec={}
n= int(input("Enter the total number of student : "))
i=1
while i<=n:
    name = input("Enter Student Name : ")
    marks = input("Enter Student Marks : ")
    rec[name]=marks
    i=i+1
print(rec)
while True:
    name=input("Enter the Student name to get the marks : ")
    marks = rec.get(name,-1)
    if marks == -1:
        print("Student not found...")
    else:
        print("The name of the Student is {} and the marks is {} : ".format(name,marks))
    option = input("Do you want to search the marks of student again, Yes||No : ")
    if option=="No":
        break
print("Thanks for visiting...")






# rec={}
# s=int(input("Enter the number of students : "))
# i=1
# while i<=s:
#     name=input("Enter a student name : ")
#     marks = input("Enter the student marks in % : ")
#     rec[name]=marks
#     i=i+1
# print("Student Name","\t","Student Marks(%)")
# for j in rec:
#     print("\t",j,"\t\t", rec[j])

# output :

# Enter the number of students : 2
# Enter a student name : Mini
# Enter the student marks in % : 87%
# Enter a student name : xiya
# Enter the student marks in % : 67%
# Student Name     Student Marks(%)
#          Mini            87%
#          xiya            67%



