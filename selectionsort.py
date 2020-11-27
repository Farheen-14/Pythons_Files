def sort(n):
    for i in range(6):
        minpos = i
        for j in range(i,7):
            if n[j] < n[j+1]:
                minpos = j

    




n = [4,7,2,3,9,5,1]
sort(n)
print(n)