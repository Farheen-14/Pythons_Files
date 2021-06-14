
word = input("Enter any word : ")
d={}
for i in word:
    d[i]=d.get(i,0)+1
for k,v in d.items():
    print(k,"Occured : ",v,"times")

# output :

# Enter any word : minni
# m Occured :  1 times
# i Occured :  2 times
# n Occured :  2 times