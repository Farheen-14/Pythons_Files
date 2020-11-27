# f = open('mydata.txt', 'r')
# # print(f.read())
# f1 = open('writedata', 'w')
# f1.write("Hello Farheen.. i am your write data... \n")
# f1.write("Hello Minni.. i am your 2nd line  of write data..\n")
# f1 = open('writedata', 'a') 
# f1.write("Hello Minni.. its a third line..")
# print(f1)

# get all the data from read file (mydata) in output
# f = open('mydata.txt', 'r')
# f1 = open('writedata', 'w')
# for date in f:
#     print(date, end="")

# get the data from read file to write file..
f = open('mydata.txt', 'r')
f1 = open('writedata', 'w')
for date in f:
    f1.write(date)