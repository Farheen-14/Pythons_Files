# Q. input a string and print positive and negatiive number.

# n= input("Enter a string : ")
# i = 0
# for j in n:
#     print("The positive index is : {} and negative index is : {} is {}".format(i,i-len(n),j))
#     i += 1

# s="farheenei"
# print(s[1:6:])


# 2:8:-2
# rheenei
########### ########### ########### ########### ########### ########### ########### ########### ###########
# Q. Enter a string and print into forward or backward directions..

# farheen

# s = input("Enter a string : ")
# n=len(s)
# i=0
# print("In forward direction of string..")
# while i<n:
#     print(s[i],end='')
#     i =i+1
# print()
# print("In backward direction of string value..")
# i=n-1
# while i>=0:
#     print(s[i],end='')
#     i=i-1
# print()
# print("Using slicing method for backwarding the string..")
# i = -1
# while i>=-n:
#     print(s[i],end='')
#     i = i-1

########### ########### ########### ########### ########### ########### ########### ########### ###########


# Q.2 input a string and substring, checking substring is available in string or not using (impressive operater in or not in)

# s = input("Enter a string value : ")
# subs = input("Enter a substring value : ")
# if subs in s:
#     print("Yes Substring is available in string value")
# else:
#     print("No, substring is not available is string...")

########### ########### ########### ########### ########### ########### ########### ########### ###########


# Q. input a string with int like : a4bf56sd then output will become : abfsd456 (first string then integer)
# n = input("Enter a string : ")
# s1=s2=res=""
# for i in n:
#     if i.isalpha():
#         s1=s1+i
#     else:
#         s2=s2+i
# for i in sorted(s1):
#     res = res+i
# for i in sorted(s2):
#     res = res+i
# print(res)

# print(s1+s2)

########### ########### ########### ########### ########### ########### ########### ########### ###########
   
# Q. input a string and output like below : 
#   a3b2c4 - aaaabbcccc

# n= input("Enter a string : ")
# output=''
# for i in n:
#     if i.isalpha():
#         output=output+i
#         previous = i
#     else:
#         output=output+ previous*(int(i)-1)
# print(output)

########### ########### ########### ########### ########### ########### ########### ########### ###########


#### input a3b4c2 , output- adfe ####

# char(unicode)- char(97) is a

# ord(chr)- ord(a)- calculate unicode value

# ord(chr)-- unicode value
# calculate the chr of unicode value as chr(unicode)
# ord(chr)-- unicode--chr(unicode)
# ord(value)+3 - ord(a)+3 then chr(ord(a)+3)- after a 3rd chr will print


# Q. Enter a string like a3b4c2 - output like a and after a 3rd character d , b and after 4 char f and so on..
# input a3b4c2 , output- adfe

# n = input("Enter a string : ")
# output=''
# for i in n:
#     if i.isalpha():
#         output=output+i
#         previous = i 
#     else:
#         newchar= chr(ord(previous)+int(i))
#         output=output+newchar
# print(output)

########### ########### ########### ########### ########### ########### ########### ########### ###########

# Q.Enter 2 string input from typing import MappingView
# from user and print the 1st char of 1st string and 
# 2nd char of 2nd string and so on. if rest available in 1st or 2nd string then, it will print on last..
# ex- 1st string- hello
#     2nd string - Mini 
# output :  hmeilnlio

s1 = input("Enter 1st string : ")
s2 = input("Enter 2nd string : ")
output=''
i=j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output= output+s1[i]
        i= i+1
    if i<len(s2):
        output= output+s2[j]
        j= j+1
print(output)
    



