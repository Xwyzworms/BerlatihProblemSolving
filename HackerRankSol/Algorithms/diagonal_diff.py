def diagonalDifference(arr):
    firstDiag = []
    secondDiag = []
    n = len(arr)
    for i in range(n):
        firstDiag.append(arr[i][i])
        secondDiag.append(arr[i][n-i-1])
    diff = math.fabs(sum(firstDiag) - sum(secondDiag))
    return int(diff)