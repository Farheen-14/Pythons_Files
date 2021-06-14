# Q.Simple program in function using position argument 
# def cal(a,b):
#     sum = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return sum,sub, mul, div
# t= cal(10,20) 
# for i in t:
#     print(i)
    
# Q.Pring some of given numbers, don't know how many numbers i am passing 

# def sum(*n):
#     res = 0
#     for i in n:
#         res = res+i
#     print("The sum of the number is : ",res)
# sum()
# sum(10)
# sum(10,20)
# sum(10,20,30)

# Global/Local Variables....
a=33
def f1():
    a=20
    print("The global value is :",globals()['a'])
    print("f1 :",a)
def f2():
    print("f2 :",a)
f1()
f2()
    
        