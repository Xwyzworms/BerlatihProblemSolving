def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    n = len(arr)
    for i in range(n):
        if arr[i] < 0:
            neg +=1
        elif arr[i] == 0:
            zero += 1
        else:
            pos +=1
    
    print(round(pos/n,6))
    print(round(neg/n,6))
    print(round(zero/n,6))