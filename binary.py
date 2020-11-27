# pos = -1

# def search(list, n):
#     l = 0
#     u = len(list)-1
#     while l <= u:
#         mid = (l+u) // 2
#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid+1;
#             else:
#                 u = mid-1;

#     return False


# list = [4,7,8,12,45,99,102,702,10987,56666]
# n = 702

# if search(list, n):
#     print("Found at ",pos+1)
# else:
#     print("Not Found")
pos = -1
def search(list, n):
    l = 0   
    u = len(list)-1
    while l <= n:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False


list = [22,3,4,1,66,77,89,90,34,56,3,27,88]
n= 66
if search(list, n):
    print("Found the value at position :", pos+1)
else:
    print("Not Found")
