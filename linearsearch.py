# pos = -1
# def search(list, n):
#     i = 0
#     while i < len(list):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#         i = i+1
#     return False
# list = [3,5,6,2,1,8,9]
# n = 8
# if search(list, n):
#     print("No. is found", pos+1)
# else:
#     print("No. is not found")

pos = -1        #its a global variable 
def search(list, n):
    i = 0
    while i <len(list):
        if list[i]==n:
            globals()['pos']= i 
            return True
        i = i+1
    return False


list = [3,5,1,6,8,9,22,11]
n = 6
if search(list, n):
    print("Number is found \n","Position is : ", pos+1)
else:
    print("Number is not found")