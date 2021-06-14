# Q. Enter 4 numbers fromm users and find the largest no.
a1 = int(input("Enter no. 1 : ")) 
a2 = int(input("Enter no. 2 : "))
a3 = int(input("Enter no. 3 : "))
a4 = int(input("Enter no. 4 : "))
if (a1>a4):
    f1 = a1  
else:
    f1 = a4
if (a2>a3):
    f2 = a2
else:
    f2 = a3
if(f1>f2):
    print("The largest value is : ", f1)
else:
    print("The largest value is : ", f2)



"""dry run
a1 =5
a2 = 6
a3 = 2
a4 = 9

1 - a1>a4 - 5>9 false then f1 - a4 - 9
2.  a2>a3 - 6>2 true then f2 - a2 - 6 """


    
