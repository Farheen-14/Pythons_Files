# Solutions 1

# from numpy import *

# arr1 =array([2,5,6,1,8,99,33])
# arr2 = array([4,5,7,8,2,1,1])
# arr3 = arr1 + arr2

# print(arr3)

# Solutions 2 
# from numpy import *

# arr1 = array([
#     [2,5,6,9,4,15],
#     [5,7,9,8,9,44]
# ])

# arr2 = arr1.flatten() #flatten - it used to 2 dimentional array to 1 single array, "flat the array clear called".
# # arr3 = arr2.reshape(2,4) # 2 is row and 4 is for column. (it dived into rows and columns which we are mentioning in this reshape value)
# # print(arr2)
# # print(arr3)

# arr4 = arr2.reshape(2,2,3) # 2- two step 1 by 1,  2 - rows and 3- column
# print(arr4)


# matrix array 


from numpy import *

m = matrix('2,3,4 ; 2,3,4 ; 3,5,6') # semicolon ; is used to devided into rows and columns
print(m)

# a= matrix('2,3 / 4,5 / 2, 1')
# print(a)