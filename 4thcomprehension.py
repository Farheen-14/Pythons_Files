# Q. print square of the numbers using empty list like 1,4,9,16,25.....
# list=[]
# for i in range(1,11):
#     list.append(i*i)
# print(list) 

# in comprehension : decrease the code...

# list=[i*i for i in range(1,21) if i%2==0]
# print(list)

# output : [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q.Enter 2 string and print the unique value between both list

# l1= [10,30,20,60]
# l2= [40,10,90,20]
# list=[i for i in l1 if i not in l2]
# print(list) 
# output : [30,60]

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q.Using split() function..

# word= "hey farheen ansari, i know you are the next prime minister".split()
# print(word)
# l= [w.upper() for w in word]
# print(l)

# output : 
# ['hey', 'farheen', 'ansari,', 'i', 'know', 'you', 'are', 'the', 'next', 'prime', 'minister']
# ['HEY', 'FARHEEN', 'ANSARI,', 'I', 'KNOW', 'YOU', 'ARE', 'THE', 'NEXT', 'PRIME', 'MINISTER']

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q.Take tuple of number from the keyboard and print sum and average of the value ..

# n= eval(input("Enter a tuble numbers : "))
# s=0
# for i in n:
#     s = s+i
# print("Sum of the no. is : ",s)
# print("Average of the no. is : ",s/len(n))

# output :
# Enter a tuble numbers : (5,10,15,20,25,30) 
# Sum of the no. is :  105
# Average of the no. is :  17.5
