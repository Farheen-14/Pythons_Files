# Q. using other file and find out the mobile numbers, how much it is available and saved in other output file using re.
'''
import re
f1 =open('re_input.txt','r')
f2 = open('re_output.txt','w')
for line in f1:
    match = re.findall('[6-9]\d{9}',line)
    for i in match:
        f2.write(i+'\n')
print("All mobile no's are available in output.txt file")
f1.close()
f2.close()  
'''
# output : All mobile no's are available in output.txt file 

#########################################################################################################

# Q. Web scrapping program to get the title of given sites...

'''
import re,urllib
import urllib.request
sites= ['https://www.youtube.com','https://www.google.com','https://www.w3schools.com/python']
for s in sites:
    print("Searching...",s)
    u = urllib.request.urlopen(s)
    text = u.read()
    title = re.findall('<title>.*</title>',str(text),re.IGNORECASE)
    print("The title is : ",title[0])
  '''  
# . - anything 
# *- any times of char...

# output : 

# Searching... https://www.youtube.com
# The title is :  <title>YouTube</title>
# Searching... https://www.google.com
# The title is :  <title>Google</title>
# Searching... https://www.w3schools.com/python
# The title is :  <title>Python Tutorial</title> (0755) 4444121 +919945600000

#########################################################################################################

# import re,urllib
# import urllib.request
# s = urllib.request.urlopen('https://www.redbus.in/info/contactus')
# text = s.read()
# match= re.findall('[+][91][0-9]{10}',str(text))
# for i in match: 
#       print(i)

#########################################################################################################

# read mobile number from redbus.in 

'''
import re,urllib
import urllib.request
s = urllib.request.urlopen('https://www.redbus.in/info/contactus')
text = s.read()
match = re.findall('[+][91][0-9]{9}',str(text))
for i in match:
      print(i)
'''
# output :

# +9199456000
# +9199456000
# +9199456000
# +9199456000

#########################################################################################################

# Q. Check email id is valid or not?

import re
n = input("Enter email-ID : ")
# match= re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com',n)
match= re.fullmatch('\w[a-zA-Z0-9_.]*@[a-zA-Z0-9]+[.][a-z]+',n)
if match!=None:
  print("Valid Email-ID")
else:
  print("Invalid Email-ID")
  

# output :
# Enter email-ID : hghekjkfh@yahoo.in
# Valid Email-ID