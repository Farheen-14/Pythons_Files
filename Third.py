# if else or elif Program 
# Q.1 Enter age and check, its aligible or not?
age = int(input("Enter Your Age : "))
if age>18:
    print("Congratulation!! You are aligible for drive")
elif age == 18:
        print("Please come for drive test")
else:
         print("You are not aligible")

# Q.2 Make a faulty Calculator : 45*3 = 555, 56+9 = 77, 56/6 = 4

a = int(input("Enter 1st no."))
b = int(input("Enter 2nd no."))
print("Operators : + , - , *, /")
oper= input("Choose operator")
# if oper=="+" :
if a==56 and b==9 and oper=='+':
        print("77")
elif a==56 and b==6 and oper=='/' :
        print("4")
elif a==45 and b==3 and oper=='*':
        print("555")
     
# Q.3 For loop examples 

list1 = [["Farheen", 5] , ["Shahnaaj",10] , ["Hasnain", 20], ["Tamanna", 15] , ["Mummy", 12] ,["Pappa", 10]]
for item, chocolate in list1:
        print(item, "and chocolate no. is", chocolate)

# For loop other examples

items = ["Farheen", "Hasnain", 2 , 4, 6,12, 23, 33, 9, 7, 5, 10]
for item in items:
        if str(item).isnumeric() and item>9:
                print(item)

# while loop examples      

i=0
while (i<20):
        i=i+1
        print(i)

# continue and break (while loop)

i=0
while (True):
        if i+1<5:
                i=i+1
                continue
        print(i+1)
        if (i==22):
                break
        i=i+1

# Age Program
while(1):
        age = int(input("Enter Age : \n"))
        if age>18:
                print("Congratulation!! You are aligible..")
                break
        else:
                print("Please try again")
                continue

        
                

