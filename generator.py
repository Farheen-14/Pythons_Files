def topten():
    n=1
    
    while n<=10:
        sq = n*n
        yield sq    #we are not using print, return statement because print - print the value and stop the program here, return - return the value and stop the progrm but yeild pass the statement and not stopping , it go ahead method.
        n += 1

values = topten()

for i in values:
    print(i)

