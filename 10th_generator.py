# l= [x*x for x in range(100000000000)]
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5])

# print(type(l))


'''l= (x*x for x in range(100000000000))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

print(type(l))

output :
0
1
4
9
16'''

'''def coutdown(num):
    while (num>0):
        yield num
        num = num-1
value = coutdown(5)
for i in value:
    print(i)
print(type(i))
print(type(value))

output : 
5
4
3
2
1
<class 'int'>
<class 'generator'>'''

# Q.Calculate fibonacci series : 0,1,1,2,3,5,8,13...

'''
def fabonacci(num):
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
value = fabonacci(13)
for i in value:
    if i >13:
        break
    print(i)'''




