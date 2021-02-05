def miniMaxSum(arr):
    arr=sorted(arr)
    minima = sum(arr[:-1])
    maxima = sum(arr[1:])
    
    print(minima,maxima)