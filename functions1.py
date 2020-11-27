# Q.Keyword valiable length argument 

# def employee(name, **data):
#     print(name)
#     print(data)
# employee('Farheen Ansari', Age= 25 , city = 'Gurgaon' , Mobile = 7835863155)

# Using for Loop

# def employee(name, **data):
#     print(name)
#     for i,j  in data.items():
#         print(i,j)
# employee('Farheen Ansari', Age= 25 , city = 'Gurgaon' , Mobile = 7835863155)

#Global Keyword Example
#  a= 8

# def add():
#     global a
#     a = 5
#     b = 6
#     c= a+b
#     print(c)
# add()

# Pass list to a function in python..

# Q. Count the total even and odd number in list using function. 

def count(int):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd

lst = [23,55,64,32,76,89,32,45,22,56]
even, odd = count(lst)
# print(even)
# print(odd)
print("Total even no. is : {} and Total odd no. is : {}".format(even,odd))