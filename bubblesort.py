def sort(n):
    for i in range(len(n)-1, 0,-1):
        for j in range(i):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp


n = [3,6,2,9,6,5,4,1]
sort(n)
print(n)