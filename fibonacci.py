# Q.1 print the fibonacchi series.... 0 1 1 2 3 5 8 13 etc...
                                    # a b c - - - -
                                    #   a b c - - -
                                    #     a b c - -
                                    #       a b c -   
# def febo(n):
#     a = 0 
#     b = 1
#     print(a)
#     print(b)
#     # n = int(input("Enter any number : "))
#     for i in range(2, n):
#         c = a + b
#         a = b 
#         b = c
#         print(c)
# febo(6)


# Q.2 - Fibonachhi series method.. Input  from user 

def fabi():
    n = int(input("Enter no. of Fabonacchi series : "))
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
fabi()


# Q. 3 Calculate Factorial .. 1*2*3*4*5 = 120

def fact():
    n = int(input("Enter a no, to calculate the factorial : "))
    f =1
    for i in range(1, n+1):
        f= f * i
    return f
    print(f)
fact()  
