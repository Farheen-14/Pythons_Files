# Q. calculating the start,end and group value available in provided strings and count the same.
'''
import re
count=0
pattern= re.compile('ab')
matcher =pattern.finditer('abaabaab')
for match in matcher:
    count += 1
    print("The ab is available  at the position of : ",match.start())
    print("Start : {},End with {} and Total Group : {}".format(match.start(),match.end(),match.group()))
print("The total no's of occurence are : ",count)
'''

'''
output :

The ab is available  at the position of :  0
Start : 0,End with 2 and Total Group : ab
The ab is available  at the position of :  3
Start : 3,End with 5 and Total Group : ab
The ab is available  at the position of :  6
Start : 6,End with 8 and Total Group : ab
The total no's of occurence are :  3
'''
# regular expression functions  
# compile()
# finditer()
# start()
# end()
# group()


#########################################################################################################

# Q.checking all alphabets and digits and symbols 

'''
import re
count=0
match = re.finditer('[abc]','ndhahjbkdc')
for m in match:
    count +=1
    print("Start : ",m.start(),".....End : ",m.end(),"....Group : ",m.group(),"......Count : ",count)
'''

'''
output :

Start :  3 .....End :  4 ....Group :  a ......Count :  1
Start :  6 .....End :  7 ....Group :  b ......Count :  2
Start :  9 .....End :  10 ....Group :  c ......Count :  3
'''

#########################################################################################################

# Predefined Character in Regular Expression 
'''
import re
count=0
match = re.finditer('[^a-z0-9]','n8dj5dj$jh8hg@c')
match = re.finditer('[^a-zA-Z0-9]','n8dA8B%j5j$jh8hg@c')
for m in match:
    count +=1
    print("Start....",m.start(),"End.....",m.end(),"Group.....",m.group(),"Count....",count)

output :

Start.... 6 End..... 7 Group..... % Count.... 1
Start.... 10 End..... 11 Group..... $ Count.... 2
Start.... 16 End..... 17 Group..... @ Count.... 3
'''

#########################################################################################################

# Quantifires in Regular Expression
'''
import re
count=0
match = re.finditer('a{2}','abaaba')
# match = re.finditer('[^a-zA-Z0-9]','n8dA8B%j5j$jh8hg@c')
for m in match:
    count +=1
    print("Start....",m.start(),"Group.....",m.group(),"Count....",count)'''


# output :
# a{2} = aa meaning 
# Start.... 2 Group..... aa Count.... 1

#########################################################################################################

# Q.match the 10 digit of mobile no. ...it is valid or not using re.
# [6-9]\d{8}
'''
import re
n = input("Enter 10-digit mobile no. to check : ")
match = re.fullmatch('[6-9]\d{9}',n)
if match!=None:
    print(n,"Correct matched...")
else:
    print(n,"Not matched...")
'''

# output :
# Enter 10-digit mobile no. to check : 9889099090
# 9889099090 Correct matched...



