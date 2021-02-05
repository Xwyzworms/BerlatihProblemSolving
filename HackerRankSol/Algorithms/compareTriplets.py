def compareTriplets(a, b):
    al=0
    bl=0 
    for i in range(len(a)):
        if (a[i] > b[i]):
           al+=1
        elif (a[i] < b[i]):
            bl+=1
    